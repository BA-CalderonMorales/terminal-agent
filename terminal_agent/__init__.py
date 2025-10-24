"""Terminal Agent - Minimalistic implementation of agents with LangChain."""

from terminal_agent.deep_agent import DeepAgent, create_deep_agent
from terminal_agent.tools import get_default_tools

__version__ = "0.1.0"
__all__ = ["DeepAgent", "create_deep_agent", "get_default_tools"]
