def sort_unique_chars(input_string: str) -> list:
    """
    Takes a string and returns a sorted list of unique characters in case-sensitive alphabetical order.

    Args:
        input_string (str): The input string to process.

    Returns:
        list: A sorted list of unique characters from the input string.

    Examples:
        >>> sort_unique_chars("hello")
        ['e', 'h', 'l', 'o']
        >>> sort_unique_chars("Hello")
        ['H', 'e', 'l', 'o']
        >>> sort_unique_chars("")
        []
    """
    # Check if input is a string
    if not isinstance(input_string, str):
        raise TypeError("Input must be a string")
    
    # Remove duplicates and sort characters
    unique_chars = sorted(set(input_string))
    
    return unique_chars