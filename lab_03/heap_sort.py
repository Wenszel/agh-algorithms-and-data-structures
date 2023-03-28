def left(i):
    return i * 2 + 1
def right(i):
    return i * 2 + 2
def parent(i):
    return (i - 1)//2

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

def heap_sort(array):
    n = len(array)
    build_heap(array)
    for i in range(n-1, 0, -1):
        array[0], array[i] = array[i], array[0]
        heapify(array, 0, i)


test_array = [5, 3, 4, 6, 7, 1, 2]
heap_sort(test_array)
print(test_array)
