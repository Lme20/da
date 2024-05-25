"""
This function implements the binary search algorithm.

used for: 
- Searching in a sorted array

The algorithm works as follows:
1. It starts by finding the middle element of the array.
2. If the target value is equal to the middle element, it returns the index of the middle element.
3. If the target value is less than the middle element, the search continues on the left half of the array.
4. If the target value is greater than the middle element, the search continues on the right half of the array.
5. This process continues, eliminating half of the elements, and comparing the target value to the middle value of the remaining elements - until the target value is found, or until the entire array has been searched.

Parameters:
array (list): The sorted list of elements
target (int): The value to search for

Returns:
int: The index of the target if found, otherwise -1
"""

def binary_search(array, target):
    left = 0 # Initialize the left pointer
    right = len(array) - 1 # Initialize the right pointer

    # Loop until the left pointer is less than or equal to the right pointer
    while (left <= right):
        mid = (right + left) // 2 # Find the middle element

        if array[mid] == target: # Check if the middle element is the target
            return mid
        elif array[mid] < target: # If the target is greater than the middle element, search the right half
            left = mid + 1
        else:
            right = mid - 1 # If the target is less than the middle element, search the left half
    return -1   