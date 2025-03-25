class ListNode:
    """
    A class representing a node in a singly linked list.
    
    Attributes:
        val (any): The value stored in the node
        next (ListNode, optional): Reference to the next node in the list
    """
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverse_linked_list(head):
    """
    Reverses a linked list in-place and returns the new head.
    
    Args:
        head (ListNode): The head of the input linked list
    
    Returns:
        ListNode: The head of the reversed linked list
    
    Time Complexity: O(n)
    Space Complexity: O(1)
    
    Raises:
        TypeError: If the input is not a ListNode or None
    """
    # Handle edge cases
    if head is None:
        return None
    
    if not isinstance(head, ListNode):
        raise TypeError("Input must be a ListNode or None")
    
    # Iterative in-place reversal
    prev = None
    current = head
    
    while current is not None:
        # Store the next node before changing links
        next_node = current.next
        
        # Reverse the link
        current.next = prev
        
        # Move pointers forward
        prev = current
        current = next_node
    
    # Return the new head (last node becomes first)
    return prev