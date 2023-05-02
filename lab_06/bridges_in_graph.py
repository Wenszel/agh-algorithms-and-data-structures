from lab_05 import adjacency_list_representation


def dfs(graph):
    def dfs_visit(graph, vertex):
        nonlocal time
        time += 1
        times[vertex] = time
        lows[vertex] = time
        visited[vertex] = True
        for neighbour in graph[vertex]:
            if not visited[neighbour]:
                parents[neighbour] = vertex
                dfs_visit(graph, neighbour)
                lows[vertex] = min(lows[vertex], lows[neighbour])
                if lows[neighbour] > times[vertex]:
                    bridges.append((vertex, neighbour))
            elif neighbour != parents[vertex]:
                lows[vertex] = min(lows[vertex], times[neighbour])

    n = len(graph)
    bridges = []
    visited = [False] * n
    parents = [None] * n
    times = [0] * n
    lows = [0] * n
    time = 0
    for i in range(n):
        if not visited[i]:
            dfs_visit(graph, i)
    return bridges


vertices = [i for i in range(8)]
edges = [(0, 1), (1, 2), (2, 3), (0, 3), (3, 4), (2, 5), (5, 6), (5, 7), (6, 7)]
g = adjacency_list_representation.Graph(vertices, edges)
print(dfs(g.l))
