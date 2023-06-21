def prom(P, l1, l2):
    n = len(P)
    F = [[[False for _ in range(l2 + 1)] for _ in range(l1 + 1)] for _ in range(n)]
    if P[0] <= l2:
        F[0][0][P[0]] = True
    if P[0] <= l1:
        F[0][P[0]][0] = True

    for i in range(1, n):
        for g in range(l1 + 1):
            for d in range(l2 + 1):
                if g < P[i] and d < P[i]:
                    F[i][g][d] = False
                elif g < P[i]:
                    F[i][g][d] = F[i - 1][g][d - P[i]]
                elif d < P[i]:
                    F[i][g][d] = F[i - 1][g - P[i]][d]
                else:
                    F[i][g][d] = F[i - 1][g - P[i]][d] or F[i - 1][g][d - P[i]]

    maximum_i = 0
    for i in range(n):
        for g in range(l1 + 1):
            for d in range(l2 + 1):
                if F[i][g][d]:
                    maximum_i = max(maximum_i, i)
                    break
    return maximum_i
