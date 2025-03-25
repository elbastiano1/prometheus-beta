def add_matrices(matrix1, matrix2):
    """
    Add two matrices element-wise, with error checking for compatibility.
    
    Args:
        matrix1 (List[List[int/float]]): First input matrix
        matrix2 (List[List[int/float]]): Second input matrix
    
    Returns:
        List[List[int/float]]: A new matrix with element-wise addition
    
    Raises:
        ValueError: If matrices have incompatible dimensions
        TypeError: If input is not a valid matrix (list of lists)
    """
    # Validate input types
    if not (isinstance(matrix1, list) and isinstance(matrix2, list)):
        raise TypeError("Inputs must be lists")
    
    # Check if matrices are empty
    if not matrix1 or not matrix2:
        raise ValueError("Matrices cannot be empty")
    
    # Check row count compatibility
    if len(matrix1) != len(matrix2):
        raise ValueError("Matrices must have the same number of rows")
    
    # Validate each row
    for row1, row2 in zip(matrix1, matrix2):
        # Ensure each row is a list
        if not (isinstance(row1, list) and isinstance(row2, list)):
            raise TypeError("Matrix rows must be lists")
        
        # Check column count compatibility
        if len(row1) != len(row2):
            raise ValueError("Matrices must have the same number of columns")
    
    # Perform matrix addition
    return [
        [row1[col] + row2[col] for col in range(len(row1))]
        for row1, row2 in zip(matrix1, matrix2)
    ]