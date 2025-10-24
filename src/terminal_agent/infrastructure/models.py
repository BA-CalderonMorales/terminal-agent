"""Model adapters for external LLM providers.

This module provides adapters and wrappers for integrating external
language model providers like Ollama.
"""

from langchain_ollama import ChatOllama


def create_ollama_model(
    model_name: str = "llama3.2",
    base_url: str = "http://localhost:11434",
    temperature: float = 0.7,
) -> ChatOllama:
    """Create and configure a ChatOllama model instance.
    
    Args:
        model_name: Name of the Ollama model to use.
        base_url: URL where Ollama is running.
        temperature: Model temperature for response generation (0.0 to 1.0).
        
    Returns:
        A configured ChatOllama model instance.
    """
    return ChatOllama(
        model=model_name,
        base_url=base_url,
        temperature=temperature,
    )
