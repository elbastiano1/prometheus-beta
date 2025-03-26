import pytest
from src.unique_char_sorter import sort_unique_chars

def test_sort_unique_chars_normal_case():
    """Test sorting unique characters in a normal string."""
    assert sort_unique_chars("hello") == ['e', 'h', 'l', 'o']

def test_sort_unique_chars_case_sensitive():
    """Test case-sensitive sorting of unique characters."""
    assert sort_unique_chars("Hello") == ['H', 'e', 'l', 'o']

def test_sort_unique_chars_empty_string():
    """Test handling of an empty string."""
    assert sort_unique_chars("") == []

def test_sort_unique_chars_repeated_chars():
    """Test sorting with repeated characters."""
    assert sort_unique_chars("banana") == ['a', 'b', 'n']

def test_sort_unique_chars_special_chars():
    """Test sorting with special characters and mixed case."""
    assert sort_unique_chars("aA1!b") == ['!', '1', 'A', 'a', 'b']

def test_sort_unique_chars_invalid_input():
    """Test handling of non-string input."""
    with pytest.raises(TypeError):
        sort_unique_chars(123)
    with pytest.raises(TypeError):
        sort_unique_chars(None)