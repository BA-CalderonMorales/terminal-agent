# Quick Start Guide

Get up and running with Deep Agents in 5 minutes!

## Installation

### 1. Install Ollama

**macOS/Linux:**
```bash
curl -fsSL https://ollama.com/install.sh | sh
```

**Windows:** Download from [ollama.com](https://ollama.com/)

### 2. Start Ollama and Pull a Model

```bash
# Start Ollama (in a separate terminal)
ollama serve

# Pull a model
ollama pull llama3.2
```

### 3. Install Terminal Agent

```bash
git clone https://github.com/BA-CalderonMorales/terminal-agent.git
cd terminal-agent
pip install -r requirements.txt
```

## Your First Agent

Create a file called `my_agent.py`:

```python
from src.terminal_agent import create_deep_agent, get_default_tools

# Create agent
tools = get_default_tools()
agent = create_deep_agent(model_name="llama3.2", tools=tools)

# Use the agent
result = agent.invoke("What is 15 multiplied by 7?")
print(result['output'])
```

Run it:
```bash
python my_agent.py
```

## That's It! 🎉

You now have a working Deep Agent that can:
- Perform calculations
- Analyze text
- Reason through multi-step problems

## Next Steps

- Read the [Usage Guide](USAGE.md) for more examples
- Learn to [create custom tools](USAGE.md#creating-custom-tools)
- Check out the [examples](../examples/) directory
- Explore [Deep Agents documentation](https://docs.langchain.com/oss/python/deepagents/overview)

## Common Issues

**"Connection refused" error?**
→ Make sure `ollama serve` is running

**"Model not found" error?**
→ Run `ollama pull llama3.2`

**Slow responses?**
→ Try a smaller model: `ollama pull llama3.2:1b`

## Available Models

| Model | Size | Best For |
|-------|------|----------|
| llama3.2:1b | 1B | Fast, simple tasks |
| llama3.2 | 3.2B | General purpose (recommended) |
| llama3.1 | 8B | Complex reasoning |
| mistral | 7B | Balanced performance |
| codellama | 7B | Code-related tasks |

List all available models:
```bash
ollama list
```
