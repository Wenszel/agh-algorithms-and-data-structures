from topological_sort import topological_sort
# A Hamiltonian path is a path in an undirected or directed graph that visits each vertex exactly once.
# To determine whether a graph has a Hamiltonian path we follow these steps:
# 1. Topologically sort the graph
# 2. Check if the next vertex in the topologically sorted graph is a neighbour of the current vertex
# 3. If it is, continue, if it isn't, return False
# 4. If we reach the end of the topologically sorted graph, return True
def is_hamiltonian_path(G):
    sorted_graph = topological_sort(G)
    for i in range(len(sorted_graph)-1):
        if sorted_graph[i+1] not in G[sorted_graph[i]]:
            return False
    return True


graph = [
    [3, 2],
    [3],
    [1, 3],
    []
]

print(is_hamiltonian_path(graph))
