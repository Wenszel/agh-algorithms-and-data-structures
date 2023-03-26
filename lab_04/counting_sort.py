def counting_sort(A, r):
    n = len(A)
    B = [0] * n
    C = [0] * r
    for i in range(n):
        C[A[i]] += 1
    for i in range(1, r):
        C[i] += C[i-1]
    for i in range(n - 1, -1, -1):
        B[C[A[i]] - 1] = A[i]
        C[A[i]] -= 1
    for i in range(n):
        A[i] = B[i]


test_array = [5, 3, 4, 6, 7, 1, 2]
counting_sort(test_array, 8)
print(test_array)
