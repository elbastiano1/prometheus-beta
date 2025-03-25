import pytest
from src.string_to_path_case import string_to_path_case

def test_camel_case_conversion():
    """Test converting camelCase to path-case."""
    assert string_to_path_case("helloWorld") == "hello-world"
    assert string_to_path_case("camelCaseString") == "camel-case-string"

def test_pascal_case_conversion():
    """Test converting PascalCase to path-case."""
    assert string_to_path_case("HelloWorld") == "hello-world"
    assert string_to_path_case("PascalCaseString") == "pascal-case-string"

def test_snake_case_conversion():
    """Test converting snake_case to path-case."""
    assert string_to_path_case("hello_world") == "hello-world"
    assert string_to_path_case("snake_case_string") == "snake-case-string"

def test_mixed_case_conversion():
    """Test converting mixed case strings to path-case."""
    assert string_to_path_case("Mixed Case String") == "mixed-case-string"
    assert string_to_path_case("Another Mixed_Case String") == "another-mixed-case-string"

def test_single_word():
    """Test single word conversion."""
    assert string_to_path_case("hello") == "hello"
    assert string_to_path_case("HELLO") == "hello"

def test_multiple_hyphens():
    """Test handling of multiple consecutive hyphens."""
    assert string_to_path_case("Multiple-----Hyphens") == "multiple-hyphens"

def test_edge_cases():
    """Test edge cases with special characters."""
    assert string_to_path_case("hello-world") == "hello-world"
    assert string_to_path_case("hello_World") == "hello-world"

def test_error_cases():
    """Test error handling."""
    with pytest.raises(TypeError):
        string_to_path_case(123)
    
    with pytest.raises(TypeError):
        string_to_path_case(None)
    
    with pytest.raises(ValueError):
        string_to_path_case("")