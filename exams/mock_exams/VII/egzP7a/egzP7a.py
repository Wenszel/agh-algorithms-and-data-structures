from egzP7atesty import runtests 
from queue import PriorityQueue
def edmonds_karp_algorithm(G, s, t):
    maximum_flow = 0
    # We are given a graph G as an adjacency list, so we need to convert it to a matrix.
    flow_matrix = get_flow_matrix(G)
    is_path, parent = bfs(flow_matrix, s, t)
    while is_path:
        bottleneck = find_bottleneck(flow_matrix, parent, t)
        maximum_flow += bottleneck
        update_flow_matrix(flow_matrix, parent, s, t, bottleneck)
        is_path, parent = bfs(flow_matrix, s, t)
    return maximum_flow


def bfs(flow, s, t):
    n = len(flow)
    visited = [False] * n
    parent = [None] * n
    queue = PriorityQueue()
    queue.put(s)
    visited[s] = True
    while not queue.empty():
        v = queue.get()
        for u in range(n):
            if flow[v][u] != 0 and not visited[u]:
                visited[u] = True
                parent[u] = v
                queue.put(u)
            if visited[t]:
                return visited[t], parent
    return visited[t], parent


def find_bottleneck(flow, parent, t):
    bottleneck = float('inf')
    while parent[t] is not None:
        bottleneck = min(bottleneck, flow[parent[t]][t])
        t = parent[t]
    return bottleneck

def get_flow_matrix(G):
    n = len(G)
    flow = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(len(G)):
        for j in G[i]:
            flow[i][j[0]] = j[1]
    return flow

def update_flow_matrix(flow, parent, s, t, bottleneck):
    while t != s:
        flow[parent[t]][t] -= bottleneck
        flow[t][parent[t]] += bottleneck
        t = parent[t]

def akademik( T ):
    def conver_to_graph():
        graph = []
        start_index = 0
        number_of_students = n
        number_of_rooms = get_number_of_rooms()
        end_index = number_of_students + number_of_rooms + 1
        graph.append([])
        for i in range(1, number_of_students+1):
            graph[start_index].append((i, 1))
            graph.append([])
        for student in range(number_of_students):
            for preference in T[student]:
                if preference is not None:
                    graph[student+1].append((n+preference+1, 1))
                else:
                    break
        for i in range(1, number_of_rooms+1):
            graph.append([])
            graph[n+i].append((end_index, 1))
        graph.append([])
        return graph

    def get_number_of_rooms():
        number_of_rooms = 0
        for prefered_rooms in T:
            for room in prefered_rooms:
                if room is not None:
                    number_of_rooms = max(number_of_rooms, room)
        return number_of_rooms + 1
    
    
    n = len(T)
    number_of_students = n
    number_of_rooms = get_number_of_rooms()
    end_index = number_of_students + number_of_rooms + 1
    number_of_students_without_preferences = 0
    for i in T:
        flag = True
        for j in i:
            if j is not None:
                flag = False
                break
        if flag:
            number_of_students_without_preferences += 1
    
    return number_of_students - edmonds_karp_algorithm(conver_to_graph(), 0, end_index) -  number_of_students_without_preferences


runtests ( akademik )
