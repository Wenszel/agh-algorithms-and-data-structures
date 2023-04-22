from adjacency_list_representation import Graph
# Algorithms counts coherent components of a graph
def coherent_components(G):
    n = len(G)
    visited = [False] * len(G)
    components = 0
    for v in range(n):
        if not visited[v]:
            components += 1
            bfs_visit(G, v, visited)
    return components

def bfs_visit(G, i, visited):
    queue = list()
    visited[i] = True
    queue.append(i)
    while len(queue) > 0:
        v = queue.pop(0)
        for p in G[v]:
            if not visited[p]:
                queue.append(p)
                visited[p] = True


vertices = [i for i in range(7)]
edges = [(0, 1), (0, 3), (2, 1), (2, 3), (4, 5)]
graph = Graph(vertices, edges)
print(coherent_components(graph.l))
