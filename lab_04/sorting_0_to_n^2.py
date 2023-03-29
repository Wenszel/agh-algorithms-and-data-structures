def counting_sort(A, n, exp):
    B = [0] * n
    C = [0] * n
    for i in range(n):
        C[get_index(A[i], exp, n)] += 1
    for i in range(1, n):
        C[i] += C[i-1]
    for i in range(n-1, -1, -1):
        B[C[get_index(A[i], exp, n)] - 1] = A[i]
        C[get_index(A[i], exp, n)] -= 1
    for i in range(n):
        A[i] = B[i]

def get_index(num, exp, n):
    return (num // exp) % n
def sort(A, n):
    counting_sort(A, n, 1)
    counting_sort(A, n, n)


test_array = [0, 10, 13, 12, 7]
sort(test_array, len(test_array))
print(test_array)
