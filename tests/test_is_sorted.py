import pytest
from src.is_sorted import is_sorted

def test_empty_list():
    """Test that an empty list is considered sorted"""
    assert is_sorted([]) == True

def test_single_element_list():
    """Test that a single-element list is considered sorted"""
    assert is_sorted([42]) == True

def test_ascending_sorted_list():
    """Test a list sorted in ascending order"""
    assert is_sorted([1, 2, 3, 4, 5]) == True

def test_descending_sorted_list():
    """Test a list sorted in descending order"""
    assert is_sorted([5, 4, 3, 2, 1], ascending=False) == True

def test_unsorted_list_ascending():
    """Test an unsorted list when ascending order is expected"""
    assert is_sorted([1, 3, 2, 4, 5]) == False

def test_unsorted_list_descending():
    """Test an unsorted list when descending order is expected"""
    assert is_sorted([5, 3, 4, 2, 1], ascending=False) == False

def test_list_with_duplicates_ascending():
    """Test a sorted list with duplicate elements in ascending order"""
    assert is_sorted([1, 2, 2, 3, 3, 4]) == True

def test_list_with_duplicates_descending():
    """Test a sorted list with duplicate elements in descending order"""
    assert is_sorted([4, 3, 3, 2, 2, 1], ascending=False) == True

def test_float_list():
    """Test sorting with float numbers"""
    assert is_sorted([1.1, 2.2, 3.3, 4.4]) == True

def test_mixed_numeric_types():
    """Test sorting with mixed numeric types"""
    assert is_sorted([1, 2.0, 3, 4.5]) == True

def test_invalid_input_type():
    """Test that a TypeError is raised for non-list input"""
    with pytest.raises(TypeError):
        is_sorted("not a list")

def test_incomparable_elements():
    """Test that a TypeError is raised for incomparable elements"""
    with pytest.raises(TypeError):
        is_sorted([1, 'a', 2])

def test_complex_comparable_list():
    """Test sorting with custom comparable objects"""
    class ComparableObject:
        def __init__(self, value):
            self.value = value
        
        def __lt__(self, other):
            return self.value < other.value
        
        def __gt__(self, other):
            return self.value > other.value

    sorted_objects = [
        ComparableObject(1), 
        ComparableObject(2), 
        ComparableObject(3)
    ]
    assert is_sorted(sorted_objects) == True