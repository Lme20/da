# Breadth-first search (BFS) - Find the shortest path

- Examines all vertices connected to the start vertex (node), used to explore nodes and edges of a graph
- Has a queue stack instead of a recursion stack  
- Breadth-first search (BFS) is commonly used for unweighted graphs
- BFS is very useful to find the shortest path in an unweighted graph
- BFS can't be used for finding the shortest path in a weighted graph, use Dijkstras instead
- Essentially, contrary to DFS, BFS explores nodes in "layers"
- Uses a queue data structure

## Steps
1. Start at the root node (or any specified starting node).
2. Add neighboring nodes (nodes attached to root node) to queue
    - if no more unvisited neighbors, go to next neighboring node (based on queue order)
3. Continue step 2 with neighboring node
4. Conclude BFS when all nodes have been visited

## UNDIRECTED AND DIRECTED BFS



## Pseudocode

    #Global/ class scope variables
    n = number of nodes in the graph
    g = adjacency list representing unweighted graph

    #s = start node, e= end node, and 0 ≤ e, s < n
    function bfs(s, e):
        #Do a BFS starting at node s
        prev = solve(s)

        #Return reconstructed path from s->e
        return reconstructPath(s, e, prev)

## Time Complexity - Operations

total complexity: O(V+E)
