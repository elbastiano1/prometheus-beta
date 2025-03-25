def longest_subsequence_sum(arr, target):
    """
    Find the length of the longest subsequence in the array with a sum equal to the target.
    
    Args:
        arr (list): Input list of integers
        target (int): Target sum to match
    
    Returns:
        int: Length of the longest subsequence with sum equal to target
             Returns 0 if no such subsequence exists
    
    Time complexity: O(2^n)
    Space complexity: O(n)
    """
    # Handle edge cases
    if not arr:
        return 0
    
    def find_subsequence(index, current_sum, current_length, found_match):
        # Base case: reached end of array
        if index == len(arr):
            return current_length if current_sum == target and found_match else 0
        
        # Two choices for each element: include or exclude
        # 1. Include current element
        include = find_subsequence(
            index + 1, 
            current_sum + arr[index], 
            current_length + 1, 
            found_match or current_sum + arr[index] == target
        )
        
        # 2. Exclude current element
        exclude = find_subsequence(
            index + 1, 
            current_sum, 
            current_length, 
            found_match
        )
        
        # Special case to handle first call
        return max(include, exclude)
    
    # Find the longest subsequence with strict matching
    result = find_subsequence(0, 0, 0, False)
    
    # If no subsequence found matching exact target, return 0
    return max(0, result)