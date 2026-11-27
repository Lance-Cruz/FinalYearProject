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

@mcp.tool()
def get_private_documents() -> list[dict]:
    """Retrieve all private documents from the database."""
    return queries.fetch_private_documents()

@mcp.tool()
def create_private_document(
    owner_id: str, title: str, content: str
) -> dict:
    """Create a private document in the database."""
    return queries.create_private_document(
        owner_id, title, content
    )

@mcp.tool()
def update_private_document(
    document_id: int, owner_id: str, title: str, content: str
) -> dict | None:
    """Update a private document by document ID and owner ID."""
    return queries.update_private_document(
        document_id, owner_id, title, content
    )

@mcp.tool()
def delete_private_document(
    document_id: int, owner_id: str
) -> bool:
    """Delete a private document by document ID and owner ID."""
    return queries.delete_private_document(
        document_id, owner_id
    )

if __name__ == "__main__":
    mcp.run()