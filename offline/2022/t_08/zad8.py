from math import sqrt, ceil
from zad8testy import runtests
def kruskal_algorithm(G):
    n = get_graph_size_based_on_edges(G)
    sets = list(range(n))
    ranks = [0] * n
    G.sort(key=lambda x: x[2])
    MST = []
    for u, v, t in G:
        if find(u, sets) != find(v, sets):
            union(u, v, ranks, sets)
            MST.append((u, v, t))
    return MST

def find(u, s):
    if s[u] == u:
        return u
    s[u] = find(s[u], s)
    return s[u]

def union(u, v, r, s):
    ur, vr = find(u, s), find(v, s)
    if ur != vr:
        if r[ur] > r[vr]:
            s[vr] = ur
        elif r[vr] > r[ur]:
            s[ur] = vr
        else:
            s[vr] = ur
            r[ur] += 1


def get_graph_size_based_on_edges(edges):
    edge_with_biggest_vertex = max(edges, key=lambda x: max(x[0], x[1]))
    biggest_vertex = max(edge_with_biggest_vertex[0], edge_with_biggest_vertex[1])
    return biggest_vertex + 1  # because vertices are indexed from 0

def is_connected(MST, n):
    visited = [False] * n
    for edge in MST:
        visited[edge[0]] = True
        visited[edge[1]] = True
    return all(visited)

def bfs(G, s):
    n = len(G)
    visited = [False] * n
    queue = []
    queue.append(s)
    visited[s] = True
    while len(queue) > 0:
        v = queue.pop(0)
        for u in G[v]:
            if not visited[u]:
                visited[u] = True
                queue.append(u)
    return all(visited)
def is_coherent(edges, n):
    G = [[] for _ in range(n)]
    for i in range(len(edges)):
        G[edges[i][0]].append(edges[i][1])
        G[edges[i][1]].append(edges[i][0])
    return bfs(G, 0)
def length(cordsA, cordsB):
    return ceil(sqrt((cordsA[0] - cordsB[0]) ** 2 + (cordsA[1] - cordsB[1]) ** 2))
def highway(A):
    minimum = float('inf')
    edges = []
    for i in range(len(A)):
        for j in range(i, len(A)):
            if i != j:
                edges.append((i, j, length(A[i], A[j])))
    mst = kruskal_algorithm(edges)
    while is_coherent(mst, len(A)):
        minimum = min(minimum, max(mst, key=lambda x: x[2])[2] - min(mst, key=lambda x: x[2])[2])
        edges.remove(mst[0])
        mst = kruskal_algorithm(edges)
    return minimum

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( highway, all_tests = True )