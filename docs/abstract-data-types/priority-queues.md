# Priority Queues

A priority queue is an ADTs. Similar to queues, it operates by:

1. *Adding elements with a priority:* Each element in the priority queue is associated with a priority. The priority can be any comparable value such as an integer or float.
2. *Removing elements with highest priority first:* When removing elements from a priority queue, the element with the highest prioriy gets removed first. If two elements have the same priority, the order of removal can be based on their order of insertion or other criterion. 

- Only supports elements that are comparable
- Very common in Dijkstra's Shortest Path Algorithm and MST (Prim's, Kruskal's)
- FIFO ADT (First-in First Out)

## Implementation

### 1. Binary Heaps

### 2. Balanced Binary Search Tree

### 3. Unsorted List

### 4. Sorted List

## Complexity (with Binary Heaps)

Binary Heap construction: O(N)
Polling: O(log N)
Peeking: O(1)
Adding: O(log N)
Naive removing: O(N)
Advanced removing (with hash table): O(log N)
Naive contains: O(N)
Contains check (with hash table): O(1)
