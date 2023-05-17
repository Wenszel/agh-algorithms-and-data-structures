from queue import PriorityQueue
def dijkstra(M, s):
    n = len(M)
    inf = float('inf')
    d = [inf for _ in range(n)]
    parent = [None for _ in range(n)]
    q = PriorityQueue()
    q.put((0, s))
    d[s] = 0
    while not q.empty():
        distance, u = q.get()[1]
        if d[u] == inf:
            d[u] = distance
        for v in range(n):
            if M[u][v] >= 0 and d[v] == inf:
                q.put((d[u] + M[u][v], v))
                relax(M, u, v, d, parent)
    return d, parent

def relax(M, u, v, d, parent):
    if d[v] > d[u] + M[u][v]:
        d[v] = d[u] + M[u][v]
        parent[v] = u