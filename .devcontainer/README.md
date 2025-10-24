# Development Container Configuration

This directory contains the configuration for a VS Code development container that provides a consistent development environment for the terminal-agent project.

## What's Included

- **Python 3.12**: Latest stable Python version
- **uv**: Fast Python package installer and resolver (https://github.com/astral-sh/uv)
- **VS Code Extensions**: Pre-configured with essential Python development extensions
  - Python language support (Pylance)
  - Black formatter
  - Ruff linter
  - GitHub Copilot
  - And more...
- **Development Tools**: Common tools like git, GitHub CLI, pytest, and ipython

## Getting Started

### Prerequisites

- [VS Code](https://code.visualstudio.com/)
- [Docker Desktop](https://www.docker.com/products/docker-desktop)
- [Dev Containers extension](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers)

### Using the Dev Container

1. Open this repository in VS Code
2. When prompted, click "Reopen in Container" (or use Command Palette: `Dev Containers: Reopen in Container`)
3. Wait for the container to build and initialize
4. The post-create command will automatically set up your Python environment

## Working with uv

### Common Commands

```bash
# Add a new dependency
uv add langchain

# Add a development dependency
uv add --dev pytest

# Sync dependencies (if pyproject.toml exists)
uv sync

# Run a Python script
uv run python script.py

# Install a package directly
uv pip install package-name

# Create/update requirements.txt
uv pip freeze > requirements.txt
```

### Project Structure

The virtual environment is created at `/workspace/.venv` and is automatically activated in the terminal.

## Customization

### Adding VS Code Extensions

Edit `.devcontainer/devcontainer.json` and add extension IDs to the `extensions` array.

### Modifying Python Version

Edit `.devcontainer/Dockerfile` and change the base image (e.g., `FROM python:3.11-slim`).

### Adding System Dependencies

Edit `.devcontainer/Dockerfile` and add packages to the `apt-get install` command.

## Troubleshooting

### Container won't build

- Ensure Docker Desktop is running
- Try rebuilding without cache: Command Palette → `Dev Containers: Rebuild Container Without Cache`

### uv commands not working

- The virtual environment should be automatically activated
- If not, run: `source /workspace/.venv/bin/activate`

### Python interpreter not detected

- VS Code should automatically detect the interpreter at `/workspace/.venv/bin/python`
- If not, manually select it: Command Palette → `Python: Select Interpreter`

## Learn More

- [VS Code Dev Containers Documentation](https://code.visualstudio.com/docs/devcontainers/containers)
- [uv Documentation](https://github.com/astral-sh/uv)
