from adjacency_matrix_representation import Graph
def bfs(graph, start_vertex):
    n = len(graph)
    queue = list()

    distance = [-1 for _ in range(n)]
    parent = [None for _ in range(n)]
    visited = [False] * n

    visited[start_vertex] = True
    distance[start_vertex] = 0

    queue.append(start_vertex)

    while len(queue) != 0:
        visiting = queue.pop(0)
        for i in range(n):
            if graph[visiting][i] and not visited[i]:
                queue.append(i)
                distance[i] = distance[visiting] + 1
                parent[i] = visiting
                visited[i] = True
    return distance, parent, visited


n = 8
vertices = [i for i in range(n)]
edges = [(0, 1), (0, 2), (2, 3), (3, 4), (4, 5), (5, 6), (6, 7), (2, 5), (1, 4)]
g = Graph(vertices, edges)
d, p, v = bfs(g.m, 0)
print("Max distance: ", max(d))
print("Parents of each vertex", [(i, p[i]) for i in range(n)])
g.print_matrix()
