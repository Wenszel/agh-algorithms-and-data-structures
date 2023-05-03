from lab_05 import adjacency_list_representation


def find_times(g):
    def dfs_visit(v):
        nonlocal g, time, times, visited
        visited[v] = True
        for neighbour in g[v]:
            if not visited[neighbour]:
                dfs_visit(neighbour)
        time += 1
        times[v] = time

    n = len(g)
    visited = [False] * n
    times = [0] * n
    time = 0
    for i in range(n):
        if not visited[i]:
            dfs_visit(i)
    return times


def priority_indexes(p):
    return [len(p) - p[i] for i in range(len(p))]


def dfs(g, times):
    def dfs_visit(v, index):
        nonlocal g, dags, visited
        visited[v] = True
        dags[index].append(v)
        for neighbour in g[v]:
            if not visited[neighbour]:
                dfs_visit(neighbour, index)

    n = len(g)
    visited = [False] * n
    dags = []
    for i in priority_indexes(times):
        if not visited[i]:
            dags.append([])
            dfs_visit(i, len(dags) - 1)
    return dags


def find_scc_in_graph(g, edges):
    priority = find_times(g.l)
    reversed_graph = adjacency_list_representation.Graph([i for i in range(len(g.l))], [(v, u) for u, v in edges], True)
    return dfs(reversed_graph.l, priority)


def run_find_scc_in_graph():
    edges = [(0, 1), (1, 2), (2, 0), (2, 3), (3, 4), (4, 5), (5, 3), (3, 6), (6, 5), (9, 5), (10, 7), (7, 8), (9, 10),
             (10, 3), (8, 9), (2, 8)]
    vertices = [i for i in range(11)]
    graph = adjacency_list_representation.Graph(vertices, edges, True)
    priority = find_times(graph.l)
    reversed_graph = adjacency_list_representation.Graph(vertices, [(v, u) for u, v in edges], True)
    print(dfs(reversed_graph.l, priority))


# run_find_scc_in_graph()
