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

Run the MCP environment:

    python client/client.py

This runs client and connect to the MCP server using stdio, then interact with the tools exposed by server.

For manual development and testing, the MCP can still be used if needed:

    npx @modelcontextprotocol/inspector uv run --with "mcp[cli]" mcp run server/server.py