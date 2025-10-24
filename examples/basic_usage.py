"""Basic usage example for Deep Agents with Ollama.

This example demonstrates how to:
1. Wrap a local model with ChatOllama
2. Define tools for the agent
3. Create a deep agent with the model and tools
4. Invoke the agent with queries

Prerequisites:
- Ollama must be installed and running (see docs/SETUP.md)
- A model must be pulled (e.g., `ollama pull llama3.2`)
"""

from src.terminal_agent import create_deep_agent, get_default_tools


def main():
    """Run basic deep agent examples."""
    print("=" * 60)
    print("Deep Agent Example with Ollama")
    print("=" * 60)
    print()
    
    # Get default tools
    print("Loading default tools...")
    tools = get_default_tools()
    print(f"Loaded {len(tools)} tools: {[tool.name for tool in tools]}")
    print()
    
    # Create deep agent with Ollama model
    print("Creating deep agent with llama3.2 model...")
    try:
        agent = create_deep_agent(
            model_name="llama3.2",  # Make sure this model is pulled in Ollama
            tools=tools,
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
        "What is 15 multiplied by 7?",
        "How many characters are in the word 'artificial intelligence'?",
        "Reverse the string 'hello world'",
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
