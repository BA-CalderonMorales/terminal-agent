# Agents Architecture

## Overview

This document describes the architecture and design decisions for the Terminal Agent project. It serves as a guide for all AI tooling and developers working on this codebase.

## Architecture Style

### Domain-Driven Design (DDD)
The project follows DDD principles to maintain clear boundaries between business logic and infrastructure concerns.

**Domain Layer** (`src/terminal_agent/core/`)
- Contains core business logic
- Domain models and entities
- Business rules and validations
- Pure Python with minimal dependencies

**Application Layer** (`src/terminal_agent/agents/`)
- Agent implementations
- Use case orchestration
- Agent lifecycle management

**Infrastructure Layer** (`src/terminal_agent/infrastructure/`)
- External dependencies (LangChain, Ollama)
- Model adapters and wrappers
- Configuration management

### Vertical Slice Architecture
Features are organized as vertical slices that cut through all layers:

```
Feature: Deep Agent
├── Core: DeepAgent domain model
├── Application: Agent creation and invocation
├── Infrastructure: ChatOllama adapter
└── Tools: Tool definitions and execution
```

Benefits:
- Clear feature boundaries
- Easy to understand and maintain
- Reduced coupling between features
- Facilitates parallel development

## Project Structure

```
terminal-agent/
├── src/                           # Source code root
│   └── terminal_agent/            # Main package
│       ├── core/                  # Core domain logic
│       │   ├── __init__.py
│       │   ├── agent.py           # Agent domain model
│       │   └── contracts.py       # Interfaces/protocols
│       ├── agents/                # Agent implementations
│       │   ├── __init__.py
│       │   ├── deep_agent.py      # Deep agent implementation
│       │   └── factory.py         # Agent factory
│       ├── tools/                 # Tool definitions
│       │   ├── __init__.py
│       │   ├── base.py            # Tool base classes
│       │   └── default_tools.py   # Default tool implementations
│       └── infrastructure/        # External dependencies
│           ├── __init__.py
│           ├── models.py          # Model adapters (ChatOllama)
│           └── config.py          # Configuration
├── examples/                      # Usage examples
├── tests/                         # Test suite
├── docs/                          # Documentation
├── AGENTS.md                      # This file
├── .github/
│   └── copilot-instructions.md   # AI tooling instructions
└── README.md                      # Project overview
```

## Design Principles

### SOLID Principles

**Single Responsibility Principle (SRP)**
- Each class/module has one reason to change
- DeepAgent: manages agent lifecycle
- Tools: execute specific operations
- Factory: creates agent instances

**Open/Closed Principle (OCP)**
- Open for extension, closed for modification
- Add new tools without modifying existing code
- Extend agent behavior through composition

**Liskov Substitution Principle (LSP)**
- Subtypes must be substitutable for base types
- All tools implement the same interface
- Agent implementations are interchangeable

**Interface Segregation Principle (ISP)**
- Clients depend on minimal interfaces
- Tool interface is minimal and focused
- Agent interface exposes only necessary methods

**Dependency Inversion Principle (DIP)**
- Depend on abstractions, not concretions
- Core depends on contracts, not implementations
- Infrastructure implements contracts from core

### DRY (Don't Repeat Yourself)
- Extract common functionality into shared modules
- Use inheritance/composition to reuse code
- Avoid duplicating business logic

### YAGNI (You Aren't Gonna Need It)
- Implement only what is needed now
- Avoid speculative features
- Keep the design simple and focused

## Core Concepts

### Agent
An agent is an autonomous entity that can:
- Process user queries
- Reason about tasks
- Execute tools to accomplish goals
- Return structured responses

### Tool
A tool is a function that an agent can invoke:
- Has a clear name and description
- Accepts typed parameters
- Returns a result
- Can be composed with other tools

### Model Adapter
Wraps external LLM providers:
- Abstracts provider-specific details
- Provides consistent interface
- Handles connection and configuration

## Boundaries and Contracts

### Core Contracts
```python
# Protocol for agent implementations
class IAgent(Protocol):
    def invoke(self, query: str) -> dict: ...
    async def ainvoke(self, query: str) -> dict: ...

# Protocol for tool implementations
class ITool(Protocol):
    name: str
    description: str
    def invoke(self, **kwargs) -> str: ...
```

### Dependency Flow
```
Core (Domain) <-- Application <-- Infrastructure
     ^                                   |
     |                                   |
     +------- Interfaces -----------------+
```

- Core defines interfaces
- Infrastructure implements interfaces
- Application orchestrates core and infrastructure
- Dependencies point inward (toward core)

## Extension Points

### Adding New Tools
1. Create tool in `src/terminal_agent/tools/`
2. Implement tool interface
3. Register with tool registry
4. Tool is automatically available to agents

### Adding New Agent Types
1. Define agent in `src/terminal_agent/agents/`
2. Implement IAgent interface
3. Add factory method if needed
4. Agent can be instantiated and used

### Adding New Model Providers
1. Create adapter in `src/terminal_agent/infrastructure/models/`
2. Implement model interface
3. Configure in infrastructure layer
4. Use with any agent implementation

## Testing Strategy

### Unit Tests
- Test each component in isolation
- Mock external dependencies
- Focus on business logic

### Integration Tests
- Test component interactions
- Use real dependencies when appropriate
- Verify end-to-end workflows

### Test Organization
```
tests/
├── unit/
│   ├── test_agents.py
│   └── test_tools.py
├── integration/
│   └── test_agent_execution.py
└── fixtures/
    └── common_fixtures.py
```

## Best Practices

### Code Organization
- Keep modules small and focused
- One class per file when appropriate
- Group related functionality together

### Naming Conventions
- Use clear, descriptive names
- Avoid abbreviations unless standard
- Follow PEP 8 naming conventions

### Error Handling
- Use specific exception types
- Provide helpful error messages
- Log errors appropriately

### Documentation
- Document public APIs
- Explain complex logic
- Keep documentation up to date
- No emojis in documentation

### Security
- Validate all inputs
- Restrict dangerous operations
- Follow principle of least privilege
- Regular security audits

## References

- Domain-Driven Design by Eric Evans
- Clean Architecture by Robert C. Martin
- LangChain Documentation: https://python.langchain.com
- LangChain Deep Agents: https://docs.langchain.com/oss/python/deepagents/overview
