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
    
    # Separate even and odd numbers
    odds = sorted([num for num in arr if num % 2 != 0])
    evens = sorted([num for num in arr if num % 2 == 0])
    
    # Sort even numbers by their squares in descending order
    evens_by_square = sorted(evens, key=lambda x: x**2, reverse=True)
    
    # Merge the two lists while maintaining overall ascending order
    def merge_arrays(odds, evens):
        merged = []
        i, j = 0, 0
        
        while i < len(odds) and j < len(evens):
            if odds[i] < evens[j]:
                merged.append(odds[i])
                i += 1
            else:
                merged.append(evens[j])
                j += 1
        
        # Add remaining elements
        merged.extend(odds[i:])
        merged.extend(evens[j:])
        
        return merged
    
    # Merge with custom even number order
    return merge_arrays(odds, evens_by_square)