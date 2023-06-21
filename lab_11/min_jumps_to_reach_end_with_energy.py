def f(T):
    n = len(T)
    total = sum(T)
    F = [[float("inf") for _ in range(total+1)] for _ in range(n)]
    F[0][T[0]] = 0
    for i in range(n):
        for e in range(total+1):
            for k in range(1, i+1):
                if 0 <= k+e-T[i] <= total:
                    F[i][e] = min(F[i][e], F[i-k][k+e-T[i]] + 1)
    return min(F[n-1])


print(f([5, 5, 0, 0, 0, 0, 0, 0, 0, 0]))
