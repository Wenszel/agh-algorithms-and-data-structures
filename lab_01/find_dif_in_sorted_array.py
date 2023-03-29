def linear(array: list[int], x: int):
    i = 0
    j = 1
    while j < len(array) and array[j] - array[i] != x:
        if array[j] - array[i] > x:
            i += 1
        if array[j] - array[i] < x:
            j += 1
    return array[i], array[j]


print(linear([1, 2, 7, 9, 13, 22], 4))