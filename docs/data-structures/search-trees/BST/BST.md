
# Binary Search Trees (BST)

- Are sorted or ordered binary trees
- Nodes can have 2 subtrees
- Items to left of given node = smaller
- Items to right of given node = larger

height = number of nodes on the longest path from the root to leaf node

BST search, insert, and delete operations typically run in time O(n), where N is the depth of the relevant node in the tree

## Operations
### INSERT
1. Start from the root.
2. Compare the inserting node with root, if less, go left, else go right.
3. Do step 2 until we find an empty spot in either left or right subtree.
4. Place the inserting node at the empty spot found in step 3.

Time complexity:
- Average Case: O(log n)
- Worst Case: O(n)

### SEARCH
1. Start from the root.
2. Compare the searching element with root, if less, go left, else go right.
3. Do step 2 until we find the element or reach a leaf node (null).
4. If found, return the node, else signal that the element is not in the tree.

Time complexity:
- Average Case: O(log n)
- Worst Case: O(n)

### DELETE
1. Start from the root and find the node to delete.
2. If the node is a leaf node, we can simply remove it.
3. If the node has one child, replace the node with its child.
4. If the node has two children, replace the node with its in-order predecessor or in-order successor node and delete that node. You can choose to always replace with the in-order predecessor, always replace with the in-order successor, or alternate between the two.

NOTE: when deleting root node, replace node with its greatest value on its left side or smallest value on its right side

Time complexity:
- Average Case: O(log n)
- Worst Case: O(n)

# Red-Black trees (Balanced Search Trees)
NIL: node at the end of a tree, usually black

- Specific type of balanced search trees
- Nodes are either red or black
- Root and NIL leaves are always black
- if a node is red, then its children are black
- All paths from a node to its (NIL) descendants contain the same number of black nodes
- The longest path (root farthest to NIL) is not larger than twice the length of the shortest path (root nearest to NIL)

NOTE: BST rules still apply!!!

## Operations
### ROTATE
- Rotate left:


- Rotate right:
 1. Given a node A with left child B

### INSERT (Requires rotation)
NOTE: same procedure as BST insertion

1. New inserted node should be red
2. 
### DELETE (Requires rotation)

### SEARCH

## Time complexities
Rotations: O(1)

Worst-case
- INSERT: O(log N)
- SEARCH: O(log N)
- DELETE: O(log N)

Amortized-case
- SEARCH: O(log N)
- INSERT: O(1)
- DELETE: O(1)

Rotations have a time complexity of O(1)

## Pseudocode

# AVL trees (self-balancing BST)
For any one, the height of its two subtrees differs by at most 1. 

- We perform fixes after delete and insert to keep the tree height balance
- Similar to red-black trees
- Adheres to the properties of a BST, with the added condition that the height difference between the left and right subtrees of any node is at most 1.

Balance factor = height of right subtree - height of left subtree
- Valid values of balance factor = {-1, 0, 1}
## Operations

### INSERT
### SEARCH
### DELETE

## Time complexities
Rotations: O(1)

Worst-case
- INSERT: O(log N)
- SEARCH: O(log N)
- DELETE: O(log N)

Amortized-case
- INSERT: Θ(log N)
- SEARCH: Θ(log N)
- DELETE: Θ(log N)

## Pseudocode
