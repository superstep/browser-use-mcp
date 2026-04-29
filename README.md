# Browser-Use MCP Server

This project implements a Model Context Protocol (MCP) server that provides a specialized prompt for web browsing tasks and a tool to execute those tasks using the `browser-use` library.

## Prerequisites

- **Python**: >= 3.13
- **Package Manager**: [uv](https://github.com/astral-sh/uv)

## Setup

1. **Install `uv`**:
   If you don't have `uv` installed, follow the instructions on their [official website](https://github.com/astral-sh/uv).

2. **Configure Environment**:
   Create a `.env` file in the root directory (you can use `example.env` as a template):
   ```bash
   cp example.env .env
   ```
   Edit `.env` and provide your credentials:
   - `LLM_DEEPSEEK_API_KEY`: Your DeepSeek API key.
   - `CDP_URL`: URL for a remote browser instance via Chrome DevTools Protocol (e.g., `http://localhost:9222`).

3. **Install Dependencies**:
   ```bash
   uv sync
   ```

## Running the Server

To start the MCP server:

```bash
uv run browser-mcp
```

The server will start and listen for JSON-RPC connections over `stdio`.

## Features

- **Prompt**: `browser_command` - Helps structure requests for the browser agent.
- **Tool**: `run_browser_task` - Executes natural language tasks in a web browser.

## Architecture

- **FastMCP**: Framework for rapid MCP server development.
- **browser-use**: Agentic browser automation framework.
- **LangChain/DeepSeek**: Underlying LLM driving the browser agent.
