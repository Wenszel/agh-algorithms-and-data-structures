from zad4testy import runtests
def bfs(G, s, t, i, j):
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
    distance = bfs(G, s, t, -1, -1)[t]
    if distance == -1:
        return None
    for i in G[s]:
        new_distance = bfs(G, s, t, s, i)
        if distance < new_distance[t] or new_distance[t] == -1:
            return s, i
    for i in G[t]:
        new_distance = bfs(G, s, t, t, i)
        if distance < new_distance[t] or new_distance[t] == -1:
            return t, i
    for i in range(len(G)):
        if not (i == s or i == t):
            for j in G[i]:
                new_distance = bfs(G, s, t, i, j)
                if distance < new_distance[t] or new_distance[t] == -1:
                    return i, j
    return None


runtests(longer, all_tests=True)
