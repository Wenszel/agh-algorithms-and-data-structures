class Graph:
    def __init__(self, v, e, directed=False):
        self.v = v
        self.e = e
        self.directed = directed
        self.l = self.create_adjacency_list()

    def create_adjacency_list(self):
        n = len(self.v)
        adj_list = [[] for _ in range(n)]
        for edge in self.e:
            adj_list[edge[0]].append(edge[1])
            if not self.directed:
                adj_list[edge[1]].append(edge[0])
        return adj_list

    def print_list(self):
        for i in range(len(self.l)):
            print(i, "->", self.l[i])
