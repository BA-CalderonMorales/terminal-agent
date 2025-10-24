"""Tools for Deep Agents.

This module provides example tools that can be used with deep agents.
Tools allow agents to interact with external systems and perform actions.
"""

from typing import List
from langchain_core.tools import tool, BaseTool


@tool
def calculator(expression: str) -> str:
    """Evaluate a mathematical expression.
    
    Args:
        expression: A mathematical expression to evaluate (e.g., "2 + 2" or "10 * 5").
        
    Returns:
        The result of the calculation as a string.
        
    Example:
        >>> calculator("2 + 2")
        "4"
    """
    try:
        # Safely evaluate mathematical expressions using restricted eval
        # Only allow basic math operations and numbers
        allowed_names = {
            "abs": abs,
            "round": round,
            "min": min,
            "max": max,
            "sum": sum,
            "pow": pow,
        }
        # Compile in eval mode with restricted globals
        code = compile(expression, "<string>", "eval")
        # Execute with no builtins and only allowed functions
        result = eval(code, {"__builtins__": {}}, allowed_names)
        return str(result)
    except Exception as e:
        return f"Error evaluating expression: {str(e)}"


@tool
def string_length(text: str) -> str:
    """Calculate the length of a string.
    
    Args:
        text: The text to measure.
        
    Returns:
        The length of the text as a string.
        
    Example:
        >>> string_length("Hello, World!")
        "13"
    """
    return str(len(text))


@tool
def reverse_string(text: str) -> str:
    """Reverse a string.
    
    Args:
        text: The text to reverse.
        
    Returns:
        The reversed text.
        
    Example:
        >>> reverse_string("hello")
        "olleh"
    """
    return text[::-1]


@tool
def count_words(text: str) -> str:
    """Count the number of words in a text.
    
    Args:
        text: The text to analyze.
        
    Returns:
        The number of words as a string.
        
    Example:
        >>> count_words("Hello world, how are you?")
        "5"
    """
    words = text.split()
    return str(len(words))


def get_default_tools() -> List[BaseTool]:
    """Get the default set of tools for deep agents.
    
    Returns:
        A list of BaseTool instances that can be used with agents.
        
    Example:
        >>> from terminal_agent import get_default_tools, create_deep_agent
        >>> tools = get_default_tools()
        >>> agent = create_deep_agent(tools=tools)
    """
    return [
        calculator,
        string_length,
        reverse_string,
        count_words,
    ]
