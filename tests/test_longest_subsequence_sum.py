import pytest
from src.longest_subsequence_sum import longest_subsequence_sum

def test_basic_positive_case():
    """Test a basic positive scenario"""
    arr = [1, 2, 3, 4, 5]
    target = 9
    assert longest_subsequence_sum(arr, target) == 2  # [4, 5]

def test_empty_array():
    """Test empty array case"""
    assert longest_subsequence_sum([], 5) == 0

def test_no_matching_subsequence():
    """Test when no subsequence matches the target"""
    arr = [1, 2, 3, 4]
    target = 10
    assert longest_subsequence_sum(arr, target) == 0

def test_multiple_subsequences():
    """Test multiple possible subsequences"""
    arr = [1, 1, 1, 1, 1]
    target = 3
    assert longest_subsequence_sum(arr, target) == 3  # Multiple ways to get sum 3

def test_single_element_matches():
    """Test when a single element matches the target"""
    arr = [1, 2, 3, 4, 5]
    target = 3
    assert longest_subsequence_sum(arr, target) == 1

def test_negative_numbers():
    """Test with negative numbers in the array"""
    arr = [-1, 2, -3, 4, 5]
    target = 1
    assert longest_subsequence_sum(arr, target) in {2, 1}  # Can be 2 [2,-1] or 1 [1]

def test_zero_target():
    """Test with zero as the target"""
    arr = [-1, 1, 0, 2, -2]
    target = 0
    assert longest_subsequence_sum(arr, target) in {2, 1}  # Can be 2 or 1