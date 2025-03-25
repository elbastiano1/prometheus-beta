def run_length_encode(data):
    """
    Perform Run-Length Encoding on the input data.
    
    Args:
        data (str or list): The input sequence to be encoded.
    
    Returns:
        str: The run-length encoded representation of the input.
    
    Raises:
        TypeError: If input is not a string or list.
        ValueError: If input is an empty sequence.
    
    Examples:
        >>> run_length_encode("AABBBCCCC")
        '2A3B4C'
        >>> run_length_encode([1,1,2,3,3,3])
        '2-1 1-2 3-3'
    """
    # Validate input
    if not data:
        raise ValueError("Input cannot be empty")
    
    if not isinstance(data, (str, list)):
        raise TypeError("Input must be a string or list")
    
    # Handle lists and strings slightly differently
    if isinstance(data, list):
        return _encode_list(data)
    
    return _encode_string(data)

def _encode_string(s):
    """Encode a string using Run-Length Encoding."""
    if not s:
        return ''
    
    encoded = []
    current_char = s[0]
    count = 1
    
    for char in s[1:]:
        if char == current_char:
            count += 1
        else:
            # Only include count if > 1
            encoded.append(str(count) + current_char if count > 1 else current_char)
            current_char = char
            count = 1
    
    # Handle the last group
    encoded.append(str(count) + current_char if count > 1 else current_char)
    
    return ''.join(encoded)

def _encode_list(lst):
    """Encode a list using Run-Length Encoding."""
    if not lst:
        return ''
    
    encoded = []
    current_item = lst[0]
    count = 1
    
    for item in lst[1:]:
        if item == current_item:
            count += 1
        else:
            # Always include count for lists
            encoded.append(f'{count}-{current_item}')
            current_item = item
            count = 1
    
    # Handle the last group
    encoded.append(f'{count}-{current_item}')
    
    return ' '.join(encoded)

def run_length_decode(encoded):
    """
    Decode a Run-Length Encoded string or representation.
    
    Args:
        encoded (str): The encoded string to decode.
    
    Returns:
        str or list: The decoded sequence.
    
    Raises:
        ValueError: If the encoded string is invalid.
    
    Examples:
        >>> run_length_decode('2A3B4C')
        'AABBBCCCC'
        >>> run_length_decode('2-1 1-2 3-3')
        [1, 1, 2, 3, 3, 3]
    """
    # Validate input
    if not encoded:
        raise ValueError("Input cannot be empty")
    
    # Check if it looks like a list-style encoding
    if '-' in encoded:
        return _decode_list(encoded)
    
    return _decode_string(encoded)

def _decode_string(s):
    """Decode a string-style Run-Length Encoded string."""
    decoded = []
    i = 0
    
    while i < len(s):
        # Check if current character is a digit
        if s[i].isdigit():
            # Find the full number
            j = i
            while j < len(s) and s[j].isdigit():
                j += 1
            
            # Convert number and get character
            count = int(s[i:j])
            char = s[j]
            decoded.extend([char] * count)
            
            # Move index
            i = j + 1
        else:
            # No number, just one character
            decoded.append(s[i])
            i += 1
    
    return ''.join(decoded)

def _decode_list(s):
    """Decode a list-style Run-Length Encoded string."""
    decoded = []
    
    # Split into individual group encodings
    groups = s.split()
    
    for group in groups:
        # Split each group into count and item
        count, item = group.split('-')
        
        # Convert count to int and create list of items
        decoded.extend([type(eval(item))(item)] * int(count))
    
    return decoded