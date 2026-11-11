import anyio

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

        for tool in tools.tools:
            print(f"- {tool.name}")

        add_tool = await client.call_tool("add", {"a": 5, "b": 15})
        greeting_tool = await client.call_tool("greeting", {"name": "Lance"})
        get_colors_tool = await client.call_tool("get_colors", {})

        print(add_tool.structured_content)
        print(greeting_tool.structured_content)
        print(get_colors_tool.structured_content)

        response = await llm.responses.create(
            model="gpt-6-luna",
            instructions="You are an assistant, that gives clear and simple explanation",
            input="Hello, what is MCP? (Model Context Protocol)",
        )

        print(response.output_text)

if __name__ == "__main__":
    anyio.run(main)