import pytest
from src.triangle_number_sequence import generate_triangle_numbers

def test_generate_triangle_numbers_standard_cases():
    """Test standard cases of triangle number generation."""
    # Check known triangle number sequences
    assert generate_triangle_numbers(0) == []
    assert generate_triangle_numbers(1) == [1]
    assert generate_triangle_numbers(5) == [1, 3, 6, 10, 15]

def test_generate_triangle_numbers_edge_cases():
    """Test edge cases for triangle number generation."""
    # Verify edge cases
    assert generate_triangle_numbers(0) == []
    assert len(generate_triangle_numbers(10)) == 10

def test_generate_triangle_numbers_error_handling():
    """Test error handling for invalid inputs."""
    # Test negative input
    with pytest.raises(ValueError, match="Number of triangle numbers must be non-negative"):
        generate_triangle_numbers(-1)
    
    # Test non-integer input
    with pytest.raises(TypeError, match="Input must be an integer"):
        generate_triangle_numbers(3.14)
    with pytest.raises(TypeError, match="Input must be an integer"):
        generate_triangle_numbers("5")

def test_generate_triangle_numbers_validation():
    """Additional validation tests for triangle number generation."""
    # Verify mathematical property of triangle numbers
    result = generate_triangle_numbers(6)
    expected = [1, 3, 6, 10, 15, 21]
    assert result == expected

    # Check large input
    large_result = generate_triangle_numbers(100)
    assert len(large_result) == 100
    assert large_result[0] == 1
    assert large_result[-1] == 5050  # 100th triangle number