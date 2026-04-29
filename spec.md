# Specification: Browser-Use MCP Server

## Overview
This project implements a Model Context Protocol (MCP) server that provides a specialized prompt for web browsing tasks and a tool to execute those tasks using the `browser-use` library. The server allows LLMs to delegate complex web-based research and automation to a dedicated agent that can navigate websites, interact with elements, and return the execution history.

## Architecture
The server is built using the Python MCP SDK and integrates with:
- **browser-use**: For high-level browser automation.
- **Playwright/CDP**: To connect to a browser instance (local or remote).
- **LangChain/DeepSeek**: As the underlying LLM driving the browser agent.

## MCP Components

### 1. Prompts
The server exposes a prompt named `browser_command` which helps users structure their requests for the browser agent.

- **Name**: `browser_command`
- **Arguments**:
  - `task` (string, required): The description of what the browser should do (e.g., "Search for the latest news on SpaceX").
- **Template**:
  ```text
  You are a web automation expert. Please execute the following task using the browser:
  {{task}}
  
  Provide a detailed summary of your findings and the steps taken.
  ```

### 2. Tools
The server provides a tool to trigger the browser agent execution.

- **Name**: `run_browser_task`
- **Description**: Executes a natural language task in a web browser and returns the history of actions and results.
- **Input Schema**:
  ```json
  {
    "type": "object",
    "properties": {
      "task": {
        "type": "string",
        "description": "The task for the browser agent to perform"
      },
      "max_steps": {
        "type": "integer",
        "description": "Maximum number of steps the agent should take",
        "default": 50
      }
    },
    "required": ["task"]
  }
  ```
- **Output**: A JSON-formatted string containing the `AgentHistory` (steps, screenshots, and final result).

### 3. Resources (Optional/Future)
- **`browser://history`**: A dynamic resource that provides the history of the last executed task.

## Technical Implementation Details

### Environment Variables
- `LLM_DEEPSEEK_API_KEY`: Required for the `ChatDeepSeek` model.
- `CDP_URL`: URL for a remote browser instance via Chrome DevTools Protocol.

### Dependencies & Environment
- **Python**: >= 3.13
- **Package Manager**: `uv`
- **Framework**: `fastmcp` for rapid MCP server development.
- `browser-use`: Agentic browser automation framework.
- `langchain-deepseek`: Integration for DeepSeek LLMs.

## Usage Example
When a client (like Claude Desktop) connects to this MCP server:
1. The user selects the `browser_command` prompt.
2. The user provides a task.
3. The LLM uses the `run_browser_task` tool to fulfill the request.
4. The server initializes the `Agent`, connects to the browser via CDP, and streams the execution.
5. The final history is returned to the LLM to summarize for the user.

## Success Criteria
- [ ] MCP server starts and listens for JSON-RPC connections over stdio.
- [ ] `browser_command` prompt is correctly registered and discoverable.
- [ ] `run_browser_task` tool successfully triggers `agent.run()`.
- [ ] Browsing history is captured and returned as a tool response.
- [ ] Errors (e.g., timeout, navigation failure) are gracefully handled and reported back through the MCP protocol.
