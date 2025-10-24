"""Tests for terminal_agent.tools module."""

import pytest
from terminal_agent.tools import (
    calculator,
    string_length,
    reverse_string,
    count_words,
    get_default_tools,
)


def test_calculator():
    """Test calculator tool."""
    assert calculator.invoke("2 + 2") == "4"
    assert calculator.invoke("10 * 5") == "50"
    assert calculator.invoke("100 / 4") == "25.0"


def test_string_length():
    """Test string_length tool."""
    assert string_length.invoke("hello") == "5"
    assert string_length.invoke("") == "0"
    assert string_length.invoke("Hello, World!") == "13"


def test_reverse_string():
    """Test reverse_string tool."""
    assert reverse_string.invoke("hello") == "olleh"
    assert reverse_string.invoke("abc") == "cba"
    assert reverse_string.invoke("") == ""


def test_count_words():
    """Test count_words tool."""
    assert count_words.invoke("hello world") == "2"
    assert count_words.invoke("one") == "1"
    assert count_words.invoke("") == "0"
    assert count_words.invoke("The quick brown fox") == "4"


def test_get_default_tools():
    """Test get_default_tools function."""
    tools = get_default_tools()
    assert len(tools) == 4
    tool_names = [tool.name for tool in tools]
    assert "calculator" in tool_names
    assert "string_length" in tool_names
    assert "reverse_string" in tool_names
    assert "count_words" in tool_names
