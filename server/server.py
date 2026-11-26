from mcp.server import MCPServer

from database.queries import fetch_public_documents

mcp = MCPServer("Basic MCP Server")

@mcp.tool()
def add(a: int, b: int) -> int:
    """Add two numbers."""
    return a + b

@mcp.tool()
def greeting(name: str) -> str:
    """Return a simple greeting."""
    return f"Hello {name}"

@mcp.tool()
def get_colors() -> list[str]:
    """Return a list of colors"""
    return ["red", "green", "blue"]


@mcp.tool()
def get_public_documents() -> list[dict]:
    """Retrieve all public documents from the database."""
    return fetch_public_documents()

if __name__ == "__main__":
    mcp.run()