from egzP5btesty import runtests 

def find_bridges(graph):
    def dfs_visit(graph, vertex):
        nonlocal time
        time += 1
        times[vertex] = time
        lows[vertex] = time
        visited[vertex] = True
        for neighbour in graph[vertex]:
            if not visited[neighbour]:
                parents[neighbour] = vertex
                dfs_visit(graph, neighbour)
                lows[vertex] = min(lows[vertex], lows[neighbour])
                if lows[neighbour] > times[vertex]:
                    bridges.append((vertex, neighbour))
            elif neighbour != parents[vertex]:
                lows[vertex] = min(lows[vertex], times[neighbour])

    n = len(graph)
    bridges = []
    visited = [False] * n
    parents = [None] * n
    times = [0] * n
    lows = [0] * n
    time = 0
    for i in range(n):
        if not visited[i]:
            dfs_visit(graph, i)
    return bridges

def koleje ( B ):
    def get_number_of_stations():
        maximum = 0
        for start_station, end_station in B:
            maximum = max(maximum, start_station, end_station)
        return maximum + 1
    
    
    def is_wkw(station):
        return len(G[station]) > 1
    
    number_of_vertices = get_number_of_stations()
    length_of_B = len(B)
    G = [[] for _ in range(number_of_vertices)]
    T = [] * length_of_B
    for start, end in B:
        if start < end:
            T.append((start, end))
        else:
            T.append((end, start))
            
    T.sort(key= lambda x: (x[0], x[1]))
    last = None
    for start, end in T:
        if (start, end) != last:
            G[start].append(end)
            G[end].append(start)
            last = (start, end)


    bridges = find_bridges(G)
    candidates = []    
    for bridge in bridges:
        start, end = bridge
        if start not in candidates:
            candidates.append(start)
        if end not in candidates:
            candidates.append(end)
    output = 0
    for candidate in candidates:
        if is_wkw(candidate):
            output += 1
    return output


runtests ( koleje, all_tests=True)