def left(i):
    return 2 * i + 1
def right(i):
    return 2 * i + 2
def parent(i):
    return (i - 1) // 2


def min_heapify(array, i, n):
    l = left(i)
    r = right(i)
    smallest = i
    if l < n and array[l][0] < array[smallest][0]:
        smallest = l
    if r < n and array[r][0] < array[smallest][0]:
        smallest = r
    if smallest != i:
        array[i], array[smallest] = array[smallest], array[i]
        min_heapify(array, smallest, n)

def build_heap(array):
    n = len(array)
    for i in range(parent(n-1), -1, -1):
        min_heapify(array, i, n)

def merge_k_sorted_arrays(arrays, k, n):
    output = [0 for _ in range(k*n)]
    min_heap = [(arrays[i][0], i, 0) for i in range(k)]
    build_heap(min_heap)
    for i in range(n*k):
        s = min_heap[0]
        output[i] = s[0]
        if s[2] < n:
            min_heap[0] = (arrays[s[1]][s[2]], s[1], s[2] + 1)
            min_heapify(min_heap, 0, len(min_heap))
        else:
            min_heap[0] = (9999, s[1], s[2])
            min_heapify(min_heap, 0, len(min_heap))
    return output


test = [[3, 4, 5, 7, 9, 10, 11], [1, 3, 4, 5, 6, 8, 9], [2, 3, 4, 5, 8, 13, 14]]
print(merge_k_sorted_arrays(test, 3, 7))
