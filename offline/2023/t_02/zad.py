from zad2testy import runtests

def heapify(array, i, n):
    left = 2 * i + 1
    right = 2 * i + 2
    largest = i
    if left < n and array[left] > array[largest]:
        largest = left
    if right < n and array[right] > array[largest]:
        largest = right
    if largest != i:
        array[i], array[largest] = array[largest], array[i]
        heapify(array, largest, n)


def heap_sort(array):
    length = len(array)
    build_heap(array)
    output = 0
    melt = 0
    for i in range(length-1, 0, -1):
        array[0], array[i] = array[i], array[0]
        if array[i] - melt < 0:
            break
        output += array[i] - melt
        melt += 1
        heapify(array, 0, i)
    return output


def build_heap(array):
    length = len(array)
    for i in range((length - 2) // 2, -1, -1):
        heapify(array, i, length)


def snow(S):
    return heap_sort(S)


runtests( snow, all_tests = False )