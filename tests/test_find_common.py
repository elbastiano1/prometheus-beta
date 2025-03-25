import pytest
from src.find_common import find_common

def test_find_common_basic():
    """Test basic functionality of finding common elements"""
    assert set(find_common([1, 2, 3], [3, 4, 5])) == {3}
    assert set(find_common(['a', 'b', 'c'], ['b', 'c', 'd'])) == {'b', 'c'}

def test_find_common_empty_lists():
    """Test behavior with empty lists"""
    assert find_common([], [1, 2, 3]) == []
    assert find_common([1, 2, 3], []) == []
    assert find_common([], []) == []

def test_find_common_no_overlap():
    """Test when there are no common elements"""
    assert find_common([1, 2, 3], [4, 5, 6]) == []

def test_find_common_duplicates():
    """Test handling of duplicate elements"""
    assert set(find_common([1, 1, 2, 2], [2, 2, 3, 3])) == {2}

def test_find_common_type_mix():
    """Test finding common elements with mixed types"""
    assert set(find_common([1, 'a', 2], [2, 'a', 3])) == {2, 'a'}

def test_find_common_object_types():
    """Test finding common elements with unhashable types"""
    list1 = [[1, 2], [3, 4]]
    list2 = [[3, 4], [5, 6]]
    with pytest.raises(TypeError):
        find_common(list1, list2)