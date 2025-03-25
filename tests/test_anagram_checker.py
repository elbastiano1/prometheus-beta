import pytest
from src.anagram_checker import anagram_checker

def test_basic_anagrams():
    """Test basic anagram scenarios"""
    assert anagram_checker("listen", "silent") == True
    assert anagram_checker("triangle", "integral") == True
    assert anagram_checker("debit card", "bad credit") == True

def test_non_anagrams():
    """Test words that are not anagrams"""
    assert anagram_checker("hello", "world") == False
    assert anagram_checker("python", "java") == False
    assert anagram_checker("cat", "dog") == False

def test_case_insensitive():
    """Test that anagram checking is case-insensitive"""
    assert anagram_checker("Tea", "Eat") == True
    assert anagram_checker("LISTEN", "silent") == True

def test_whitespace_handling():
    """Test handling of whitespace in inputs"""
    assert anagram_checker("debit card", "bad credit") == True
    assert anagram_checker(" listen ", "silent") == True

def test_edge_cases():
    """Test edge cases"""
    assert anagram_checker("", "") == True  # Empty strings
    assert anagram_checker("a", "a") == True  # Single character
    assert anagram_checker("a", "b") == False

def test_error_handling():
    """Test error handling for invalid inputs"""
    with pytest.raises(TypeError):
        anagram_checker(123, "test")
    with pytest.raises(TypeError):
        anagram_checker("test", None)
    with pytest.raises(TypeError):
        anagram_checker(["list"], "test")