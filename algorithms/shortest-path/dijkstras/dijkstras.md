# Dijktra's algorithm - Find the shortest path

*Examples given in a weighted graph*

*Breadth-first search (BFS) is more commonly used for unweighted graphs*

Goal: To find the shortest path from a source vertex to all other vertices in a graph

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

### Calculating values

When calculating the properties of vertices (nodes) in a graph, you should account for the following:

- d[v]: Represents the shortest known distance from the start node to a vertex v. This is what is set as infinity for all vertices except for the starting node, which is set as 0.

- π[v]: Represents the predecessor of a vertex V on the shortest path from the start node to V. 

## Pseudocode

## Implementation


## Time Complexity
Θ((|V|+|E|)log|E|)

## Space Complexity

