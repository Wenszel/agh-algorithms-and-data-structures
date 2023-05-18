# - Bellman-Ford algorithm finds the shortest paths from vertex s to other vertices
# - Unlike Dijkstra algorithm Bellman-Ford works fine when edges have negative weights
# - When negative cycle is detected then Bellman-Ford algorithm returns False which means
#   that there the shortest paths can not be determined.
# - Time Complexity is O(V*E)

def bellman_ford(G, s):
    distances = [float('inf')] * NO_VERTICES
    distances[s] = 0
    for i in range(NO_VERTICES):
        for edge in G:
            relax(edge, distances)
    for edge in G:
        # If any vertex can still be relaxed after all the above relaxations,
        # it means that there is a negative cycle.
        if distances[edge[1]] > distances[edge[0]] + edge[2]:
            return False
    return distances

def relax(edge, distances):
    if distances[edge[1]] > distances[edge[0]] + edge[2]:
        distances[edge[1]] = distances[edge[0]] + edge[2]


graph1 = [
    [0, 1, 5],
    [0, 2, 2],
    [1, 3, 1],
    [2, 1, -3],
    [3, 2, 3]
]

graph2 = [
    [0, 1, 4],
    [0, 2, 1],
    [1, 3, -2],
    [2, 1, 3],
    [3, 2, 2]
]

graph3 = [
    [0, 1, -2],
    [0, 2, 3],
    [1, 3, 1],
    [2, 1, 2],
    [3, 2, -4]
]

graph4 = [
    [0, 1, 5],
    [0, 2, 2],
    [1, 3, 1],
    [2, 1, -1],
    [3, 2, 3]
]

graph5 = [
    [0, 1, 4],
    [0, 2, 1],
    [1, 3, -2],
    [2, 1, 3],
    [3, 2, 2]
]
lists_of_graphs = [graph1, graph2, graph3, graph4, graph5]
NO_VERTICES = 4
for graph in lists_of_graphs:
    print(bellman_ford(graph, 0))
