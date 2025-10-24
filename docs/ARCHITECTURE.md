# Architecture Documentation

This document explains the architecture and design decisions of the terminal-agent project.

## Overview

Terminal-agent is a minimalistic implementation of Deep Agents using LangChain and Ollama. It enables running AI agents with local language models, eliminating the need for external API calls.

## Architecture Diagram

```
┌─────────────────────────────────────────────────────────────┐
│                         User Application                     │
│                  (examples/basic_usage.py)                   │
└────────────────────────┬────────────────────────────────────┘
                         │
                         │ uses
                         ▼
┌─────────────────────────────────────────────────────────────┐
│              terminal_agent Package                          │
│  ┌──────────────────────────────────────────────────────┐  │
│  │           create_deep_agent()                        │  │
│  │  - Factory function for creating agents              │  │
│  └───────────────────┬──────────────────────────────────┘  │
│                      │                                      │
│                      │ creates                              │
│                      ▼                                      │
│  ┌──────────────────────────────────────────────────────┐  │
│  │           DeepAgent Class                            │  │
│  │  - Wraps model and tools                             │  │
│  │  - Manages agent lifecycle                           │  │
│  │  - Provides invoke() and ainvoke() methods           │  │
│  └───────────────────┬──────────────────────────────────┘  │
│                      │                                      │
│                      │ uses                                 │
│                      ▼                                      │
│  ┌──────────────────────────────────────────────────────┐  │
│  │         LangGraph ReAct Agent                        │  │
│  │  (from langgraph.prebuilt)                           │  │
│  │  - Implements reasoning and action loop             │  │
│  │  - Manages tool calling                              │  │
│  └───────────────────┬──────────────────────────────────┘  │
│                      │                                      │
└──────────────────────┼──────────────────────────────────────┘
                       │
        ┌──────────────┴──────────────┐
        │                             │
        ▼                             ▼
┌───────────────────┐         ┌───────────────────┐
│   ChatOllama      │         │      Tools        │
│   Model Wrapper   │         │  - calculator     │
│                   │         │  - string_length  │
│  - llama3.2      │         │  - reverse_string │
│  - mistral       │         │  - count_words    │
│  - codellama     │         │  - custom tools   │
└────────┬──────────┘         └───────────────────┘
         │
         │ communicates with
         ▼
┌───────────────────┐
│  Ollama Server    │
│  (localhost:11434)│
│                   │
│  - Model runtime  │
│  - GPU/CPU mgmt   │
└───────────────────┘
```

## Components

### 1. DeepAgent Class

**Location:** `terminal_agent/deep_agent.py`

**Purpose:** Main agent class that orchestrates model and tools.

**Key Methods:**
- `__init__()`: Initializes agent with model, tools, and system prompt
- `invoke()`: Synchronously processes a query
- `ainvoke()`: Asynchronously processes a query

**Design Decisions:**
- Uses LangGraph's `create_react_agent` for ReAct (Reasoning + Acting) pattern
- Wraps responses in a consistent format with `output` and `messages` keys
- Accepts custom system prompts for specialized behavior

### 2. ChatOllama Model Wrapper

**Location:** `langchain_ollama.ChatOllama` (external library)

**Purpose:** Provides a LangChain-compatible interface to Ollama models.

**Configuration:**
- `model`: Name of the Ollama model (e.g., "llama3.2")
- `base_url`: Ollama server URL (default: "http://localhost:11434")
- `temperature`: Response randomness (0.0 = deterministic, 1.0 = creative)

### 3. Tools System

**Location:** `terminal_agent/tools.py`

**Purpose:** Provides reusable functions that agents can call.

**Default Tools:**
1. **calculator**: Safely evaluates mathematical expressions
2. **string_length**: Counts characters in text
3. **reverse_string**: Reverses text
4. **count_words**: Counts words in text

**Tool Design Pattern:**
```python
@tool
def tool_name(param: type) -> str:
    """Tool description for the agent.
    
    Args:
        param: Parameter description.
        
    Returns:
        Result description.
    """
    # Implementation
    return result
```

### 4. Factory Function

**Location:** `terminal_agent/deep_agent.py`

**Function:** `create_deep_agent()`

**Purpose:** Convenience function for creating agents with sensible defaults.

**Benefits:**
- Simplifies agent creation
- Provides default configuration
- Reduces boilerplate code

## Data Flow

