# Usage Guide for Deep Agents

This guide provides detailed examples and best practices for using deep agents with terminal-agent.

## Table of Contents

- [Quick Start](#quick-start)
- [Creating a Deep Agent](#creating-a-deep-agent)
- [Using Default Tools](#using-default-tools)
- [Creating Custom Tools](#creating-custom-tools)
- [Advanced Configuration](#advanced-configuration)
- [Best Practices](#best-practices)

## Quick Start

The simplest way to get started:

```python
from terminal_agent import create_deep_agent, get_default_tools

# Create agent with default settings
agent = create_deep_agent()

# Invoke with a query
result = agent.invoke("What is 15 multiplied by 7?")
print(result['output'])
```

## Creating a Deep Agent

### Basic Creation

```python
from terminal_agent import create_deep_agent, get_default_tools

tools = get_default_tools()
agent = create_deep_agent(
    model_name="llama3.2",
    tools=tools,
    temperature=0.7,
    verbose=True
)
```

### With Custom System Prompt

```python
agent = create_deep_agent(
    model_name="llama3.2",
    tools=tools,
    system_prompt="You are a helpful math tutor. Always explain your reasoning step by step.",
    verbose=True
)
```

### Using a Different Ollama Instance

```python
agent = create_deep_agent(
    model_name="llama3.2",
    base_url="http://remote-server:11434",  # Custom Ollama server
    tools=tools
)
```

## Using Default Tools

The library provides several default tools:

### Calculator

```python
result = agent.invoke("What is (25 * 4) + 17?")
```

### String Operations

```python
# Get string length
result = agent.invoke("How many characters are in 'Hello World'?")

# Reverse string
result = agent.invoke("Reverse the text 'LangChain'")

# Count words
result = agent.invoke("How many words are in 'The quick brown fox'?")
```

## Creating Custom Tools

### Simple Tool

```python
from langchain_core.tools import tool
from terminal_agent import create_deep_agent

@tool
def get_weather(location: str) -> str:
    """Get the weather for a location.
    
    Args:
        location: The city or location to get weather for.
        
    Returns:
        Weather information as a string.
    """
    # In a real application, this would call a weather API
    return f"The weather in {location} is sunny and 72°F"

# Create agent with custom tool
agent = create_deep_agent(tools=[get_weather])
result = agent.invoke("What's the weather in San Francisco?")
```

### Tool with Multiple Parameters

```python
@tool
def search_database(query: str, limit: int = 10) -> str:
    """Search a database for records.
    
    Args:
        query: The search query.
        limit: Maximum number of results to return.
        
    Returns:
        Search results as a string.
    """
    return f"Found {limit} results for '{query}'"

agent = create_deep_agent(tools=[search_database])
result = agent.invoke("Search for users named 'John', show 5 results")
```

### Combining Multiple Custom Tools

```python
from typing import List
from langchain_core.tools import tool, BaseTool

@tool
def add_numbers(a: float, b: float) -> str:
    """Add two numbers."""
    return str(a + b)

@tool
def multiply_numbers(a: float, b: float) -> str:
    """Multiply two numbers."""
    return str(a * b)

def get_math_tools() -> List[BaseTool]:
    """Get math-related tools."""
    return [add_numbers, multiply_numbers]

agent = create_deep_agent(tools=get_math_tools())
```

## Advanced Configuration

### Adjusting Temperature

Temperature controls randomness in responses:

```python
# More focused and deterministic (good for factual tasks)
agent = create_deep_agent(temperature=0.3)

# More creative (good for brainstorming)
agent = create_deep_agent(temperature=0.9)
```

### Using the DeepAgent Class Directly

For more control, use the `DeepAgent` class:

```python
from langchain_ollama import ChatOllama
from terminal_agent import DeepAgent, get_default_tools

# Create model explicitly
model = ChatOllama(
    model="llama3.2",
    base_url="http://localhost:11434",
    temperature=0.7,
)

# Create agent
tools = get_default_tools()
agent = DeepAgent(
    model=model,
    tools=tools,
    system_prompt="Custom system prompt here",
    verbose=True
)

# Use the agent
result = agent.invoke("Your query here")
```

### Async Usage

For async operations:

```python
import asyncio
from terminal_agent import create_deep_agent, get_default_tools

async def main():
    agent = create_deep_agent()
    result = await agent.ainvoke("What is 5 + 5?")
    print(result['output'])

asyncio.run(main())
```

## Best Practices

### 1. Choose the Right Model

- **Small tasks**: Use `llama3.2:1b` for speed
- **General tasks**: Use `llama3.2` (default)
- **Complex tasks**: Use `llama3.1` or larger models

### 2. Optimize Tool Descriptions

Good tool descriptions help the agent understand when to use each tool:

```python
@tool
def analyze_sentiment(text: str) -> str:
    """Analyze the sentiment of a text.
    
    Use this tool when you need to determine if text is positive, negative, or neutral.
    
    Args:
        text: The text to analyze.
        
    Returns:
        Sentiment classification (positive, negative, or neutral).
    """
    # Implementation here
    pass
```

### 3. Handle Errors Gracefully

```python
try:
    result = agent.invoke(query)
    print(result['output'])
except Exception as e:
    print(f"Error: {e}")
    # Handle error appropriately
```

### 4. Use Verbose Mode for Debugging

```python
agent = create_deep_agent(verbose=True)  # See agent's reasoning process
```

### 5. Limit Tool Scope

Only include tools that are relevant to your use case to improve agent performance.

## Examples

See the [examples](../examples/) directory for complete working examples:

- `basic_usage.py` - Basic agent usage with default tools
- `custom_tools.py` - Creating and using custom tools

## Additional Resources

- [LangChain Deep Agents Documentation](https://docs.langchain.com/oss/python/deepagents/overview)
- [Ollama Documentation](https://ollama.com/docs)
- [LangChain Tools Documentation](https://python.langchain.com/docs/modules/agents/tools/)
