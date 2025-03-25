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
    
    def backtrack(index, current_sum, current_length):
        # Base case: reached end of array
        if index == len(arr):
            return current_length if current_sum == target else 0
        
        # Two choices for each element: include or exclude
        # 1. Include current element
        include = backtrack(index + 1, current_sum + arr[index], current_length + 1)
        
        # 2. Exclude current element
        exclude = backtrack(index + 1, current_sum, current_length)
        
        # Return the max length
        return max(include, exclude)
    
    # Start backtracking from the first element
    return backtrack(0, 0, 0)