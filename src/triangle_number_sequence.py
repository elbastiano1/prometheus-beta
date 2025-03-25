def generate_triangle_numbers(n):
    """
    Generate the first n numbers in the Triangle Number Sequence.

    A triangle number is a number that can be represented as a triangular grid of points 
    where the first line contains a single element and each subsequent line contains 
    one more element than the previous line.

    The sequence is: 1, 3, 6, 10, 15, 21, ...
    Mathematically defined as: T(n) = n * (n + 1) // 2

    Args:
        n (int): The number of triangle numbers to generate.

    Returns:
        list: A list of the first n triangle numbers.

    Raises:
        ValueError: If n is negative.
        TypeError: If n is not an integer.
    """
    # Input validation
    if not isinstance(n, int):
        raise TypeError("Input must be an integer")
    
    if n < 0:
        raise ValueError("Number of triangle numbers must be non-negative")
    
    # Generate triangle numbers
    return [i * (i + 1) // 2 for i in range(1, n + 1)]