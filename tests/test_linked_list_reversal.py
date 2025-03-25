import pytest
from src.linked_list_reversal import ListNode, reverse_linked_list

def list_to_array(head):
    """Convert a linked list to an array for easy comparison."""
    result = []
    current = head
    while current:
        result.append(current.val)
        current = current.next
    return result

def array_to_list(arr):
    """Convert an array to a linked list."""
    if not arr:
        return None
    head = ListNode(arr[0])
    current = head
    for val in arr[1:]:
        current.next = ListNode(val)
        current = current.next
    return head

def test_reverse_empty_list():
    """Test reversing an empty list."""
    assert reverse_linked_list(None) is None

def test_reverse_single_node_list():
    """Test reversing a list with a single node."""
    node = ListNode(42)
    reversed_list = reverse_linked_list(node)
    assert list_to_array(reversed_list) == [42]

def test_reverse_multiple_node_list():
    """Test reversing a list with multiple nodes."""
    # Original list: 1 -> 2 -> 3 -> 4 -> 5
    original_list = array_to_list([1, 2, 3, 4, 5])
    reversed_list = reverse_linked_list(original_list)
    assert list_to_array(reversed_list) == [5, 4, 3, 2, 1]

def test_reverse_two_node_list():
    """Test reversing a list with two nodes."""
    original_list = array_to_list([10, 20])
    reversed_list = reverse_linked_list(original_list)
    assert list_to_array(reversed_list) == [20, 10]

def test_invalid_input_type():
    """Test that an error is raised for invalid input types."""
    with pytest.raises(TypeError):
        reverse_linked_list([1, 2, 3])  # List instead of ListNode
    
    with pytest.raises(TypeError):
        reverse_linked_list("not a list")  # String instead of ListNode

def test_multiple_reversals():
    """Ensure multiple reversals work correctly."""
    original_list = array_to_list([1, 2, 3, 4, 5])
    
    # First reversal
    reversed_list = reverse_linked_list(original_list)
    assert list_to_array(reversed_list) == [5, 4, 3, 2, 1]
    
    # Second reversal
    back_to_original = reverse_linked_list(reversed_list)
    assert list_to_array(back_to_original) == [1, 2, 3, 4, 5]