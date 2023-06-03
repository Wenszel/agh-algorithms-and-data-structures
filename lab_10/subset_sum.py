def is_subset_sum(A, v):
    n = len(A)
    F = [[False for _ in range(n)] for _ in range(v+1)]
    for i in range(n):
        F[0][i] = True
    for val in range(v+1):
        for i in range(n):
            if val - A[i] >= 0:
                F[val][i] = F[val-A[i]][i - 1] or F[val][i -1]
    return F[v][n - 1]


print(is_subset_sum([3, 5, 0, 0, 17, 3, 5, 2, 7, 8], 10))
print(is_subset_sum([3, 5, 0, 0, 17, 3, 5, 2, 7, 8], 1))
