from lab_05 import adjacency_list_representation
from topological_sort import topological_sort
from find_scc_in_graph import find_scc_in_graph


# A vertex v in a directed graph is called
# a mother vertex if every other vertex can be
# reached by a directed path starting from v.
# Give an algorithm that, for a given graph,
# determines whether G has a good start; a list of neighbourhoods
def shrink_graph(graph, dag):
    n = len(dag)
    edges = []
    # for every set of vertices in dag
    for vertices in range(n):
        # for every vertex in that set
        for vertex in range(len(dag[vertices])):
            # for every neighbour of that vertex
            for neighbour in graph.l[dag[vertices][vertex]]:
                # for every other set of vertices in dag
                for i in range(len(dag)):
                    # if neighbour is in that set
                    if neighbour in dag[i] and i != vertices:
                        if (vertices, i) not in edges:
                            edges.append((vertices, i))
    return adjacency_list_representation.Graph([i for i in range(len(dag))], edges, True)


def find_good_start():
    vertices = [i for i in range(6)]
    edges = [(1, 0), (1, 2), (1, 3), (1, 4), (1, 5), (2, 3)]
    graph = adjacency_list_representation.Graph(vertices, edges, True)
    dag = find_scc_in_graph(graph, edges)
    print("dag:", dag)
    new_graph = shrink_graph(graph, dag)
    topological_sorted = topological_sort(new_graph.l)
    print("topological sorted:", topological_sorted)
    # Graph has a good start if scc element in dag has edges to other dag vertices
    if len(new_graph.l[topological_sort(new_graph.l)[0]]) == len(dag)-1:
        print("good start vertices:", dag[topological_sort(new_graph.l)[0]])
    else:
        print("no good start vertices")


find_good_start()
