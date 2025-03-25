def is_sorted(lst, ascending=True):
    """
    Check if a list is sorted in ascending or descending order.

    Args:
        lst (list): The input list to check for sorting.
        ascending (bool, optional): 
            - If True, checks for ascending order (default)
            - If False, checks for descending order

    Returns:
        bool: True if the list is sorted according to the specified order, 
              False otherwise

    Raises:
        TypeError: If the input is not a list or contains elements of different types
        ValueError: If the list contains elements that cannot be compared

    Examples:
        >>> is_sorted([1, 2, 3, 4])
        True
        >>> is_sorted([4, 3, 2, 1], ascending=False)
        True
        >>> is_sorted([])
        True
        >>> is_sorted([1])
        True
    """
    # Handle empty or single-element lists (always considered sorted)
    if len(lst) <= 1:
        return True

    # Validate input type
    if not isinstance(lst, list):
        raise TypeError("Input must be a list")

    # Determine comparison function based on ascending parameter
    if ascending:
        # Check if list is in ascending order
        for i in range(1, len(lst)):
            try:
                if lst[i] < lst[i-1]:
                    return False
            except TypeError:
                raise TypeError("List contains incomparable elements")
    else:
        # Check if list is in descending order
        for i in range(1, len(lst)):
            try:
                if lst[i] > lst[i-1]:
                    return False
            except TypeError:
                raise TypeError("List contains incomparable elements")

    return True