def anagram_checker(word1: str, word2: str) -> bool:
    """
    Check if two words are anagrams of each other.
    
    An anagram is a word or phrase formed by rearranging the letters of another word,
    using all the original letters exactly once.
    
    Args:
        word1 (str): The first word to compare
        word2 (str): The second word to compare
    
    Returns:
        bool: True if the words are anagrams, False otherwise
    
    Examples:
        >>> anagram_checker("listen", "silent")
        True
        >>> anagram_checker("hello", "world")
        False
    """
    # Validate input
    if not isinstance(word1, str) or not isinstance(word2, str):
        raise TypeError("Both inputs must be strings")
    
    # Convert to lowercase and remove any whitespace
    word1 = word1.lower().replace(" ", "")
    word2 = word2.lower().replace(" ", "")
    
    # Check if lengths are different
    if len(word1) != len(word2):
        return False
    
    # Create character frequency dictionaries
    char_count1 = {}
    char_count2 = {}
    
    # Count character frequencies
    for char in word1:
        char_count1[char] = char_count1.get(char, 0) + 1
    
    for char in word2:
        char_count2[char] = char_count2.get(char, 0) + 1
    
    # Compare character frequencies
    return char_count1 == char_count2