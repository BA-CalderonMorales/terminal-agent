"""Deep Agent implementation using LangChain and Ollama.

This module provides functionality to create and use deep agents with local models
through Ollama. Deep agents can utilize tools and reason about complex tasks.
"""

from typing import Any, Dict, List, Optional

from langchain_ollama import ChatOllama
from langchain_core.messages import HumanMessage, SystemMessage
from langchain_core.tools import BaseTool
from langgraph.prebuilt import create_react_agent


class DeepAgent:
    """A deep agent that can use tools and reason with a local Ollama model.
    
    This class wraps a ChatOllama model with tools to create an agent that can
    perform complex reasoning and task execution using LangGraph's ReAct agent.
    
    Attributes:
        model: The ChatOllama model instance.
        tools: List of tools available to the agent.
        agent: The agent executor that runs the agent.
        system_prompt: The system prompt used by the agent.
    """

    def __init__(
        self,
        model: ChatOllama,
        tools: List[BaseTool],
        system_prompt: Optional[str] = None,
        verbose: bool = True,
    ):
        """Initialize a DeepAgent.
        
        Args:
            model: ChatOllama model instance to use.
            tools: List of tools the agent can use.
            system_prompt: Optional custom system prompt for the agent.
            verbose: Whether to print verbose output during execution.
        """
        self.model = model
        self.tools = tools
        self.verbose = verbose
        
        # Default system prompt for deep agents
        if system_prompt is None:
            system_prompt = (
                "You are a helpful AI assistant with access to tools. "
                "Use the available tools to answer questions and accomplish tasks. "
                "Think step by step and explain your reasoning."
            )
        
        self.system_prompt = system_prompt
        
        # Create the agent using LangGraph's prebuilt ReAct agent
        self.agent = create_react_agent(model, tools)
    
    def invoke(self, query: str) -> Dict[str, Any]:
        """Invoke the agent with a query.
        
        Args:
            query: The question or task for the agent.
            
        Returns:
            A dictionary containing the agent's response and intermediate steps.
        """
        messages = [
            SystemMessage(content=self.system_prompt),
            HumanMessage(content=query)
        ]
        
        result = self.agent.invoke({"messages": messages})
        
        # Extract the final response
        final_message = result["messages"][-1]
        
        return {
            "output": final_message.content,
            "messages": result["messages"],
        }
    
    async def ainvoke(self, query: str) -> Dict[str, Any]:
        """Asynchronously invoke the agent with a query.
        
        Args:
            query: The question or task for the agent.
            
        Returns:
            A dictionary containing the agent's response and intermediate steps.
        """
        messages = [
            SystemMessage(content=self.system_prompt),
            HumanMessage(content=query)
        ]
        
        result = await self.agent.ainvoke({"messages": messages})
        
        # Extract the final response
        final_message = result["messages"][-1]
        
        return {
            "output": final_message.content,
            "messages": result["messages"],
        }


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
        >>> from terminal_agent import create_deep_agent, get_default_tools
        >>> tools = get_default_tools()
        >>> agent = create_deep_agent(model_name="llama3.2", tools=tools)
        >>> result = agent.invoke("What is the weather like today?")
    """
    # Wrap the model with ChatOllama
    model = ChatOllama(
        model=model_name,
        base_url=base_url,
        temperature=temperature,
    )
    
    # Use default tools if none provided
    if tools is None:
        from terminal_agent.tools import get_default_tools
        tools = get_default_tools()
    
    # Create and return the deep agent
    return DeepAgent(
        model=model,
        tools=tools,
        system_prompt=system_prompt,
        verbose=verbose,
    )
