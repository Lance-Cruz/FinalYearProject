from mcp.server import MCPServer

mcp = MCPServer("Basic MCP Server")

@mcp.tool()
def add(a: int, b: int) -> int:
    """Add two numbers."""
    return a + b

@mcp.tool()
def greeting(name: str) -> str:
    """return a simple greeting."""
    return f"Hello {name}"