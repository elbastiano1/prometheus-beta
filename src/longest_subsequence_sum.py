def longest_subsequence_sum(arr, target):
    """
    Find the length of the longest subsequence in the array with a sum equal to the target.
    
    Args:
        arr (list): Input list of integers
        target (int): Target sum to match
    
    Returns:
        int: Length of the longest subsequence with sum equal to target
             Returns 0 if no such subsequence exists
    
    Time complexity: O(n * target)
    Space complexity: O(n * target)
    """
    # Handle edge cases
    if not arr:
        return 0
    
    n = len(arr)
    # dp[i][j] represents the length of the longest subsequence with sum j using first i elements
    dp = [[0] * (target + 1) for _ in range(n + 1)]
    
    # Iterate through array elements
    for i in range(1, n + 1):
        for j in range(target + 1):
            # If current element can be included
            if arr[i-1] <= j:
                # Max of including and excluding current element
                dp[i][j] = max(
                    dp[i-1][j],  # exclude current element
                    dp[i-1][j - arr[i-1]] + 1  # include current element
                )
            else:
                # Cannot include, just copy previous row's value
                dp[i][j] = dp[i-1][j]
    
    # The last cell gives the length of the longest subsequence
    return dp[n][target]