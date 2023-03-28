def parent(i): return (i-1) // 2
def left(i): return 2 * i + 1
def right(i): return 2 * i + 2


def build_heap(array):
    n = len(array)
    for i in range(parent(n-1), -1, -1):
        heapify(array, i, n)


def heapify(array, i, n):
    maximum = i
    l = left(i)
    r = right(i)
    if l < n and array[l] > array[maximum]:
        maximum = l
    if r < n and array[r] > array[maximum]:
        maximum = r
    if maximum != i:
        array[i], array[maximum] = array[maximum], array[i]
        heapify(array, maximum, n)

def heapify_parent(array, i):
    p = parent(i)
    while p >= 0 and array[p] < array[i]:
        array[p], array[i] = array[i], array[p]
        i = p
        p = parent(i)

def insert(heap, value):
    heap.append(value)
    heapify_parent(heap, len(heap) - 1)


test_array = [1, 4, 2, 7, 8, 5, 3]
build_heap(test_array)
print(test_array)
insert(test_array, 10)
print(test_array)
insert(test_array, 6)
print(test_array)

