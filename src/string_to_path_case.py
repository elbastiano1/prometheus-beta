import re

def string_to_path_case(input_string):
    """
    Convert a given string to path case (lowercase with hyphens).
    
    Args:
        input_string (str): The input string to convert.
    
    Returns:
        str: The input string converted to path case.
    
    Raises:
        TypeError: If input is not a string.
        ValueError: If input string is empty.
    
    Examples:
        >>> string_to_path_case("HelloWorld")
        'hello-world'
        >>> string_to_path_case("snake_case_string")
        'snake-case-string'
        >>> string_to_path_case("Mixed Case String")
        'mixed-case-string'
    """
    # Check input type
    if not isinstance(input_string, str):
        raise TypeError("Input must be a string")
    
    # Check for empty string
    if not input_string:
        raise ValueError("Input string cannot be empty")
    
    # Step 1: Replace underscores with hyphens
    input_string = input_string.replace('_', '-')
    
    # Step 2: Insert hyphen before capital letters 
    # and convert to lowercase using regex
    path_case = re.sub(r'([a-z0-9])([A-Z])', r'\1-\2', input_string)
    
    # Convert to lowercase
    path_case = path_case.lower()
    
    # Remove multiple consecutive hyphens
    path_case = re.sub(r'-+', '-', path_case)
    
    # Remove leading/trailing hyphens
    path_case = path_case.strip('-')
    
    return path_case