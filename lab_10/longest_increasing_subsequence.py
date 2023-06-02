def lis(A):
    n = len(A)
    L = [1] * len(A)
    for i in range(1, n):
        for j in range(i):
            if A[j] < A[i]:
                L[i] = max(L[i], L[j] + 1)
    return max(L)


print(lis([3, 1, 8, 2, 5]))
print(lis([5, 2, 8, 6, 3, 6, 9, 5]))
