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


        response = await llm.responses.create(
            model="gpt-6-luna",
            instructions=(
                "You are an assistant, that give clear and simple explanation. "
                "Use the available MCP tools when appropriate."
            ),
            input="What is 5 plus 15?",
            tools=llm_tools
        )

        for call in response.output:
            if call.type == "function_call":

                arguments = json.loads(call.arguments)

                print(f"Calling tool: {call.name}")
                print(f"Arguments: {arguments}")

                result = await client.call_tool(
                    call.name,
                    arguments
                )

                print("Tool result:", result.structured_content)

if __name__ == "__main__":
    anyio.run(main)