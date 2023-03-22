def partition_hoare(array, low, height):
    pivot = array[low]
    i = low - 1
    j = height + 1
    while True:
        i += 1
        while array[i] < pivot:
            i += 1
        j -= 1
        while array[j] > pivot:
            j -= 1
        if i >= j:
            return j
        array[i], array[j] = array[j], array[i]


def quick_sort(array, start, end):
    if start < end:
        pivot = partition_hoare(array, start, end)
        quick_sort(array, start, pivot)
        quick_sort(array, pivot + 1, end)


test_array = [5, 3, 4, 6, 7, 1, 2]
quick_sort(test_array, 0, len(test_array) - 1)
print(test_array)
