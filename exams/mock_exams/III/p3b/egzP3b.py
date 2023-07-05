from egzP3btesty import runtests 

def lufthansa ( G ):
    def graph_to_edges(G):
        edges = []
        for i in range(n):
            for neighbour, weight in G[i]:
                if neighbour > i:
                    edges.append((i, neighbour, weight)) 
        return edges  
    
    def biggest_edge_outside_MST(edges, MST):
        for i in range(len(MST)):
            if edges[i][2] != MST[i][2]:
                return edges[i][2]
        return edges[len(MST)][2]
    
    def kruskal_algorithm(G):
        def find(u, s):
            if s[u] == u:
                return u
            s[u] = find(s[u], s)
            return s[u]
        
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
                    
        sets = list(range(n))
        ranks = [0] * n

        MST = []
        
        for u, v, t in G:
            if find(u, sets) != find(v, sets):
                union(u, v, ranks, sets)
                MST.append((u, v, t))
                
        return MST
    
    n = len(G)
    edges = graph_to_edges(G)
    edges.sort(key=lambda x: x[2], reverse=True)
    MST = kruskal_algorithm(edges)
    weight_of_graph = sum([t for _, _, t in edges])
    weight_of_mst = sum([t for _, _, t in MST])
    edge = biggest_edge_outside_MST(edges, MST)
    return weight_of_graph - (weight_of_mst + edge) 

        
runtests ( lufthansa, all_tests=True)