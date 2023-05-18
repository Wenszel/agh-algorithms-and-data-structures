import numpy as np
def floyd_warshall(G):
    n = len(G)
    distance = G
    for k in range(n):
        for i in range(n):
            for j in range(n):
                distance[i][j] = min(distance[i][j], distance[i][k] + distance[k][j])
    return distance


INF = float('inf')
graph = [
    [0,   5, INF, 10],
    [INF,  0,  3,  INF],
    [INF, INF, 0,   1],
    [INF, INF, INF, 0]
]

print(np.matrix(floyd_warshall(graph)))
