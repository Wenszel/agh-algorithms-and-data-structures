from adjacency_list_representation import Graph

def dfs(graph):
    def dfs_visit(g, v):
        nonlocal time, visited
        time += 1
        times[v] = time
        visited[v] = True
        for neighbour in g[v]:
            if not visited[neighbour]:
                parent[neighbour] = v
                dfs_visit(g, neighbour)
        time += 1

    n = len(graph)
    visited = [False] * n
    parent = [None] * n
    times = [0] * n
    time = 0

    for vertex in range(n):
        if not visited[vertex]:
            dfs_visit(graph, vertex)

    return visited, parent, times


SIZE = 8
vertices = [i for i in range(SIZE)]
edges = [(0, 1), (0, 2), (2, 3), (3, 4), (4, 5), (5, 6), (6, 7), (2, 5), (1, 4)]
g = Graph(vertices, edges)
g.print_list()
v, p, t = dfs(g.l)
print(p, t)
