import pytest
from src.longest_palindromic_substring import longest_palindromic_substring

def test_basic_palindromes():
    """Test basic palindromic substrings"""
    assert longest_palindromic_substring("babad") in ["bab", "aba"]
    assert longest_palindromic_substring("cbbd") == "bb"

def test_full_string_palindrome():
    """Test when entire string is a palindrome"""
    assert longest_palindromic_substring("racecar") == "racecar"
    assert longest_palindromic_substring("level") == "level"

def test_empty_string():
    """Test empty string"""
    assert longest_palindromic_substring("") == ""

def test_single_character():
    """Test single character strings"""
    assert longest_palindromic_substring("a") == "a"
    assert longest_palindromic_substring("z") == "z"

def test_no_palindrome():
    """Test string with no palindrome longer than single character"""
    assert longest_palindromic_substring("abcd") in ["a", "b", "c", "d"]

def test_multiple_palindromes():
    """Test string with multiple palindromes of same length"""
    result = longest_palindromic_substring("abaxyzzyxf")
    assert result in ["xyzzyx", "xyzyx"]

def test_complex_cases():
    """Test more complex palindrome scenarios"""
    test_cases = [
        "abcdefgfedcba",  # Even length palindrome
        "forgeeksskeegfor",  # Complex case
        "aacabdkacaa"  # Multiple palindrome possibilities
    ]
    
    expected_results = [
        "abcdefgfedcba",
        "geeksskeeg",
        "aca"
    ]
    
    for test_input, expected in zip(test_cases, expected_results):
        assert longest_palindromic_substring(test_input) == expected