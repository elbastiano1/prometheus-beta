def longest_palindromic_substring(s: str) -> str:
    """
    Find the longest palindromic substring in a given string.
    
    A palindrome is a string that reads the same backward as forward.
    If multiple palindromic substrings exist with the same maximum length, 
    return the first one encountered.
    
    Args:
        s (str): Input string to search for palindromic substrings
    
    Returns:
        str: The longest palindromic substring
    
    Examples:
        >>> longest_palindromic_substring("babad")
        'bab'
        >>> longest_palindromic_substring("cbbd")
        'bb'
        >>> longest_palindromic_substring("")
        ''
    """
    # Handle edge cases
    if not s:
        return ""
    
    # Function to expand around center
    def expand_around_center(left: int, right: int) -> str:
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return s[left + 1:right]
    
    # Initialize longest palindrome
    longest = ""
    
    # Try every possible center
    for i in range(len(s)):
        # Odd length palindromes
        odd = expand_around_center(i, i)
        # Even length palindromes
        even = expand_around_center(i, i + 1)
        
        # Update longest if needed
        if len(odd) > len(longest):
            longest = odd
        if len(even) > len(longest):
            longest = even
    
    return longest