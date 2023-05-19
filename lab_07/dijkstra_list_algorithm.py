from queue import PriorityQueue

def dijkstra(G, source):
    queue = PriorityQueue()
    distance = [float('inf') for _ in range(len(G))]
    distance[source] = 0
    queue.put((0, source))
    while not queue.empty():
        _, vertex = queue.get()
        for edge in G[vertex]:
            neighbour, weight = edge
            if distance[neighbour] > distance[vertex] + weight:
                distance[neighbour] = distance[vertex] + weight
                queue.put((distance[neighbour], neighbour))
    return distance


graph1 = [[(1, 2), (2, 4)],
          [(2, 1), (3, 7)],
          [(4, 3)],
          [(5, 1)],
          [(3, 2), (5, 5)],
          []]
graph2 = [
    [(1, 4), (2, 1)],
    [(3, 2)],
    [(1, 3), (3, 5)],
    [(4, 1)],
    [(2, 3), (5, 2)],
    [(6, 4)],
    [(5, 3), (7, 2)],
    [(4, 6), (7, 3)]]

print(dijkstra(graph1, 0))
print(dijkstra(graph2, 0))
