def find_missing_number(nums):
    """
    Find the missing number in a sequence of integers from 1 to n.
    
    Args:
        nums (list): A list of unique integers from 1 to n, with one number missing.
    
    Returns:
        int: The missing number in the sequence.
    
    Raises:
        ValueError: If the input list is empty or contains duplicate numbers.
    """
    # Check for invalid input
    if not nums:
        raise ValueError("Input list cannot be empty")
    
    # Check for duplicates
    if len(nums) != len(set(nums)):
        raise ValueError("Input list must contain unique numbers")
    
    # Calculate the expected sum of numbers from 1 to n
    n = len(nums) + 1  # Total expected length with the missing number
    expected_sum = (n * (n + 1)) // 2
    
    # Calculate the actual sum of the given numbers
    actual_sum = sum(nums)
    
    # The difference is the missing number
    return expected_sum - actual_sum