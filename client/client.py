import anyio

from mcp import Client, StdioServerParameters


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

if __name__ == "__main__":
    anyio.run(main)