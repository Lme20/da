
# Binary Search Trees (BST)

## Operation

### INSERT
1. Start from the root.
2. Compare the inserting node with root, if less, go left, else go right.
3. Do step 2 until we find an empty spot in either left or right.
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

Time complexity:
- Average Case: O(log n)
- Worst Case: O(n)

## Red-Black trees

### Operation
Worst-case
- INSERT: O(log N)
- SEARCH: O(log N)
- DELETE: O(log N)

Amortized-case
- INSERT: O(log N)
- SEARCH: O(1)
- DELETE: O(1)

## AVL trees

For any one, the height of its two subtrees differs by at most 1. 

Balance factor = height of left subtree - height of right subtree
- Valid values of balance factor = {-1, 0, 1}

### Operation
Worst-case
- INSERT: O(log N)
- SEARCH: O(log N)
- DELETE: O(log N)

Amortized-case
- INSERT: Θ(log N)
- SEARCH: Θ(log N)
- DELETE: Θ(log N)