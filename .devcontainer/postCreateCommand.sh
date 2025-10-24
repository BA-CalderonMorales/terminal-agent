#!/bin/bash
set -e

echo "Setting up your development environment..."

# Check if pyproject.toml exists
if [ -f "pyproject.toml" ]; then
    echo "Found pyproject.toml, installing dependencies with uv..."
    uv sync
elif [ -f "requirements.txt" ]; then
    echo "Found requirements.txt, installing dependencies with uv..."
    uv venv
    uv pip install -r requirements.txt
else
    echo "No dependency files found. Creating a virtual environment..."
    uv venv
    echo "You can add dependencies later with: uv add <package-name>"
fi

# Install common development tools
echo "Installing common development tools..."
uv pip install --quiet black ruff pytest ipython 2>/dev/null || true

echo "Development environment setup complete!"
echo ""
echo "Useful commands:"
echo "  - uv add <package>        : Add a new dependency"
echo "  - uv sync                 : Sync dependencies from pyproject.toml"
echo "  - uv run <command>        : Run a command in the virtual environment"
echo "  - uv pip install <package>: Install a package directly"
echo ""
