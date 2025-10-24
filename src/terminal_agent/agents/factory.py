"""Factory for creating agent instances.

This module provides convenience functions for creating configured agent instances
with sensible defaults.
"""

from typing import List, Optional

from langchain_core.tools import BaseTool

from src.terminal_agent.agents.deep_agent import DeepAgent
from src.terminal_agent.infrastructure.models import create_ollama_model


def create_deep_agent(
    model_name: str = "llama3.2",
    base_url: str = "http://localhost:11434",
    tools: Optional[List[BaseTool]] = None,
    temperature: float = 0.7,
    system_prompt: Optional[str] = None,
    verbose: bool = True,
) -> DeepAgent:
    """Create a deep agent with an Ollama model and tools.
    
    This is a convenience function that wraps model creation and agent initialization.
    
    Args:
        model_name: Name of the Ollama model to use (default: "llama3.2").
        base_url: URL where Ollama is running (default: "http://localhost:11434").
        tools: List of tools for the agent. If None, uses default tools.
        temperature: Model temperature for response generation (0.0 to 1.0).
        system_prompt: Optional custom system prompt for the agent.
        verbose: Whether to print verbose output during execution.
        
    Returns:
        A configured DeepAgent instance.
        
    Example:
        >>> from src.terminal_agent.agents.factory import create_deep_agent
        >>> from src.terminal_agent.tools.default_tools import get_default_tools
        >>> tools = get_default_tools()
        >>> agent = create_deep_agent(model_name="llama3.2", tools=tools)
        >>> result = agent.invoke("What is the weather like today?")
    """
    model = create_ollama_model(
        model_name=model_name,
        base_url=base_url,
        temperature=temperature,
    )
    
    if tools is None:
        from src.terminal_agent.tools.default_tools import get_default_tools
        tools = get_default_tools()
    
    return DeepAgent(
        model=model,
        tools=tools,
        system_prompt=system_prompt,
        verbose=verbose,
    )
