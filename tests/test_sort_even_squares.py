import pytest
from src.sort_even_squares import sort_array_with_even_squares

def test_basic_sorting():
    """Test basic functionality of the function"""
    input_arr = [3, 1, 4, 2, 6, 5]
    expected = [1, 2, 3, 4, 5, 6]
    assert sort_array_with_even_squares(input_arr) == expected

def test_even_squares_descending():
    """Test that even squares are sorted in descending order"""
    input_arr = [3, 1, 4, 2, 6, 5]
    expected = [1, 6, 2, 4, 3, 5]
    assert sort_array_with_even_squares(input_arr) == expected

def test_empty_list():
    """Test handling of empty list"""
    assert sort_array_with_even_squares([]) == []

def test_only_odd_numbers():
    """Test array with only odd numbers"""
    input_arr = [7, 3, 1, 5]
    expected = [1, 3, 5, 7]
    assert sort_array_with_even_squares(input_arr) == expected

def test_only_even_numbers():
    """Test array with only even numbers"""
    input_arr = [8, 4, 2, 6]
    expected = [2, 4, 6, 8]
    assert sort_array_with_even_squares(input_arr) == expected

def test_negative_numbers():
    """Test array with negative and positive numbers"""
    input_arr = [-3, 4, -2, 1, 6, -1]
    expected = [-3, -2, 1, 4, -1, 6]
    assert sort_array_with_even_squares(input_arr) == expected

def test_invalid_input():
    """Test that invalid input raises TypeError"""
    with pytest.raises(TypeError):
        sort_array_with_even_squares("not a list")
    with pytest.raises(TypeError):
        sort_array_with_even_squares(123)
    with pytest.raises(TypeError):
        sort_array_with_even_squares(None)