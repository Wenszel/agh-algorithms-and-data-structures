from zad6testy import runtests
from queue import PriorityQueue

def edmonds_karp_algorithm(flow_matrix, s, t):
    maximum_flow = 0
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



def binworker(M):
    n = len(M) # ilosc pracownikow
    m = len(M) # liczba maszyn
    source = m + n
    sink = source + 1
    flow = [[0 for _ in range(m + n + 2)] for _ in range(m + n + 2)]
    for i in range(m):
        for j in M[i]:
            flow[i][m + j] = 1
    for i in range(m):
        flow[source][i] = 1
    for i in range(n):
        flow[m + i][sink] = 1
    return edmonds_karp_algorithm(flow, source, sink)

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( binworker, all_tests = True )
