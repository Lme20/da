# Dijktra's algorithm - Find the shortest path

*Examples given in a weighted graph*

*Breadth-first search (BFS) is more commonly used for unweighted graphs*

## Steps

1. Mark all nodes as unvisited

2. Assign all nodes a tentative distance value
    - Starting node has the shortest path of 0
    - Assign a tentative distance of infinity to all other nodes, 

3. For the current node calculate the distance to all unvisited neighbors
    - For the current node, consider all its unvisited neighbors and calculate their tentative distances through the current node.
    - Compare the newly calculated tentative distance to the current assigned value for each neighbor, and update it if the new value is less. 

4. Mark current node as visited
    - Add the current node to the set of visited nodes.
    - Remove it from the unvisited set.

5. Choose new current node from unvisited nodes with minimal distance
    - Repeat steps 3 to 5 until all nodes have been visited or the smallest tentative distance among the unvisited nodes is infinity (which means they are not reachable from the starting node).

## Pseudocode

## Implementation


## Time Complexity

## Space Complexity

