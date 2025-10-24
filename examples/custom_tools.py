"""Advanced example with custom tools for Deep Agents.

This example shows how to create custom tools and use them with deep agents.
"""

from typing import List
from langchain_core.tools import tool, BaseTool
from src.terminal_agent import create_deep_agent


# Define custom tools
@tool
def get_current_time() -> str:
    """Get the current time in a readable format.
    
    Returns:
        Current time as a string.
    """
    from datetime import datetime
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")


@tool
def to_uppercase(text: str) -> str:
    """Convert text to uppercase.
    
    Args:
        text: The text to convert.
        
    Returns:
        The text in uppercase.
    """
    return text.upper()


@tool
def to_lowercase(text: str) -> str:
    """Convert text to lowercase.
    
    Args:
        text: The text to convert.
        
    Returns:
        The text in lowercase.
    """
    return text.lower()


def get_custom_tools() -> List[BaseTool]:
    """Get a custom set of tools.
    
    Returns:
        List of custom tools.
    """
    return [
        get_current_time,
        to_uppercase,
        to_lowercase,
    ]


def main():
    """Run advanced deep agent example with custom tools."""
    print("=" * 60)
    print("Advanced Deep Agent Example with Custom Tools")
    print("=" * 60)
    print()
    
    # Get custom tools
    tools = get_custom_tools()
    print(f"Loaded {len(tools)} custom tools: {[tool.name for tool in tools]}")
    print()
    
    # Create deep agent with custom system prompt
    print("Creating deep agent with custom tools...")
    
    custom_prompt = (
        "You are a helpful assistant that can manipulate text and provide time information. "
        "Always use the available tools to answer questions accurately."
    )
    
    try:
        agent = create_deep_agent(
            model_name="llama3.2",
            tools=tools,
            system_prompt=custom_prompt,
            temperature=0.7,
            verbose=True,
        )
        print("Deep agent created successfully!")
        print()
    except Exception as e:
        print(f"Error creating agent: {e}")
        print("\nMake sure Ollama is running and you have pulled the model:")
        print("  ollama pull llama3.2")
        return
    
    # Example queries
    queries = [
        "What is the current time?",
        "Convert the text 'Hello World' to uppercase",
        "Convert 'PYTHON PROGRAMMING' to lowercase",
    ]
    
    for i, query in enumerate(queries, 1):
        print(f"\n{'=' * 60}")
        print(f"Query {i}: {query}")
        print("=" * 60)
        
        try:
            result = agent.invoke(query)
            print(f"\nFinal Answer: {result['output']}")
        except Exception as e:
            print(f"Error: {e}")
        
        print()


if __name__ == "__main__":
    main()
