# DYNAMIC ARRAYS

- An array with a resizable capacity
- Random access of elements O(1)
- Easy to delete/insert at the end
- Shifting elements in O(N)
- Expanding/shrinking the array is O(N)

## STEPS

1. Specify the initial capacity
Insertion: Insert elements at the end
    - If the array is full, double the capacity
Deletion: Remove elements from the end. 
    - If the number of elements is smaller than capacity, shrink capacity (optional)
Accessing: Access elements by their index (constant time)
Searching: Search for elements using linear or binary search

## OPERATIONS
### ACCESSING
constant time: O(1)

### INSERTION
linear time: O(N)

### DELETION
linear time: O(N)

### SEARCHING
Depends on the type of search that is performed.
- **Linear Search**: O(N)
- **Binary Search (if sorted)**: O(log N)