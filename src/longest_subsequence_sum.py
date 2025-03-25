def longest_subsequence_sum(arr, target):
    """
    Find the length of the longest subsequence in the array with a sum equal to the target.
    
    Args:
        arr (list): Input list of integers
        target (int): Target sum to match
    
    Returns:
        int: Length of the longest subsequence with sum equal to target
             Returns 0 if no such subsequence exists
    
    Time complexity: O(n * abs(target))
    Space complexity: O(n * abs(target))
    """
    # Handle edge cases
    if not arr:
        return 0
    
    n = len(arr)
    # Use wider range to handle negative numbers
    total_min = min(0, min(arr) * n)
    total_max = max(0, max(arr) * n)
    
    # Shift target to handle both positive and negative sums
    shifted_target = target - total_min
    range_size = total_max - total_min + 1
    
    # Initialize dp with a larger range
    dp = [[0] * range_size for _ in range(n + 1)]
    
    # Mark initial state
    dp[0][0] = 0
    
    # Iterate through array elements
    for i in range(1, n + 1):
        for j in range(range_size):
            # Try excluding current element
            dp[i][j] = dp[i-1][j]
            
            # Compute shifted index for current element
            curr_val_shifted = arr[i-1] - total_min
            
            # Try including current element if possible
            if 0 <= j - curr_val_shifted < range_size:
                include_sum = dp[i-1][j - curr_val_shifted] + 1
                dp[i][j] = max(dp[i][j], include_sum)
    
    # Find the length of the longest subsequence
    # Check the column corresponding to the shifted target
    max_length = 0
    for i in range(1, n + 1):
        shifted_col = shifted_target
        max_length = max(max_length, dp[i][shifted_col])
    
    return max_length