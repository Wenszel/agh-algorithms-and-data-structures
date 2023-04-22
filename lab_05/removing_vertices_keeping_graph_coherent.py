from adjacency_list_representation import Graph
# The algorithm removes vertices in such an order that the graph remains connected
def coherent(G):
    n = len(G)
    w = []
    visited = [False for _ in range(n)]
    dfs_visit(G, 0, visited, w)
    return w

def dfs_visit(G, s, visited, w):
    visited[s] = True
    for v in G[s]:
        if not visited[v]:
            dfs_visit(G, v, visited, w)
            w.append(s)


vertices = [i for i in range(5)]
edges = [(0, 1), (0, 2), (0, 4), (2, 3), (1, 4), (2, 4), (1, 2)]
graph = Graph(vertices, edges)
print(coherent(graph.l))


