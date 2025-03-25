def strand_sort(arr):
    """
    Implement the strand sort algorithm to sort a list in ascending order.
    
    Strand sort works by repeatedly extracting sorted sublists from the input 
    and merging them into a final sorted list.
    
    Args:
        arr (list): The input list to be sorted.
    
    Returns:
        list: A new sorted list.
    
    Raises:
        TypeError: If the input is not a list or contains non-comparable elements.
    """
    # Handle edge cases
    if not isinstance(arr, list):
        raise TypeError("Input must be a list")
    
    # Handle empty or single-element list
    if len(arr) <= 1:
        return arr.copy()
    
    # Create a working copy of the input list
    unsorted = arr.copy()
    result = []
    
    while unsorted:
        # Extract the first element as the start of a sublist
        sublist = [unsorted.pop(0)]
        
        # Iterate through the remaining unsorted elements
        i = 0
        while i < len(unsorted):
            # If current element is greater than the last element in sublist, 
            # add it to the sublist and remove from unsorted
            if unsorted[i] >= sublist[-1]:
                sublist.append(unsorted.pop(i))
            else:
                i += 1
        
        # Merge the extracted sublist with the result
        result = merge(result, sublist)
    
    return result

def merge(list1, list2):
    """
    Merge two sorted lists into a single sorted list.
    
    Args:
        list1 (list): First sorted list.
        list2 (list): Second sorted list.
    
    Returns:
        list: A new merged and sorted list.
    """
    merged = []
    i, j = 0, 0
    
    # Compare and merge elements from both lists
    while i < len(list1) and j < len(list2):
        if list1[i] <= list2[j]:
            merged.append(list1[i])
            i += 1
        else:
            merged.append(list2[j])
            j += 1
    
    # Add remaining elements from list1, if any
    merged.extend(list1[i:])
    
    # Add remaining elements from list2, if any
    merged.extend(list2[j:])
    
    return merged