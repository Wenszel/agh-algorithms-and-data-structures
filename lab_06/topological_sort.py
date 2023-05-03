from lab_05 import adjacency_list_representation

def topological_sort(G):
    n = len(G)
    visited = [False] * n
    sorted_vertices = []
    for vertex in range(n):
        if not visited[vertex]:
            dfs_visited(G, visited, vertex, sorted_vertices)
    return sorted_vertices


def dfs_visited(G, visited, vertex, sorted_vertices):
    visited[vertex] = True
    for neighbour in G[vertex]:
        if not visited[neighbour]:
            dfs_visited(G, visited, neighbour, sorted_vertices)
    sorted_vertices.insert(0, vertex)


def run_topological_sort():
    vertices = [i for i in range(8)]
    edges = [(0, 1), (0, 2), (1, 3), (3, 5), (5, 6), (5, 7), (4, 5), (2, 4)]
    graph = adjacency_list_representation.Graph(vertices, edges, True)
    graph.print_list()
    print(topological_sort(graph.l))

# run_topological_sort()

