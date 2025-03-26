def sort_array_with_even_squares(arr):
    """
    Sort an array in ascending order, with even number squares sorted in descending order.
    
    Args:
        arr (list): Input list of numbers
    
    Returns:
        list: Sorted array with even number squares processed 
    
    Raises:
        TypeError: If input is not a list
    """
    # Validate input
    if not isinstance(arr, list):
        raise TypeError("Input must be a list")
    
    # Handle empty list case
    if not arr:
        return []
    
    # Sort the entire array in ascending order first
    sorted_arr = sorted(arr)
    
    # Identify even numbers and their squares
    even_squares = [(num, num**2) for num in sorted_arr if num % 2 == 0]
    
    # Sort the even squares by their squared value in descending order
    even_squares_sorted = sorted(even_squares, key=lambda x: x[1], reverse=True)
    
    # Reconstruct the final array
    result = []
    even_square_index = 0
    
    for num in sorted_arr:
        if num % 2 == 0:
            # Replace even numbers with their descending sorted squares
            result.append(even_squares_sorted[even_square_index][0])
            even_square_index += 1
        else:
            # Keep odd numbers in their original ascending order
            result.append(num)
    
    return result