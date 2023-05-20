from queue import PriorityQueue
# Edmonds-Karp algorithm is an implementation of Ford-Fulkerson algorithm
# with BFS as a method of finding augmenting paths.
# Steps:
# 1. Find an augmenting path using BFS.
# 2. Find the bottleneck of the path.
# 3. Update the flow matrix.
# 4. Repeat until there is no augmenting path.
# 5. Return the maximum flow.
# Complexity: O(V * E^2)
def edmonds_karp_algorithm(G, s, t):
    maximum_flow = 0
    # We are given a graph G as an adjacency list, so we need to convert it to a matrix.
    flow_matrix = get_flow_matrix(G)
    is_path, parent = bfs(flow_matrix, s, t)
    while is_path:
        bottleneck = find_bottleneck(flow_matrix, parent, t)
        maximum_flow += bottleneck
        update_flow_matrix(flow_matrix, parent, s, t, bottleneck)
        is_path, parent = bfs(flow_matrix, s, t)
    return maximum_flow


def bfs(flow, s, t):
    n = len(flow)
    visited = [False] * n
    parent = [None] * n
    queue = PriorityQueue()
    queue.put(s)
    visited[s] = True
    while not queue.empty():
        v = queue.get()
        for u in range(n):
            if flow[v][u] != 0 and not visited[u]:
                visited[u] = True
                parent[u] = v
                queue.put(u)
            if visited[t]:
                return visited[t], parent
    return visited[t], parent


def find_bottleneck(flow, parent, t):
    bottleneck = float('inf')
    while parent[t] is not None:
        bottleneck = min(bottleneck, flow[parent[t]][t])
        t = parent[t]
    return bottleneck

def get_flow_matrix(G):
    n = len(G)
    flow = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(len(G)):
        for j in G[i]:
            flow[i][j[0]] = j[1]
    return flow

def update_flow_matrix(flow, parent, s, t, bottleneck):
    while t != s:
        flow[parent[t]][t] -= bottleneck
        flow[t][parent[t]] += bottleneck
        t = parent[t]


graph1 = [[(1, 4), (3, 3)],
          [(3, 2), (2, 2)],
          [(5, 4)],
          [(2, 2), (4, 2)],
          [(5, 5)], []]

graph2 = [[(1, 10), (3, 10)],
          [(2, 25)],
          [(5, 10)],
          [(4, 15)],
          [(1, 6), (5, 10)], []]

print(edmonds_karp_algorithm(graph1, 0, 5))
print(edmonds_karp_algorithm(graph2, 0, 5))
