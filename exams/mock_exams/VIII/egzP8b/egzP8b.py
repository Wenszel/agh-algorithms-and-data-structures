from egzP8btesty import runtests

def floyd_warshall(G):
    n = len(G)
    distance = G
    for intermediate in range(n):
        for start in range(n):
            if intermediate == start:
                continue
            for end in range(n):
                if intermediate == end or start == end:
                    continue
                distance[start][end] = min(distance[start][end],
                                           distance[start][intermediate] + distance[intermediate][end])
    return distance
def list_to_matrix(L):
    n = len(L)
    M = [[float("inf") for _ in range(n)] for _ in range(n)]
    for v in range(n):
        for neigh, cost in L[v]:
            M[v][neigh] = cost
            M[neigh][v] = cost
    return M

def robot( G, P ):
    M = list_to_matrix(G)
    total = 0
    distances = floyd_warshall(M)
    
    for i in range(len(P)-1):
        total += distances[P[i]][P[i+1]]
    return total
    
runtests(robot, all_tests = True)
