# Prim's algorithm - Minimal Cost Spanning Trees

*Results in a minimum-spanning tree, minimum weight connected graph, no cycles*

*can Also be used with a priority queue*

GOAL: find the Minimum Spanning Tree (MST) of a graph.
- Example of a greedy algorithm

## Steps

1. Initialize the MST with a single vertex chosen arbitrarily. (pick a node on the graph)
2. While the MST does not contain all vertices:
   - Find the edge with the minimum weight that connects a vertex in the MST to a vertex outside the MST.
   - Add this edge to the MST.
3. Repeat until all vertices are included in the MST.

### Calculating values

- Start from an arbitrary vertex, add it to the MST.
- Use a priority queue to select the edge with the minimum weight that connects the MST to a new vertex.
- Continue selecting the smallest edge until all vertices are included.

## Pseudocode

## Implementation


## Time Complexity

- O(E log V) using an adjacency list and a priority queue. (binary heap)
- O(V^2) using an adjacency matrix.

## Space Complexity

- O(V + E) using an adjacency list.
- O(V^2) using an adjacency matrix.