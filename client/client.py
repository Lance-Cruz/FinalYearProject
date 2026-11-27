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
        args=["-m", "server.server"]
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

        input_message = []

        print("\nChat started. Type 'exit' to quit.")

        while True:
            user_input = input("\nUser: ").strip()

            if user_input.lower() == "exit":
                break

            if not user_input:
                continue

            input_message.append({
                "role": "user",
                "content": user_input
            })

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

                for item in response.output:
                    if item.type == "function_call":
                        tool_called = True

                        arguments = json.loads(item.arguments)

                        result = await client.call_tool(
                            item.name,
                            arguments
                        )

                        input_message.append({
                            "type": "function_call_output",
                            "call_id": item.call_id,
                            "output": result.model_dump_json()
                        })

                if not tool_called:
                    print(f"\nLLM: {response.output_text}")
                    break

            else:
                print("\nTool call limit reached.")

        print("Chat ended.")

if __name__ == "__main__":
    anyio.run(main)