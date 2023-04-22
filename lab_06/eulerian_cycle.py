from lab_05 import adjacency_matrix_representation
# Algorithm return Eulerian cycle in graph G
def euler_cycle(M):
    M = [M[i][:] for i in range(len(M))]
    result = []
    dfs_visit(M, 0, result)
    return result

def dfs_visit(M, v, result):
    n = len(M)
    for i in range(n):
        if M[v][i] is True:
            M[v][i] = False
            M[i][v] = False
            dfs_visit(M, i, result)
    result.insert(0, v)


vertices = [i for i in range(6)]
edges = [(0, 1), (0, 2), (0, 4), (0, 5), (1, 2), (2, 3), (3, 4), (5, 4), (2, 4)]
graph = adjacency_matrix_representation.Graph(vertices, edges)
print(euler_cycle(graph.m))
