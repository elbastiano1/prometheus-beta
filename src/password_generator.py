import secrets
import string

def generate_password(length: int) -> str:
    """
    Generate a secure random password of specified length.

    Args:
        length (int): The desired length of the password.
        
    Returns:
        str: A randomly generated password.
        
    Raises:
        ValueError: If the length is less than 1.
    """
    # Validate input
    if length < 1:
        raise ValueError("Password length must be at least 1 character")
    
    # Define character sets
    characters = string.ascii_letters + string.digits + string.punctuation
    
    # Generate password using cryptographically secure random selection
    password = ''.join(secrets.choice(characters) for _ in range(length))
    
    return password