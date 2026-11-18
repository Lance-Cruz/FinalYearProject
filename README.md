# FinalYearProject

Final Year Project investigating security vulnerabilities in Large Language Model (LLM) systems that interact with external tools using the Model Context Protocol (MCP).

## Current Implementation

- Basic MCP server exposing a set of tools.
- MCP client that connects to the server using stdio.
- LLM interacting with MCP tools.
- Interactive chat loop allowing users to communicate with the LLM through the terminal.

## How It Works

1. The user enters a prompt through the terminal.
2. The MCP client sends the prompt and available tool definitions to the LLM.
3. The LLM determines whether an MCP tool is required.
4. If required, the MCP client executes the tool through the MCP server and returns the result to the LLM.
5. The LLM generates a response which is displayed to the user.

## Setup

Create a virtual environment:

```bash
python -m venv .venv
```

Activate the virtual environment for your operating system:

<details>
<summary>Windows (Git Bash)</summary>

```bash
source .venv/Scripts/activate
```

</details>

<details>
<summary>Windows (PowerShell)</summary>

```powershell
.venv\Scripts\Activate.ps1
```

</details>
<details>
<summary>Linux / macOS</summary>

```bash
source .venv/bin/activate
```

</details>

Install dependencies:

```bash
pip install -r requirements.txt
```

## OpenAI API Configuration

Rename `.env.example` to `.env` in the root directory of the project and add your OpenAI API key:

```env
OPENAI_API_KEY=your_api_key_here
```

## Running the MCP Environment

Run the MCP client:

```bash
python client/client.py
```

This starts the MCP client, connects to the MCP server using stdio, discovers the available tools and starts an interactive chat session with the LLM.

Users can enter prompts directly through the terminal, allowing the LLM to interact with the tools exposed by the MCP server when required.

## Manual Testing

For manual development and testing, the MCP can still be used if needed:

```bash
npx @modelcontextprotocol/inspector uv run --with "mcp[cli]" mcp run server/server.py
```