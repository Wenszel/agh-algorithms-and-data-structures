from math import log10
def radix_sort(A):
    n = len(A)
    max_length = 0
    for i in A:
        max_length = max(max_length, int(log10(i)) + 1)
    for i in range(1, max_length+1):
        print(A)
        counting_sort(A, n, 10 ** i)


def get_digit(number, power):
    return int(((number % power) - (number % (power/10))) / (power / 10))


def counting_sort(A, n, power):
    B = [0] * n
    C = [0] * 10
    for i in range(n):
        C[get_digit(A[i], power)] += 1
    for i in range(1, 10):
        C[i] += C[i-1]
    for i in range(n-1, -1, -1):
        B[C[get_digit(A[i], power)] - 1] = A[i]
        C[get_digit(A[i], power)] -= 1
    for i in range(n):
        A[i] = B[i]


array = [100, 432, 455, 123, 555, 876, 123, 111, 999]
radix_sort(array)
print(array)
