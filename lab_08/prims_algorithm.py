from queue import PriorityQueue
def prims_algorithm(G, s):
    n = len(G)
    queue = PriorityQueue()
    queue.put((0, s))
    distance = [float('inf')] * n
    visited = [False] * n
    parent = [None] * n
    while not queue.empty():
        weight, vertex = queue.get()
        visited[vertex] = True
        for edge in G[vertex]:
            if not visited[edge[0]] and distance[edge[0]] > edge[1]:
                distance[edge[0]] = edge[1]
                queue.put((distance[edge[0]], edge[0]))
                parent[edge[0]] = vertex
    return parent


graph = [
    [(1, 1), (4, 5), (5, 8)],
    [(0, 1), (2, 3)],
    [(1, 3), (3, 6), (4, 4)],
    [(2, 6), (4, 2)],
    [(0, 5), (2, 4), (3, 2), (5, 7)],
    [(0, 8), (4, 7)]
]
print(prims_algorithm(graph, 2))
