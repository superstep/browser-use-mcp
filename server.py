import os
from fastmcp import FastMCP
from browser_use import Agent, Browser
from browser_use.llm.deepseek.chat import ChatDeepSeek

# Initialize FastMCP server
mcp = FastMCP("Browser-Use Server")

# Configure browser
# Note: Using CDP URL from spec/original code if available, otherwise default
CDP_URL = os.getenv("CDP_URL", "http://192.168.0.111:9223")

@mcp.tool()
async def run_browser_task(task: str, max_steps: int = 50) -> str:
    """
    Executes a natural language task in a web browser and returns the history of actions and results.
    """
    api_key = os.getenv("LLM_DEEPSEEK_API_KEY")
    if not api_key:
        return "Error: LLM_DEEPSEEK_API_KEY environment variable is not set."

    browser = Browser(
        cdp_url=CDP_URL,
        headless=False,
    )

    agent = Agent(
        task=task,
        llm=ChatDeepSeek(
            api_key=api_key,
        ),
        browser=browser,
    )

    try:
        history = await agent.run(max_steps=max_steps)
        # Return history as string (FastMCP handles string return)
        return str(history)
    except Exception as e:
        return f"Error executing browser task: {str(e)}"
    finally:
        # Browser cleanup is handled by browser-use or context if managed, 
        # but here we rely on the instance lifecycle.
        pass

@mcp.prompt()
def browser_command(task: str) -> str:
    """
    A prompt to help structure web browsing tasks.
    """
    return f"""You are a web automation expert. Please execute the following task using the browser:
{task}

Provide a detailed summary of your findings and the steps taken."""

if __name__ == "__main__":
    mcp.run()
