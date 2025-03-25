import pytest
from src.sum_of_multiples import sum_of_multiples

def test_basic_multiple():
    """Test sum of multiples with a simple case."""
    assert sum_of_multiples(10, [3, 5]) == 23  # 3 + 5 + 6 + 9 + 10

def test_single_multiple():
    """Test sum of multiples with a single number."""
    assert sum_of_multiples(15, [3]) == 18  # 3 + 6 + 9 + 12 + 15

def test_no_multiples():
    """Test sum of multiples when no multiples are found."""
    assert sum_of_multiples(2, [7]) == 0

def test_duplicate_multiples():
    """Test that duplicate multiples are counted only once."""
    assert sum_of_multiples(20, [3, 5]) == 78  # Only unique multiples

def test_invalid_limit():
    """Test that a non-positive limit raises a ValueError."""
    with pytest.raises(ValueError, match="Limit must be a positive integer"):
        sum_of_multiples(0, [3, 5])
    with pytest.raises(ValueError, match="Limit must be a positive integer"):
        sum_of_multiples(-5, [3, 5])

def test_invalid_multiples():
    """Test that non-positive multiples raise a ValueError."""
    with pytest.raises(ValueError, match="All multiples must be positive integers"):
        sum_of_multiples(10, [0, 5])
    with pytest.raises(ValueError, match="All multiples must be positive integers"):
        sum_of_multiples(10, [3, -5])

def test_large_limit():
    """Test with a larger limit to ensure performance and accuracy."""
    assert sum_of_multiples(1000, [3, 5]) == 234168

def test_empty_multiples():
    """Test with an empty list of multiples."""
    assert sum_of_multiples(10, []) == 0