# STATIC ARRAYS

- Fixed in size
- Can't have mixed types
- Provides random access to elements
- Suitable for applications where fast element retrieval is required
- Space complexity: O(n)

## STEPS
1.

## OPERATIONS
### ACCESSING
Example: array[i] gives you the element at index 'i'.

Time complexity:
- Accessing an element by index: O(1)

### INSERTION
Inserting at the beginning or middle requires shifting elements to the right. 

Time complexity:
- Insertion at the end: O(1)
- Insertion at the beginning or middle: O(n)

### DELETION
Time complexity:
- Deletion at the end: O(1)
- Deletion at the beginning or middle: O(n)

### SEARCHING

*BINARY SEARCH*
If the array is sorted, use binary search.

- Works by repeatedly dividing the search interval.

Time complexity:
- Searching for an element: O(log n)

*LINEAR SEARCH*
If array is unsorted, use linear search. 

- Check each element one by one until finding target element. 

Time complexity:
- Searching for an element: O(n)

