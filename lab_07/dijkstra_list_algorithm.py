from queue import PriorityQueue
def dijkstra(G, source):
    distance = [float('inf') for _ in range(len(G))]
    queue = PriorityQueue()
    distance[source] = 0
    queue.put(source)
    while not queue.empty():
        vertex = queue.get()
        for i in range(len(G[vertex])):
            neighbour, weight = G[vertex][i]
            queue.put(neighbour)
            if distance[neighbour] > distance[vertex] + G[vertex][i][1]:
                distance[neighbour] = distance[vertex] + G[vertex][i][1]
    return distance


graph = [[(1, 2), (2, 4)],
         [(2, 1), (3, 7)],
         [(4, 3)],
         [(5, 1)],
         [(3, 2), (5, 5)],
         []]


print(dijkstra(graph, 0))
