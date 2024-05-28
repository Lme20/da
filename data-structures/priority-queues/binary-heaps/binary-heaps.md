# Minimum-heap

- the value of each node is smaller than or equal to the values of its children.
- the minimum element is always at the root of the heap.


worst-case time complexity for insertion and deletion:
O(log n) where n is the number of elements in the heap. 

## Operations:

### Deletion

To delete the minimum element from a minimum-heap, also known as extracting the minimum, we follow these steps:
1. Replace the root node with the last node in the heap.
2. Compare the new root with its children and swap it with the smaller child if necessary.
3. Repeat step 2 until the heap property is restored.

### Insertion

To insert a new element into a minimum-heap, we follow these steps:
1. Add the new element as the last node in the heap.
2. Compare the new element with its parent and swap them if necessary to maintain the heap property.
3. Repeat step 2 until the heap property is restored.

# Maximum-heap

- The value of each node is greater than or equal to the values of its children.
- the maximum element is always at the root of the heap.

## Operations:

### Deletion

To delete the maximum element from a maximum-heap, also known as extracting the maximum, we follow similar steps as in the deletion operation for a minimum-heap. However, instead of swapping with the smaller child, we swap with the larger child.

### Insertion

To insert a new element into a maximum-heap, we follow similar steps as in the insertion operation for a minimum-heap. However, instead of comparing with the parent and swapping if necessary, we compare with the parent and swap if the new element is greater than the parent.
