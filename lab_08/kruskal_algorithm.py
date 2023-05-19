# Kruskal algorithm finds the minimum spanning tree in a graph.
# Steps:
# 1. Sort edges by weight
# 2. Take the smallest edge and check if it creates a cycle
# 3. If it doesn't create a cycle, add it to the MST
# 4. Repeat 2-3 until all vertices are in the MST
# 5. Return the MST
# To handle the cycle problem, we use the union-find data structure.
def kruskal_algorithm(G):
    # In this example, the graph is represented as a list of edges, so we have to get the number of vertices
    n = get_graph_size_based_on_edges(G)
    # keeps track of the representative of the set that the element belongs to
    sets = list(range(n))
    # keeps track of the height of the tree
    ranks = [0] * n
    # sort edges by weight
    G.sort(key=lambda x: x[2])
    MST = []
    for u, v, t in G:
        # if the edge doesn't create a cycle, add it to the MST
        # the edge creates a cycle if the vertices belong to the same set
        if find(u, sets) != find(v, sets):
            union(u, v, ranks, sets)
            MST.append((u, v, t))
    return MST

# returns the representative of the set that the element belongs to
def find(u, s):
    if s[u] == u:
        return u
    s[u] = find(s[u], s)
    return s[u]

# merges two sets into one
def union(u, v, r, s):
    ur, vr = find(u, s), find(v, s)
    if ur != vr:
        if r[ur] > r[vr]:
            s[vr] = ur
        elif r[vr] > r[ur]:
            s[ur] = vr
        else:
            s[vr] = ur
            r[ur] += 1


def get_graph_size_based_on_edges(edges):
    edge_with_biggest_vertex = max(edges, key=lambda x: max(x[0], x[1]))
    biggest_vertex = max(edge_with_biggest_vertex[0], edge_with_biggest_vertex[1])
    return biggest_vertex + 1  # because vertices are indexed from 0


graph = [
    [1, 2, 3],
    [2, 3, 2],
    [2, 4, 7],
    [1, 3, 5],
    [1, 5, 9],
    [5, 4, 6]
]

print(kruskal_algorithm(graph))
