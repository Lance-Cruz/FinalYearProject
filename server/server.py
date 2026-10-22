from mcp.server import MCPServer

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

if __name__ == "__main__":
    mcp.run()