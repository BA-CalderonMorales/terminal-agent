# Use Microsoft Container Registry Python image for better Codespaces compatibility
FROM mcr.microsoft.com/devcontainers/python:3.12

# Install uv - the fast Python package installer and resolver
COPY --from=ghcr.io/astral-sh/uv:latest /uv /usr/local/bin/uv

# Configure uv to use a local virtual environment in the workspace
ENV UV_PROJECT_ENVIRONMENT="/workspace/.venv"
ENV PATH="/workspace/.venv/bin:$PATH"
ENV VIRTUAL_ENV="/workspace/.venv"
