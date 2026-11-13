import anyio
import json

from mcp import Client, StdioServerParameters
from openai import AsyncOpenAI
from dotenv import load_dotenv

load_dotenv()

llm = AsyncOpenAI()


async def main():
    server = StdioServerParameters(
        command="python",
        args=["server/server.py"]
    )

    async with Client(server) as client:
        tools = await client.list_tools()

        print("Available tools:")

        llm_tools = []

        for tool in tools.tools:
            print(f"- {tool.name}")

            llm_tools.append({
                "type": "function",
                "name": tool.name,
                "description": tool.description,
                "parameters": tool.input_schema,
                "strict": False
            })

        test_case = [
            ("FYPLC-54", "What is 21+21?"),
            ("FYPLC-55", "Can you greet a person called Alex?"),
            ("FYPLC-56", "Retrieve a list of colours available"),
            ("FYPLC-57", "What does MCP (Model Context Protocol) stand for?")
        ]

        for test_no, prompt in test_case:
            print(f"\n --- {test_no} ---")

            input_message = [
                {
                    "role": "user",
                    "content": prompt
                }
            ] 

            for _ in range(5):
                response = await llm.responses.create(
                    model="gpt-6-luna",
                    instructions=(
                        "You are an assistant, that give clear and simple explanation. "
                        "Use the available MCP tools when appropriate."
                    ),
                    input=input_message,
                    tools=llm_tools
                )

                input_message.extend(response.output)

                tool_called = False

                for call in response.output:
                    if call.type == "function_call":
                        tool_called = True

                        arguments = json.loads(call.arguments)

                        print(f"Calling tool: {call.name}")
                        print(f"Arguments: {arguments}")

                        result = await client.call_tool(
                            call.name,
                            arguments
                        )

                        print("Tool result:", result.structured_content)

                        input_message.append(
                            {
                                "type": "function_call_output",
                                "call_id": call.call_id,
                                "output": json.dumps(result.structured_content),
                            }
                        )

                if not tool_called:
                    print("\nLLM:", response.output_text)
                    break

if __name__ == "__main__":
    anyio.run(main)