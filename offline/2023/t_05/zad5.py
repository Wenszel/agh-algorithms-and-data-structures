from zad5testy import runtests
from queue import PriorityQueue

def path_finding(vertices, a, b):
    distances = [float('inf') for _ in range(len(vertices))]
    queue = PriorityQueue()
    queue.put((0, a))

    while not queue.empty():
        distance, vertex = queue.get()
        if distances[vertex] == float('inf'):
            distances[vertex] = distance
            for v in vertices[vertex]:
                queue.put((distance + v[1], v[0]))
    return distances[b]


def add_singularity_edges(E, S):
    n = len(S)
    for i in range(n):
        for j in range(i, n):
            E.append((S[i], S[j], 0))

def create_adjacency_list(E, n):
    adjacency_list = [[] for _ in range(n)]
    for edge in E:
        adjacency_list[edge[0]].append((edge[1], edge[2]))
        adjacency_list[edge[1]].append((edge[0], edge[2]))
    return adjacency_list

def spacetravel(n, E, S, a, b):
    add_singularity_edges(E, S)
    adjacency_list = create_adjacency_list(E, n)
    time = path_finding(adjacency_list, a, b)
    return None if time == float('inf') else time



runtests(spacetravel, all_tests=False)
