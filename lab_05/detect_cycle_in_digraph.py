def is_cycle(G):
    def dfs_visit(j):
        visited[j] = True
        current_recursion[j] = True
        for neighbour in G[j]:
            if not visited[neighbour]:
                if dfs_visit(neighbour):
                    return True
            if current_recursion[neighbour]:
                return True
        current_recursion[j] = False
        return False

    n = len(G)
    visited = [False] * n
    current_recursion = [False] * n
    for i in range(len(G)):
        if not visited[i]:
            if dfs_visit(i):
                return True
    return False


adjacency_lists = [
    # Graph 1 - Cycle
    [[1], [2], [0]],
    # Graph 2 -  No cycle
    [[1, 2], [], []],
    # Graph 3 - Cycle
    [[1, 2], [2], [0]],
    # Graph 4 - No cycle
    [[1, 2], [3], [4], [], []],
    # Graph 5 - Cycle
    [[1, 2], [2, 3], [3, 4], [4], [0]],
    # Graph 6 - No cycle
    [[1, 2], [3], [4], [2], []],
    # Graph 7 - Cycle
    [[1], [2], [3], [0]],
    # Graph 8 - No cycle
    [[1, 2], [2], [3], []],
    # Graph 9 - No cycle
    [[1], [2], [3], []],
    # Graph 10 - Cycle
    [[1], [2], [3], [4], [0]]
]

answers = [True, False, True, False, True, False, True, False, False, True]
for index in range(len(adjacency_lists)):
    print(index+1, "Algorithm: ", is_cycle(adjacency_lists[index]), " \tCorrect: ", answers[index])




