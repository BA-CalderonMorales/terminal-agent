"""Deep Agent implementation using LangChain and Ollama.

This module provides the core DeepAgent implementation that can use tools
and reason about complex tasks using local models through Ollama.
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
        verbose: Whether to print verbose output during execution.
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
        
        if system_prompt is None:
            system_prompt = (
                "You are a helpful AI assistant with access to tools. "
                "Use the available tools to answer questions and accomplish tasks. "
                "Think step by step and explain your reasoning."
            )
        
        self.system_prompt = system_prompt
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
        final_message = result["messages"][-1]
        
        return {
            "output": final_message.content,
            "messages": result["messages"],
        }
