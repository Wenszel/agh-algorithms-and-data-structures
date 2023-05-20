# Ford-Fulkerson algorithm implementation using DFS as a method of finding augmenting paths.
# Steps:
# 1. Find an augmenting path using DFS.
# 2. Find the bottleneck of the path.
# 3. Update the flow matrix.
# 4. Repeat until there is no augmenting path.
# 5. Return the maximum flow.
# Complexity: O(V * E * C), where C is the maximum capacity of an edge.
def ford_fulkerson_algorithm(matrix_of_flow, source, sink):
    maximum_flow = 0
    is_path, parent = dfs(matrix_of_flow, source, sink)
    while is_path:
        bottleneck = find_bottleneck(graph, parent, sink)
        maximum_flow += bottleneck
        update_flow_matrix(graph, parent, source, sink, bottleneck)
        is_path, parent = dfs(matrix_of_flow, source, sink)
    return maximum_flow


def dfs(matrix_of_flow, s, t):
    n = len(matrix_of_flow)
    parent = [None] * n
    visited = [False] * n
    dfs_visit(graph, s, visited, parent)
    return visited[t], parent


def dfs_visit(matrix_of_flow, source, visited, parent):
    n = len(matrix_of_flow)
    visited[source] = True
    for v in range(n):
        if not visited[v] and graph[source][v] != 0:
            parent[v] = source
            dfs_visit(graph, v, visited, parent)


def find_bottleneck(flow, parent, t):
    bottleneck = float('inf')
    while parent[t] is not None:
        bottleneck = min(bottleneck, flow[parent[t]][t])
        t = parent[t]
    return bottleneck


def update_flow_matrix(flow, parent, s, t, bottleneck):
    while t != s:
        flow[parent[t]][t] -= bottleneck
        flow[t][parent[t]] += bottleneck
        t = parent[t]


graph = [[0, 11, 12, 17, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 14, 0, 0, 0, 0],
         [0, 0, 0, 0, 8, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 9, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 7, 0, 10, 0],
         [0, 0, 0, 0, 0, 0, 6, 9, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 5],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 3],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 8],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]


print(ford_fulkerson_algorithm(graph, 0, 9))
