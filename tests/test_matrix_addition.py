import pytest
from src.matrix_addition import add_matrices

def test_basic_matrix_addition():
    """Test basic matrix addition with integer matrices"""
    matrix1 = [[1, 2], [3, 4]]
    matrix2 = [[5, 6], [7, 8]]
    expected = [[6, 8], [10, 12]]
    assert add_matrices(matrix1, matrix2) == expected

def test_matrix_addition_with_floats():
    """Test matrix addition with floating-point numbers"""
    matrix1 = [[1.5, 2.5], [3.5, 4.5]]
    matrix2 = [[0.5, 1.5], [2.5, 3.5]]
    expected = [[2.0, 4.0], [6.0, 8.0]]
    assert add_matrices(matrix1, matrix2) == expected

def test_single_element_matrices():
    """Test matrix addition with single-element matrices"""
    matrix1 = [[42]]
    matrix2 = [[58]]
    expected = [[100]]
    assert add_matrices(matrix1, matrix2) == expected

def test_incompatible_row_count():
    """Test that an error is raised for matrices with different row counts"""
    matrix1 = [[1, 2], [3, 4]]
    matrix2 = [[5, 6]]
    with pytest.raises(ValueError, match="Matrices must have the same number of rows"):
        add_matrices(matrix1, matrix2)

def test_incompatible_column_count():
    """Test that an error is raised for matrices with different column counts"""
    matrix1 = [[1, 2, 3], [4, 5, 6]]
    matrix2 = [[7, 8], [9, 10]]
    with pytest.raises(ValueError, match="Matrices must have the same number of columns"):
        add_matrices(matrix1, matrix2)

def test_empty_matrices():
    """Test that empty matrices raise an error"""
    with pytest.raises(ValueError, match="Matrices cannot be empty"):
        add_matrices([], [])

def test_non_list_input():
    """Test that non-list inputs raise a TypeError"""
    with pytest.raises(TypeError, match="Inputs must be lists"):
        add_matrices(42, [1, 2])

def test_non_list_rows():
    """Test that non-list rows raise a TypeError"""
    matrix1 = [[1, 2], 3]
    matrix2 = [[4, 5], [6, 7]]
    with pytest.raises(TypeError, match="Matrix rows must be lists"):
        add_matrices(matrix1, matrix2)