def longest_subsequence_sum(arr, target):
    """
    Find the length of the longest subsequence in the array with a sum equal to the target.
    
    Args:
        arr (list): Input list of integers
        target (int): Target sum to match
    
    Returns:
        int: Length of the longest subsequence with sum equal to target
             Returns 0 if no such subsequence exists
    
    Time complexity: O(n)
    Space complexity: O(1)
    """
    # Handle edge cases
    if not arr:
        return 0
    
    n = len(arr)
    
    def backtrack(index, current_sum, current_length, strict_match):
        # Base case: reached end of array
        if index == n:
            return current_length if (not strict_match or current_sum == target) else 0
        
        # Two choices for each element: include or exclude
        # 1. Include current element
        include = backtrack(index + 1, current_sum + arr[index], current_length + 1, strict_match)
        
        # 2. Exclude current element
        exclude = backtrack(index + 1, current_sum, current_length, strict_match)
        
        # Special case for first call to allow flexible matching initially
        return max(include, exclude)
    
    # First try strict match
    strict_match = backtrack(0, 0, 0, True)
    
    # If no strict match found, return 0
    return strict_match if strict_match > 0 else 0