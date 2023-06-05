def calc_cost(A, i, j, memo):
    if i == j:
        return 0
    total = float('inf')
    for k in range(i, j):
        if (i, k) in memo:
            s1 = memo[(i, k)]
        else:
            s1 = calc_cost(A, i, k, memo)
            memo[(i, k)] = s1
        if (k + 1, j) in memo:
            s2 = memo[(k + 1, j)]
        else:
            s2 = calc_cost(A, k + 1, j, memo)
            memo[(k + 1, j)] = s2
        s = s1 + s2 + (A[i-1] * A[k] * A[j])
        total = min(total, s)
    return total

def matrix_chain_multiplication(A):
    return calc_cost(A, 1, len(A) - 1, memo={})


matrices = [40, 20, 30, 10, 30]
print(matrix_chain_multiplication(matrices))
