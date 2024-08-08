# Kruskal's algorithm - Minimum Spanning Trees

- Kruskal's a greedy algorithm

MST: a subset of edges which connect all vertices in the graph with the minimal total edge cost. 

GOAL: To find the Minimum Spanning Tree (MST) of a connected, undirected graph.

Cycle: formed when two nodes that are already connected through edges form a loop. 


## Steps

1. **Sort all edges:** Sort all edges of the graph by ascendig edge weight (smallest to largest)
2. **Process each edge:** For each edge, process the 2 nodes the edge connects 
    - if nodes already unified (i.e., they belong to the same subset) = discard edge
    - otherwise, include edge in the MST and unify the 2 subsets.
3. **Termination:** Terminate algorithm when every edge has been processed or all nodes have been unified. That is, when [n - 1] edges are reached. 

NOTE: unified nodes should be ignored to avoid cycles. 

Calculating the total weight:
- Simply add all of the weights found in every edge of the MST. 

Alternative steps: 

1. Select an edge of G of minimum weight
2. Select a remaining edge of G of minimum weight
3. Select any remaining edge of G that does not form a cycle with previously selected edges
4. Repeat cycle 3 until n-1 edges have been reached

## Pseudocode


## Time Complexity

Overall complexity: O(E log E)

Average complexity: O(V log E)

Where E is the number of edges in the graph.

## Space Complexity
