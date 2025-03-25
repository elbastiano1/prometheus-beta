import pytest
from src.run_length_encoding import run_length_encode, run_length_decode

def test_run_length_encode_string_basic():
    """Test basic string encoding."""
    assert run_length_encode("AABBBCCCC") == '2A3B4C'
    assert run_length_encode("WWWWWWWWWWWWBWWWWWWWWWWWWBBBWWWWWWWWWWWWWWWWWWB") == '12W1B12W3B24W1B'

def test_run_length_encode_string_single_chars():
    """Test encoding with single characters."""
    assert run_length_encode("ABCD") == 'A1B1C1D'

def test_run_length_encode_list_basic():
    """Test basic list encoding."""
    assert run_length_encode([1,1,2,3,3,3]) == '2-1 1-2 3-3'
    assert run_length_encode(['a','a','b','c','c','c']) == '2-a 1-b 3-c'

def test_run_length_decode_string():
    """Test decoding of string-style encoding."""
    assert run_length_decode('2A3B4C') == 'AABBBCCCC'
    assert run_length_decode('12W1B12W3B24W1B') == 'WWWWWWWWWWWWBWWWWWWWWWWWWBBBWWWWWWWWWWWWWWWWWWB'

def test_run_length_decode_list():
    """Test decoding of list-style encoding."""
    assert run_length_decode('2-1 1-2 3-3') == [1,1,2,3,3,3]
    assert run_length_decode('2-a 1-b 3-c') == ['a','a','b','c','c','c']

def test_round_trip_encoding():
    """Test round-trip encoding and decoding."""
    test_strings = [
        "AABBBCCCC",
        "WWWWWWWWWWWWBWWWWWWWWWWWWBBBWWWWWWWWWWWWWWWWWWB",
        "ABCDEFG"
    ]
    
    test_lists = [
        [1,1,2,3,3,3],
        ['a','a','b','c','c','c'],
        [1,2,3,4,5]
    ]
    
    for s in test_strings:
        assert run_length_decode(run_length_encode(s)) == s
    
    for lst in test_lists:
        assert run_length_decode(run_length_encode(lst)) == lst

def test_error_handling():
    """Test error cases."""
    with pytest.raises(ValueError, match="Input cannot be empty"):
        run_length_encode("")
    
    with pytest.raises(ValueError, match="Input cannot be empty"):
        run_length_decode("")
    
    with pytest.raises(TypeError):
        run_length_encode(123)
    
    with pytest.raises(ValueError):
        run_length_decode("invalid-encoding")

def test_edge_cases():
    """Test edge cases for encoding and decoding."""
    # Single character
    assert run_length_encode("A") == 'A'
    assert run_length_decode('A') == 'A'
    
    # Repeated single character
    assert run_length_encode("AAAAA") == '5A'
    assert run_length_decode('5A') == 'AAAAA'
    
    # Mixed types in list
    mixed_list = [1, 1, 'a', 'a', 'a']
    encoded = run_length_encode(mixed_list)
    assert encoded == '2-1 2-a 3-a'
    assert run_length_decode(encoded) == mixed_list