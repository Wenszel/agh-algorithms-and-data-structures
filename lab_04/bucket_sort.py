def bucket_sort(x):
    arr = []
    n = 10

    for i in range(n):
        arr.append([])

    for j in x:
        index_b = int(n * j)
        arr[index_b].append(j)

    for i in range(n):
        arr[i] = insertion_sort(arr[i])

    k = 0
    for i in range(n):
        for j in range(len(arr[i])):
            x[k] = arr[i][j]
            k += 1
    return x


def insertion_sort(A):
    for i in range(1, len(A)):
        key = A[i]
        j = i - 1
        while j >= 0 and A[j] > key:
            A[j + 1] = A[j]
            j -= 1
        A[j + 1] = key
    return A

