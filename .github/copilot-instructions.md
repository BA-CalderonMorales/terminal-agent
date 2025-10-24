# Copilot Instructions for Terminal Agent

## Code Style and Standards

### NO EMOJIS
- **NEVER** use emojis in code, comments, or documentation
- Use clear, descriptive text instead
- Example: Instead of "Creating agent..." use "Creating agent..."

### Architecture
- Follow Domain-Driven Design (DDD) principles
- Use Vertical Slice Architecture for feature organization
- Keep code modular and organized in src/ directory

### Design Principles
- **SOLID**: Single Responsibility, Open/Closed, Liskov Substitution, Interface Segregation, Dependency Inversion
- **DRY**: Don't Repeat Yourself - extract common functionality
- **YAGNI**: You Aren't Gonna Need It - avoid over-engineering

### Project Structure
```
src/
├── terminal_agent/
│   ├── core/              # Domain models and core business logic
│   ├── agents/            # Agent implementations
│   ├── tools/             # Tool definitions
│   └── infrastructure/    # External dependencies and adapters
```

### Code Organization
- Each module should have a clear, single responsibility
- Keep related code together (vertical slices)
- Separate concerns: business logic, infrastructure, presentation

### Documentation
- Use clear, professional language
- Avoid casual language or emojis
- Focus on technical accuracy and clarity
- Reference AGENTS.md for architecture decisions

### Testing
- Write unit tests for all business logic
- Test tools independently
- Ensure security through testing

### Security
- Never use unrestricted eval()
- Validate all inputs
- Use type hints for better code safety
- Follow principle of least privilege
