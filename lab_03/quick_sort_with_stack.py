def quick_sort(array: list):
    length = len(array)
    stack = [(0, 0) for _ in range(length)]
    top = 0
    stack[top] = (0, length - 1)
    top += 1
    while top > 0:
        start, end = stack[top - 1]
        top -= 1
        pivot = partition(array, start, end)
        if start < pivot - 1:
            stack[top] = (start, pivot - 1)
            top += 1
        if end > pivot + 1:
            stack[top] = (pivot+1, end)
            top += 1


def partition(array, start, end):
    pivot = array[end]
    i = start
    for j in range(start, end):
        if pivot >= array[j]:
            array[j], array[i] = array[i], array[j]
            i += 1
    array[end], array[i] = array[i], array[end]
    return i


test_array = [5, 3, 4, 6, 7, 1, 2]
quick_sort(test_array)
print(test_array)
