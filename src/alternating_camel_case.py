def to_alternating_camel_case(s: str) -> str:
    """
    Convert a string to alternating camel case.
    
    Args:
        s (str): The input string to convert.
    
    Returns:
        str: The string converted to alternating camel case.
    
    Raises:
        TypeError: If input is not a string.
    
    Examples:
        >>> to_alternating_camel_case("hello world")
        'hElLoWoRlD'
        >>> to_alternating_camel_case("python is awesome")
        'pYtHoNiSaWeSoMe'
        >>> to_alternating_camel_case("")
        ''
    """
    # Check for invalid input
    if not isinstance(s, str):
        raise TypeError("Input must be a string")
    
    # Handle empty string case
    if not s:
        return ""
    
    # Convert to alternating case
    result = []
    for i, char in enumerate(s.replace(' ', '')):
        if i % 2 == 0:
            result.append(char.lower())
        else:
            result.append(char.upper())
    
    return ''.join(result)