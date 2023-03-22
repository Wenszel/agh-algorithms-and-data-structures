def quick_sort(array, start, end):
    if start < end:
        pivot = partition(array, start, end)
        quick_sort(array, start, pivot - 1)
        quick_sort(array, pivot + 1, end)


def partition(array, low, high):
    pivot = array[high]
    i = low
    for j in range(low, high):
        if pivot >= array[j]:
            array[i], array[j] = array[j], array[i]
            i += 1
    array[high], array[i] = array[i], array[high]
    return i


test_array = [5, 3, 4, 6, 7, 1, 2]
quick_sort(test_array, 0, len(test_array) - 1)
print(test_array)
