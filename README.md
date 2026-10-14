# FinalYearProject
Final Year Project investigating security vulnerabilities in LLM systems that interact with external tools using the Model Context Protocol (MCP).

## Current Implementation

Basic MCP server.

## Setup

Create a virtual environment:

    python -m venv .venv

Activate it:

    source .venv/bin/activate

Install dependencies:

    pip install -r requirements.txt

Run the MCP server:

For the current development stage: the server can be tested using the MCP inspector:

    npx @modelcontextprotocol/inspector uv run --with "mcp[cli]" mcp run server/server.py

Note: This is a temporary development/testing approach. The MCP Inspector is currently being used as a client to interact with and test the server. A dedicated MCP client will be added later in the project, at which point the normal workflow will use that client instead of the Inspector.