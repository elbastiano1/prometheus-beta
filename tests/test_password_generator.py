import pytest
import string
from src.password_generator import generate_password

def test_generate_password_length():
    """Test that password generation returns correct length."""
    lengths = [1, 5, 10, 20, 50]
    for length in lengths:
        password = generate_password(length)
        assert len(password) == length

def test_generate_password_complexity():
    """Test that generated password contains characters from different sets."""
    password = generate_password(20)
    
    # Check that password contains at least one character from each set
    assert any(c in string.ascii_lowercase for c in password)
    assert any(c in string.ascii_uppercase for c in password)
    assert any(c in string.digits for c in password)
    assert any(c in string.punctuation for c in password)

def test_generate_password_randomness():
    """Test that multiple password generations are different."""
    password1 = generate_password(10)
    password2 = generate_password(10)
    assert password1 != password2

def test_generate_password_invalid_length():
    """Test that invalid length raises a ValueError."""
    with pytest.raises(ValueError, match="Password length must be at least 1 character"):
        generate_password(0)
    
    with pytest.raises(ValueError, match="Password length must be at least 1 character"):
        generate_password(-5)

def test_generate_password_types():
    """Test that function handles different input types."""
    # While the implementation uses int, these tests show robustness
    with pytest.raises(TypeError):
        generate_password("10")
    
    with pytest.raises(TypeError):
        generate_password(None)