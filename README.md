# terminal-agent

Minimalistic implementation of Deep Agents with LangChain and Ollama.

This project demonstrates how to wrap local models for use with Deep Agents, enabling AI-powered automation with locally-run language models.

## Features

- 🤖 **Local Model Integration**: Use Ollama to run models locally without external API calls
- 🛠️ **Tool Support**: Create and use custom tools with your agents
- 🔧 **Easy Setup**: Simple API for creating and using deep agents
- 📚 **Well Documented**: Comprehensive guides and examples
- ⚡ **Flexible**: Support for custom prompts, multiple tools, and various models

## Quick Start

### Prerequisites

1. **Install Ollama**: Follow the [Setup Guide](docs/SETUP.md) for detailed instructions
2. **Pull a model**: `ollama pull llama3.2`
3. **Start Ollama**: `ollama serve`

### Installation

```bash
# Clone the repository
git clone https://github.com/BA-CalderonMorales/terminal-agent.git
cd terminal-agent

# Install dependencies
pip install -r requirements.txt
```

### Basic Usage

```python
from terminal_agent import create_deep_agent, get_default_tools

# Create a deep agent with default tools
tools = get_default_tools()
agent = create_deep_agent(model_name="llama3.2", tools=tools)

# Invoke the agent with a query
result = agent.invoke("What is 15 multiplied by 7?")
print(result['output'])
```

## What are Deep Agents?

Deep Agents are AI agents that can:
- **Reason** about complex tasks
- **Use tools** to interact with external systems
- **Plan** multi-step solutions
- **Learn** from feedback and intermediate results

This implementation wraps local models (via Ollama) with LangChain's agent framework to enable these capabilities without relying on external APIs.

## Project Structure

```
terminal-agent/
├── terminal_agent/        # Main package
│   ├── __init__.py       # Package exports
│   ├── deep_agent.py     # Deep agent implementation
│   └── tools.py          # Tool definitions
├── examples/             # Example scripts
│   ├── basic_usage.py    # Basic usage example
│   └── custom_tools.py   # Custom tools example
├── docs/                 # Documentation
│   ├── SETUP.md         # Setup instructions
│   └── USAGE.md         # Usage guide
├── requirements.txt      # Python dependencies
└── README.md            # This file
```

## Documentation

- **[Setup Guide](docs/SETUP.md)**: Complete setup instructions including Ollama installation
- **[Usage Guide](docs/USAGE.md)**: Detailed usage examples and best practices
- **[Examples](examples/)**: Working code examples

## Key Components

### 1. Model Wrapping with ChatOllama

```python
from langchain_ollama import ChatOllama

model = ChatOllama(
    model="llama3.2",
    base_url="http://localhost:11434",
    temperature=0.7,
)
```

### 2. Tool Definition

```python
from langchain_core.tools import tool

@tool
def calculator(expression: str) -> str:
    """Evaluate a mathematical expression."""
    return str(eval(expression))
```

### 3. Deep Agent Creation

```python
from terminal_agent import DeepAgent

agent = DeepAgent(
    model=model,
    tools=[calculator],
    verbose=True
)
```

### 4. Agent Invocation

```python
result = agent.invoke("What is 25 * 4?")
print(result['output'])
```

## Examples

### Run Basic Example

```bash
python examples/basic_usage.py
```

### Run Custom Tools Example

```bash
python examples/custom_tools.py
```

## Requirements

- Python 3.8+
- Ollama (running locally or remotely)
- LangChain and related packages (see requirements.txt)

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## Resources

- **LangChain Deep Agents**: [Documentation](https://docs.langchain.com/oss/python/deepagents/overview)
- **Ollama**: [Official Website](https://ollama.com)
- **LangChain**: [Documentation](https://python.langchain.com)

## License

MIT License - see [LICENSE](LICENSE) file for details

## Acknowledgments

This project demonstrates the integration of:
- [LangChain](https://python.langchain.com) - Framework for developing applications with LLMs
- [Ollama](https://ollama.com) - Tool for running large language models locally
- Deep Agents pattern from LangChain for advanced agent capabilities
