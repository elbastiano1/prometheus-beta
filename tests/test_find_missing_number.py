import pytest
from src.find_missing_number import find_missing_number

def test_find_missing_number_basic():
    """Test finding a missing number in a standard sequence."""
    assert find_missing_number([1, 3, 4, 5]) == 2

def test_find_missing_number_at_start():
    """Test when the missing number is at the start of the sequence."""
    assert find_missing_number([2, 3, 4, 5]) == 1

def test_find_missing_number_at_end():
    """Test when the missing number is at the end of the sequence."""
    assert find_missing_number([1, 2, 3, 4]) == 5

def test_find_missing_number_large_sequence():
    """Test with a larger sequence."""
    nums = list(range(1, 10)) + list(range(11, 11))
    assert find_missing_number(nums) == 10

def test_find_missing_number_empty_list():
    """Test that an empty list raises a ValueError."""
    with pytest.raises(ValueError, match="Input list cannot be empty"):
        find_missing_number([])

def test_find_missing_number_with_repeated_numbers():
    """Ensure the function works with no duplicates."""
    with pytest.raises(ValueError):
        find_missing_number([1, 2, 2, 4])  # Invalid input with duplicates