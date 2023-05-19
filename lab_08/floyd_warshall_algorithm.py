import numpy as np


def floyd_warshall(G):
    n = len(G)
    distance = G
    for intermediate in range(n):
        for start in range(n):
            if intermediate == start:
                continue
            for end in range(n):
                if intermediate == end or start == end:
                    continue
                distance[start][end] = min(distance[start][end],
                                           distance[start][intermediate] + distance[intermediate][end])
    return distance


INF = float('inf')
graph1 = [
    [0, 5, INF, 10],
    [INF, 0, 3, INF],
    [INF, INF, 0, 1],
    [INF, INF, INF, 0]
]
graph2 = [
    [0, 3, INF, 7],
    [8, 0, 2, INF],
    [5, INF, 0, 1],
    [2, INF, INF, 0]
]
print(np.matrix(floyd_warshall(graph1)))
print(np.matrix(floyd_warshall(graph2)))
