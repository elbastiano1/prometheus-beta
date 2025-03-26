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
    
    # Sort the input array first
    sorted_full = sorted(arr)
    
    # Separate indices of even and odd numbers
    even_indices = [i for i, x in enumerate(sorted_full) if x % 2 == 0]
    odd_indices = [i for i, x in enumerate(sorted_full) if x % 2 != 0]
    
    # Sort even numbers by their squares in descending order
    even_squares_sorted = sorted(
        [sorted_full[i] for i in even_indices], 
        key=lambda x: x**2, 
        reverse=True
    )
    
    # Reconstruct the final list
    result = sorted_full.copy()
    
    # Replace even numbers at original indices with square-sorted values
    for i, even_index in enumerate(even_indices):
        result[even_index] = even_squares_sorted[i]
    
    return result