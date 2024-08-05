def traverseDFS(G, v, visited):
    if v not in visited:
        visited.add(v)
        PreVisit(G, v)
        for edge in G.outgoingEdges(v):
            traverseDFS(G, edge.end, visited)
        PostVisit(G, v)