### Query Processing Flow

```
1. User calls agent.invoke("query")
   │
   ▼
2. DeepAgent wraps query in system + human messages
   │
   ▼
3. LangGraph ReAct agent processes messages
   │
   ├─▶ [Reasoning] Analyzes what needs to be done
   │   │
   │   ▼
   ├─▶ [Tool Selection] Decides which tool(s) to use
   │   │
   │   ▼
   ├─▶ [Tool Execution] Calls selected tool(s)
   │   │
   │   ▼
   └─▶ [Response Generation] Formulates final answer
   │
   ▼
4. ChatOllama model generates responses
   │
   ▼
5. Ollama server runs model inference
   │
   ▼
6. Result returned to user
```

### Message Format

Messages follow LangChain's message format:
```python
{
    "messages": [
        SystemMessage(content="system prompt"),
        HumanMessage(content="user query"),
        AIMessage(content="agent reasoning"),
        ToolMessage(content="tool result"),
        AIMessage(content="final answer")
    ]
}
```

## Security Considerations

### 1. Calculator Tool Safety

The calculator tool uses restricted `eval()`:
- No access to `__builtins__`
- Only allows specific safe functions (abs, round, min, max, sum, pow)
- Prevents arbitrary code execution

### 2. Ollama Local Execution

- All model inference happens locally
- No data sent to external APIs
- User has full control over model and data

### 3. Tool Restrictions

- Tools are explicitly defined and scoped
- No dynamic tool loading from untrusted sources
- Each tool has clear input/output contracts

## Performance Considerations

### Model Selection

| Factor | Small Models (1B) | Medium Models (3B) | Large Models (8B+) |
|--------|-------------------|--------------------|--------------------|
| Speed | Fast | Moderate | Slow |
| Quality | Basic | Good | Excellent |
| Memory | ~2GB | ~4GB | ~8GB+ |

### Optimization Strategies

1. **Use appropriate model size** for your task
2. **Lower temperature** for faster, more focused responses
3. **Limit tool count** to reduce decision overhead
4. **Use async methods** for concurrent operations
5. **Enable GPU acceleration** in Ollama when available

## Extension Points

### Adding Custom Tools

```python
from langchain_core.tools import tool

@tool
def my_custom_tool(input: str) -> str:
    """Description for the agent."""
    # Your implementation
    return result

agent = create_deep_agent(tools=[my_custom_tool])
```

### Custom System Prompts

```python
agent = create_deep_agent(
    system_prompt="You are a specialized assistant for X..."
)
```

### Using Different Models

```python
agent = create_deep_agent(
    model_name="mistral",  # or "codellama", "llama3.1", etc.
    base_url="http://remote-server:11434"  # or remote Ollama
)
```

## Dependencies

### Core Dependencies
- **langchain (≥1.0.0)**: Agent framework
- **langchain-ollama (≥1.0.0)**: Ollama integration
- **langchain-core (≥1.0.0)**: Core abstractions
- **langgraph (≥1.0.0)**: Agent graph orchestration
- **langgraph-prebuilt (≥1.0.0)**: ReAct agent implementation
- **pydantic (≥2.0.0)**: Data validation

### Why These Versions?

LangChain 1.0+ introduced significant changes:
- Moved agent functionality to LangGraph
- Deprecated old `AgentExecutor` in favor of graph-based agents
- Improved tool calling interface
- Better async support

## Testing Strategy

### Unit Tests
- Test individual tools in isolation
- Verify tool input/output contracts
- Ensure safe execution of calculator

### Integration Tests
- Would require Ollama server running
- Test agent creation and configuration
- Verify message flow

### Current Coverage
- Tool functionality: Tested
- Agent integration: ⚠️ Requires Ollama (manual testing)

## Future Enhancements

Potential improvements:
1. **Streaming responses** for real-time output
2. **Memory/conversation history** for multi-turn dialogues
3. **More default tools** (web search, file I/O, etc.)
4. **Agent templates** for common use cases
5. **Performance monitoring** and metrics
6. **Docker support** for easier deployment

## References

- [LangChain Deep Agents](https://docs.langchain.com/oss/python/deepagents/overview)
- [LangGraph Documentation](https://langchain-ai.github.io/langgraph/)
- [Ollama Documentation](https://ollama.com/docs)
- [ReAct Paper](https://arxiv.org/abs/2210.03629)
