from adjacency_matrix_representation import Graph
def is_bipartite(M):
    n = len(M)
    colors = [0 for _ in range(n)]
    for vertex in range(n):
        if colors[vertex] == 0:
            if not dfs_visit(M, vertex, 1, colors):
                return False
    return True

def dfs_visit(M, s, c, colors):
    colors[s] = c
    c = 2 if c == 1 else 1
    n = len(M)
    for i in range(n):
        if M[s][i]:
            if colors[i] == 0:
                r = dfs_visit(M, i, c, colors)
                if r is False:
                    return False
            elif colors[i] != c:
                return False
    return True


vertices = [i for i in range(8)]
edges = [(0, 4), (0, 5), (0, 6), (1, 5), (1, 7), (2, 6), (3, 6)]
graph = Graph(vertices, edges)
print(is_bipartite(graph.m))

vertices = [i for i in range(4)]
edges = [(0, 1), (0, 2), (0, 3), (1, 2), (1, 3), (2, 3)]
graph = Graph(vertices, edges)
print(is_bipartite(graph.m))
