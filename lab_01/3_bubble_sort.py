def bubble_sort(array: list[int]):
    for i in range(len(array)):
        key = i
        while key + 1 < len(array) and array[key] > array[key+1]:
            array[key], array[key+1] = array[key+1], array[key]
            key += 1
    return array


print(bubble_sort([1, 5, 3, 4, 6]))
