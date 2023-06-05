def knapsack_double(P, W, w):
    n = len(P)
    F = [[0 for _ in range(w + 1)] for _ in range(n + 1)]
    for i in range(n + 1):
        for j in range(w + 1):
            if j == 0 or i == 0:
                F[i][j] = 0
            elif j - W[i-1] >= 0:
                F[i][j] = max(F[i-1][j], F[i-1][j-W[i-1]] + P[i-1])
            else:
                F[i][j] = F[i-1][j]
    return F[n][w]


profit = [1, 2, 3]
weight = [3, 5, 1]
max_weight = 4
print(knapsack_double(profit, weight, max_weight))
