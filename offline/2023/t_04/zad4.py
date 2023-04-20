from zad4testy import runtests

def bfs_shortest_paths(G, s, t):
    n = len(G)
    visited = [False] * n
    path = [[] for _ in range(n)]
    visited[s] = True
    q = list()
    q.append(s)
    while len(q) > 0:
        visiting = q.pop(0)
        for neighbour in G[visiting]:
            if not visited[neighbour]:
                q.append(neighbour)
                visited[neighbour] = True
                for el in path[visiting]:
                    path[neighbour].append(el)
                path[neighbour].append(visiting)
                if visiting == t:
                    path[t].append(t)
                    return path
    path[t].append(t)
    return path

def bfs_without_edge(G, s, t, i, j):
    n = len(G)
    visited = [False] * n
    distance = [-1] * n

    visited[s] = True
    distance[s] = 0

    q = list()
    q.append(s)
    while len(q) > 0:
        visiting = q.pop(0)
        for neighbour in G[visiting]:
            if not visited[neighbour] and not (
                    (visiting == i and neighbour == j) or (visiting == j and neighbour == i)):
                q.append(neighbour)
                visited[neighbour] = True
                distance[neighbour] = distance[visiting] + 1
                if visiting == t:
                    return distance
    return distance

def longer(G, s, t):
    path = bfs_shortest_paths(G, s, t)[t]
    distance = len(path) - 1
    if distance == -1:
        return None
    new_distance = bfs_without_edge(G, s, t, s, path[1])
    if distance < new_distance[t] or new_distance[t] == -1:
        return s, path[1]
    new_distance = bfs_without_edge(G, s, t, t, path[-2])
    if distance < new_distance[t] or new_distance[t] == -1:
        return t, path[-2]
    for i in range(2, len(path)):
        new_distance = bfs_without_edge(G, s, t, path[i], path[i-1])
        if distance < new_distance[t] or new_distance[t] == -1:
            return path[i], path[i-1]
    return None


runtests(longer, all_tests=True)
