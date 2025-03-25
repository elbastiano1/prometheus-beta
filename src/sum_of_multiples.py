def sum_of_multiples(limit, multiples):
    """
    Calculate the sum of all multiples of given numbers up to a limit.

    Args:
        limit (int): The maximum value to consider for multiples (exclusive).
        multiples (list): A list of positive integers to find multiples of.

    Returns:
        int: The sum of all unique multiples of the given numbers up to the limit.

    Raises:
        ValueError: If limit or any number in multiples is less than or equal to 0.
    """
    # Validate input
    if limit <= 0:
        raise ValueError("Limit must be a positive integer")
    
    # Check if any multiple is non-positive
    if any(multiple <= 0 for multiple in multiples):
        raise ValueError("All multiples must be positive integers")
    
    # Special case for empty multiples list
    if not multiples:
        return 0
    
    # Use a set to track unique multiples to avoid double-counting
    unique_multiples = set()
    
    # Find all unique multiples for each number in the multiples list
    for multiple in multiples:
        # Generate multiples of this number up to (but not exceeding) the limit
        current_multiple = multiple
        while current_multiple < limit:
            unique_multiples.add(current_multiple)
            current_multiple += multiple
    
    # Return the sum of unique multiples
    return sum(unique_multiples)