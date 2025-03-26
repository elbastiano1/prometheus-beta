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
    
    # First, identify even and odd numbers
    odds = sorted([num for num in arr if num % 2 != 0])
    evens = sorted([num for num in arr if num % 2 == 0])
    
    # Sort even numbers by their squares in descending order
    evens_by_square = sorted(evens, key=lambda x: x**2, reverse=True)
    
    # Merge the two lists, with even numbers placed in their square-sorted positions
    result = []
    odd_index = 0
    even_index = 0
    
    # Go through the merge process
    while odd_index < len(odds) or even_index < len(evens_by_square):
        # If no more odd numbers, add remaining evens
        if odd_index >= len(odds):
            result.append(evens_by_square[even_index])
            even_index += 1
            continue
        
        # If no more even numbers, add remaining odds
        if even_index >= len(evens_by_square):
            result.append(odds[odd_index])
            odd_index += 1
            continue
        
        # Decide which to add based on maintaining ascending order
        if odds[odd_index] < evens_by_square[even_index]:
            result.append(odds[odd_index])
            odd_index += 1
        else:
            result.append(evens_by_square[even_index])
            even_index += 1
    
    return result