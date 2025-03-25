import pytest
from src.alternating_camel_case import to_alternating_camel_case

def test_basic_conversion():
    """Test basic string conversion to alternating camel case."""
    assert to_alternating_camel_case("hello world") == "hElLoWoRlD"
    assert to_alternating_camel_case("python is awesome") == "pYtHoNiSaWeSoMe"

def test_empty_string():
    """Test conversion of an empty string."""
    assert to_alternating_camel_case("") == ""

def test_single_word():
    """Test conversion of a single word."""
    assert to_alternating_camel_case("hello") == "hElLo"

def test_mixed_case_input():
    """Test input with mixed case."""
    assert to_alternating_camel_case("Hello WORLD") == "hElLoWoRlD"

def test_input_with_multiple_spaces():
    """Test input with multiple spaces."""
    assert to_alternating_camel_case("  hello   world  ") == "hElLoWoRlD"

def test_invalid_input_type():
    """Test that TypeError is raised for non-string input."""
    with pytest.raises(TypeError):
        to_alternating_camel_case(123)
    
    with pytest.raises(TypeError):
        to_alternating_camel_case(None)

def test_special_characters():
    """Test input with special characters."""
    assert to_alternating_camel_case("hello! world@") == "hElLoWoRlD"