from mcp.server import MCPServer

from database import queries

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
    return queries.fetch_public_documents()

@mcp.tool()
def create_public_document(title: str, content: str) -> dict:
    """Create a public document in the database."""
    return queries.create_public_documents(title, content)

@mcp.tool()
def update_public_document(
    document_id: int, title: str, content: str
) -> dict | None:
    """Update the title and content of a public document by ID."""
    return queries.update_public_document(
        document_id, title, content
    )

@mcp.tool()
def delete_public_document(document_id: int) -> bool:
    """Delete a public document by ID; return whether it was deleted."""
    return queries.delete_public_document(document_id)

if __name__ == "__main__":
    mcp.run()