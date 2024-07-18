# DEPTH-FIRST-SEARCH - explore nodes and edges of a graph

- Not very useful used by itself
- Better used when augmented for counting connected components, determine connectivity, find bridges points, etc
- Plunges into a graph without regard for which edge it takes next
- Continues until no new edge can be attained, where it backtracks and continues

Finding connected components: separated sections of a graph
- Assign integer values to each group to tell them apart
- Start DFS at every node (except if already visited)
- mark all reachable nodes with the integer value of its corresponding group 

What can DFS do? 
- Compute a graph's minimum-spanning tree
- Detect and find cycles in a graph
- Check if a graph is bipartite
- Find strongly connected components
- Topologically sort nodes of a graph
- Find bridges and articulation points
- Find articulating paths in a flow network
- Generate mazes

## STEPS

1. Start at node 0 (can start at any node)
2. Pick any available node from node 0
    - If node has been visited, backtrack (go back to a previously visited node where new unvisited nodes can be visited)
    - If node is new, continue

3. Continue until reaching node with dead end, if dead end, backtrack
4. DFS ends when all reachable nodes from the initial node have been visited. 

## OPERATIONS


## COMPLEXITY

## PSEUDOCODE
Does not include pseudocode for finding connected components. 
    # Global or class scope variables
    n = number of nodes in the graph
    g = Adjacency list representing graph
    visited = [false,...,false] # size n

    function dfs(at):
        if visited[at] = return
        visited[at] = true

    neighbors = graph[at]
    for next in neighbors:
        dfs(next)

    #start dfs at node 0
    start_node= 0
    dfs(start_node)