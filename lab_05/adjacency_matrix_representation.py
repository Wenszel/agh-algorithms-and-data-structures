class Graph:
    def __init__(self, v, e, directed=False):
        self.v = v
        self.e = e
        self.directed = directed
        self.m = self.create_adjacency_matrix()

    def create_adjacency_matrix(self):
        n = len(self.v)
        matrix = [[False for _ in range(n)] for _ in range(n)]
        for edge in self.e:
            matrix[edge[0]][edge[1]] = True
            if not self.directed:
                matrix[edge[1]][edge[0]] = True
        return matrix

    def print_matrix(self):
        print("Adjacency matrix:")
        n = len(self.v)
        print("X", end=" ")
        for i in range(n):
            print("{}{}{}".format('\033[1m', i, '\033[0m'), end=" ")
        print()
        index = 0
        for i in range(len(self.m)):
            print("{}{}{}".format('\033[1m', index, '\033[0m'), end=" ")
            index += 1
            for j in range(len(self.m[i])):
                if j == i:
                    print("-", end=" ")
                else:
                    if self.m[i][j]:
                        print(1, end=" ")
                    else:
                        print(0, end=" ")
            print()
