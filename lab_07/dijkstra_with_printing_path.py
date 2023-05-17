from queue import PriorityQueue
def dijkstra(G, source):
    n = len(G)
    distance = [float('inf') for _ in range(len(G))]
    queue = PriorityQueue()
    parent = [None] * n
    distance[source] = 0
    queue.put(source)
    while not queue.empty():
        vertex = queue.get()
        for i in range(len(G[vertex])):
            neighbour, weight = G[vertex][i]
            queue.put(neighbour)
            if distance[neighbour] > distance[vertex] + G[vertex][i][1]:
                parent[neighbour] = vertex
                distance[neighbour] = distance[vertex] + G[vertex][i][1]
    return parent

def print_path(G, s, t):
    shortest_path_from_s_to_t = []
    parents = dijkstra(G, s)
    while t is not None:
        shortest_path_from_s_to_t.insert(0, t)
        t = parents[t]
    print(shortest_path_from_s_to_t)


graph = [[(1, 2), (2, 4)],
         [(2, 1), (3, 7)],
         [(4, 3)],
         [(5, 1)],
         [(3, 2), (5, 5)],
         []]


print_path(graph, 0, 5)
