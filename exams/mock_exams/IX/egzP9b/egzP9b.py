from egzP9btesty import runtests
def find_eulerian_cycle(graph):
    stack = []
    cycle = []
    stack.append(0)

    while stack:
        current_vertex = stack[-1]
        if graph[current_vertex]:
            stack.append(graph[current_vertex].pop())
        else:
            cycle.append(stack.pop())
    return cycle[::-1]



def dyrektor( G, R ):
    n = len(G)
    L = [[] for _ in range(n)]
    for i in range(n):
        for j in G[i]:
            if j not in R[i]:
                L[i].append(j)
            else:
                R[i].remove(j)
    
    return find_eulerian_cycle(L)
	
 

runtests(dyrektor, all_tests=True)
