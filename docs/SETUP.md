# Setup Guide for Deep Agents

This guide walks you through setting up the terminal-agent project with Ollama for local model usage.

## Prerequisites

- Python 3.8 or higher
- pip or conda package manager
- At least 8GB of RAM (16GB recommended for larger models)

## Step 1: Install Ollama

Ollama allows you to run large language models locally on your machine.

### Linux

```bash
curl -fsSL https://ollama.com/install.sh | sh
```

### macOS

```bash
brew install ollama
```

Or download from [ollama.com](https://ollama.com/)

### Windows

Download and install from [ollama.com](https://ollama.com/)

### Verify Installation

```bash
ollama --version
```

## Step 2: Start Ollama Service

After installation, start the Ollama service:

```bash
ollama serve
```

By default, Ollama runs on `http://localhost:11434`. Leave this terminal open or run it as a background service.

## Step 3: Pull a Model

Download a model that will be used by your agents. We recommend starting with `llama3.2`:

```bash
ollama pull llama3.2
```

Other available models:
- `llama3.2` (3.2B parameters, recommended for getting started)
- `llama3.2:1b` (1B parameters, faster but less capable)
- `llama3.1` (8B parameters, more powerful)
- `mistral` (7B parameters, good general purpose)
- `codellama` (7B parameters, optimized for code)

To see all available models:
```bash
ollama list
```

## Step 4: Install Terminal Agent Dependencies

Clone the repository and install the required Python packages:

```bash
git clone https://github.com/BA-CalderonMorales/terminal-agent.git
cd terminal-agent
pip install -r requirements.txt
```

Or install in development mode:

```bash
pip install -e .
```

## Step 5: Verify Setup

Run a simple test to verify everything is working:

```python
from terminal_agent import create_deep_agent, get_default_tools

# Create agent
tools = get_default_tools()
agent = create_deep_agent(model_name="llama3.2", tools=tools)

# Test query
result = agent.invoke("What is 2 + 2?")
print(result['output'])
```

## Troubleshooting

### Issue: "Connection refused" error

**Solution**: Make sure Ollama service is running:
```bash
ollama serve
```

### Issue: "Model not found" error

**Solution**: Pull the model first:
```bash
ollama pull llama3.2
```

### Issue: Out of memory errors

**Solution**: Try a smaller model:
```bash
ollama pull llama3.2:1b
```

Then use it in your code:
```python
agent = create_deep_agent(model_name="llama3.2:1b", tools=tools)
```

### Issue: Slow responses

**Solutions**:
- Use a smaller model
- Reduce temperature: `temperature=0.3`
- Ensure Ollama is using GPU acceleration (if available)

## Next Steps

- Check out the [Usage Guide](USAGE.md) for detailed examples
- Explore the [examples](../examples/) directory
- Read about [Deep Agents in LangChain](https://docs.langchain.com/oss/python/deepagents/overview)
