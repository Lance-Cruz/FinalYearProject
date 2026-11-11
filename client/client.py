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

        add_tool = await client.call_tool("add", {"a": 5, "b": 15})
        greeting_tool = await client.call_tool("greeting", {"name": "Lance"})
        get_colors_tool = await client.call_tool("get_colors", {})

        print(add_tool.structured_content)
        print(greeting_tool.structured_content)
        print(get_colors_tool.structured_content)

        response = await llm.responses.create(
            model="gpt-6-luna",
            instructions=(
                "You are an assistant, that give clear and simple explanation. "
                "Use the available MCP tools when appropriate."
            ),
            input="What is 5 plus 15?",
            tools=llm_tools
        )

        print("\nLLM response: ", response.output)

if __name__ == "__main__":
    anyio.run(main)