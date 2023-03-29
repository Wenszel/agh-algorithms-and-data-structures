def selection_sort(array: list[int]):
    for i in range(len(array) - 1):
        minimum = i
        for j in range(i, len(array)):
            if array[minimum] > array[j]:
                minimum = j
        array[i], array[minimum] = array[minimum], array[i]
    return array


print(selection_sort([1, 5, 4, 3, 7, 2]))
