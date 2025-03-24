import pytest
from src.exponential_search import exponential_search

def test_exponential_search_basic():
    """Test basic functionality of exponential search"""
    arr = [1, 3, 5, 7, 9, 11, 13, 15]
    assert exponential_search(arr, 7) == 3
    assert exponential_search(arr, 1) == 0
    assert exponential_search(arr, 15) == 7

def test_exponential_search_not_found():
    """Test when target is not in the array"""
    arr = [1, 3, 5, 7, 9, 11, 13, 15]
    assert exponential_search(arr, 4) == -1
    assert exponential_search(arr, 16) == -1

def test_exponential_search_edge_cases():
    """Test edge cases"""
    # Single element array
    assert exponential_search([5], 5) == 0
    assert exponential_search([5], 6) == -1
    
    # Target at last element
    arr = [1, 3, 5, 7, 9, 11, 13, 15]
    assert exponential_search(arr, 15) == 7

def test_exponential_search_error_handling():
    """Test error handling for invalid inputs"""
    # Empty list
    with pytest.raises(ValueError, match="Cannot search in an empty list"):
        exponential_search([], 5)
    
    # Non-list input
    with pytest.raises(TypeError, match="Input must be a list"):
        exponential_search("not a list", 5)

def test_exponential_search_large_array():
    """Test exponential search with a larger array"""
    arr = list(range(0, 1000, 2))  # Even numbers from 0 to 998
    assert exponential_search(arr, 500) == 250
    assert exponential_search(arr, 501) == -1  # Odd number not in array

def test_exponential_search_duplicates():
    """Test array with duplicate elements"""
    arr = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5]
    assert exponential_search(arr, 3) in [3, 4, 5]  # Any index of 3 is acceptable
    assert exponential_search(arr, 4) in [6, 7, 8, 9]  # Any index of 4 is acceptable