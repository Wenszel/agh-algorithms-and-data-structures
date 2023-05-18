# Determine whether a universal sink exists in a directed graph.
# A universal sink is a vertex which has no edge emanating from it,
# and all other vertices have an edge towards the sink.
def is_universal_sink(G):
    possible_sinks = []
    for i in range(len(G)):
        if len(G[i]) == 0:
            possible_sinks.append(i)
    if len(possible_sinks) == 0:
        return False
    for s in possible_sinks:
        for i in range(len(G)):
            if i != s:
                if s not in G[i]:
                    return False
    return True


graph1 = [
    [1, 2, 3, 5],
    [5],
    [5],
    [5],
    [5],
    []
]
graph2 = [
    [1, 2, 3],
    [4],
    [4],
    [4, 5],
    [6],
    [6, 7],
    [],
    []
]
graph3 = [
    [1, 2, 3, 4],
    [5, 6],
    [3, 7],
    [2, 4],
    [5, 7],
    [0, 6],
    [2, 7],
    [4, 6]
]

list_of_graphs = [graph1, graph2, graph3]
for graph in list_of_graphs:
    print(is_universal_sink(graph))
