def insertion_sort(array: list[int]) -> list:
    for i in range(1, len(array)):
        key: int = array[i]
        j: int = i-1
        while j >= 0 and key < array[j]:
            array[j+1] = array[j]
            j -= 1
        array[j + 1] = key
    return array


print(insertion_sort([1, 5, 3, 2, 7]))
