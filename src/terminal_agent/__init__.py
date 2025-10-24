"""Terminal Agent - Minimalistic implementation of agents with LangChain."""

from src.terminal_agent.agents.deep_agent import DeepAgent
from src.terminal_agent.agents.factory import create_deep_agent
from src.terminal_agent.tools.default_tools import get_default_tools

__version__ = "0.1.0"
__all__ = ["DeepAgent", "create_deep_agent", "get_default_tools"]
