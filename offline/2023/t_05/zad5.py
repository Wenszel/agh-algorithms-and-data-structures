from zad5testy import runtests
from queue import PriorityQueue


def path_finding(vertices, a, b, S):
    distances = [float('inf') for _ in range(len(vertices))]
    queue = PriorityQueue()
    queue.put((0, a))
    flag = False
    while not queue.empty():
        distance, vertex = queue.get()
        if distances[vertex] == float('inf'):
            distances[vertex] = distance
            for v in vertices[vertex]:
                queue.put((distance + v[1], v[0]))
            if not flag and vertex in S:
                for s in S:
                    queue.put((distance, s))
                flag = True
        if vertex == b:
            return distances[b]


def create_adjacency_list(E, n):
    adjacency_list = [[] for _ in range(n)]
    for edge in E:
        adjacency_list[edge[0]].append((edge[1], edge[2]))
        adjacency_list[edge[1]].append((edge[0], edge[2]))
    return adjacency_list


def spacetravel(n, E, S, a, b):
    adjacency_list = create_adjacency_list(E, n)
    time = path_finding(adjacency_list, a, b, S)
    return None if time == float('inf') else time


runtests(spacetravel, all_tests=True)
