"""Advanced usage example showing direct DeepAgent usage.

This example demonstrates:
- Direct instantiation of ChatOllama model
- Creating a DeepAgent with custom configuration
- Using the agent for multi-step reasoning
"""

from src.terminal_agent import DeepAgent, get_default_tools
from src.terminal_agent.infrastructure.models import create_ollama_model


def main():
    """Run advanced deep agent examples."""
    print("=" * 60)
    print("Advanced Deep Agent Example")
    print("=" * 60)
    print()
    
    # Step 1: Create and configure the ChatOllama model explicitly
    print("Creating ChatOllama model wrapper...")
    try:
        model = create_ollama_model(
            model_name="llama3.2",
            base_url="http://localhost:11434",
            temperature=0.5,  # Lower temperature for more focused responses
        )
        print("Model wrapper created")
    except Exception as e:
        print(f"Error creating model: {e}")
        print("\nMake sure Ollama is running:")
        print("  ollama serve")
        return
    
    print()
    
    # Step 2: Define tools
    print("Loading tools...")
    tools = get_default_tools()
    print(f"Loaded {len(tools)} tools")
    print()
    
    # Step 3: Create the deep agent with custom prompt
    print("Creating DeepAgent with custom system prompt...")
    
    custom_system_prompt = """You are an advanced AI assistant specialized in mathematics and text analysis.
When solving problems:
1. Break down the problem into steps
2. Use the available tools to perform calculations or analysis
3. Explain your reasoning clearly
4. Provide the final answer

Available tools allow you to:
- Perform mathematical calculations
- Analyze text (length, word count, reversal)
"""
    
    agent = DeepAgent(
        model=model,
        tools=tools,
        system_prompt=custom_system_prompt,
        verbose=True,
    )
    print("DeepAgent created")
    print()
    
    # Step 4: Use the agent for complex multi-step reasoning
    queries = [
        "Calculate the result of (25 * 8) + (100 / 4), then tell me how many digits are in the answer",
        "If I have a string 'Hello World', what is its length and what does it look like reversed?",
    ]
    
    for i, query in enumerate(queries, 1):
        print(f"\n{'=' * 60}")
        print(f"Complex Query {i}:")
        print(f"{query}")
        print("=" * 60)
        
        try:
            result = agent.invoke(query)
            print(f"\nFinal Answer:")
            print(result['output'])
            print()
            print(f"Total messages in conversation: {len(result['messages'])}")
        except Exception as e:
            print(f"Error: {e}")
        
        print()


if __name__ == "__main__":
    main()
