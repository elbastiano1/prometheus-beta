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
    
    # Separate odd and even numbers based on input order
    odds = [num for num in arr if num % 2 != 0]
    evens = [num for num in arr if num % 2 == 0]
    
    # Sort odds in ascending order
    odds_sorted = sorted(odds)
    
    # Sort evens by their squares in descending order
    evens_sorted = sorted(evens, key=lambda x: x**2, reverse=True)
    
    # Merge the lists
    result = []
    odd_index = 0
    even_index = 0
    
    while odd_index < len(odds_sorted) and even_index < len(evens_sorted):
        if odds_sorted[odd_index] <= evens_sorted[even_index]:
            result.append(odds_sorted[odd_index])
            odd_index += 1
        else:
            result.append(evens_sorted[even_index])
            even_index += 1
    
    # Add remaining odds
    result.extend(odds_sorted[odd_index:])
    
    # Add remaining evens (in descending square order)
    result.extend(evens_sorted[even_index:])
    
    return result