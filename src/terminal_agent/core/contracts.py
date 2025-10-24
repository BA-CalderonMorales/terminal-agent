"""Core contracts and interfaces for the terminal agent system."""

from typing import Any, Dict, Protocol


class IAgent(Protocol):
    """Interface for agent implementations.
    
    Agents are autonomous entities that can process queries,
    reason about tasks, and execute tools to accomplish goals.
    """

    def invoke(self, query: str) -> Dict[str, Any]:
        """Execute the agent synchronously with a query.
        
        Args:
            query: The question or task for the agent.
            
        Returns:
            A dictionary containing the agent's response.
        """
        ...

    async def ainvoke(self, query: str) -> Dict[str, Any]:
        """Execute the agent asynchronously with a query.
        
        Args:
            query: The question or task for the agent.
            
        Returns:
            A dictionary containing the agent's response.
        """
        ...


class ITool(Protocol):
    """Interface for tool implementations.
    
    Tools are functions that agents can invoke to perform
    specific operations or interact with external systems.
    """

    name: str
    description: str

    def invoke(self, **kwargs: Any) -> str:
        """Execute the tool with given parameters.
        
        Args:
            **kwargs: Tool-specific parameters.
            
        Returns:
            The result of the tool execution as a string.
        """
        ...
