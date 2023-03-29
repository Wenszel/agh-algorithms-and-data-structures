def find_min_and_max(array: list[int]):
    minimum = 999
    maximum = 0
    for i in range(0, len(array), 2):
        if array[i] >= array[i+1]:
            if array[i+1] < minimum:
                minimum = array[i+1]
            if array[i] > maximum:
                maximum = array[i]
        else:
            if array[i + 1] > maximum:
                maximum = array[i + 1]
            if array[i] < minimum:
                minimum = array[i]
    return minimum, maximum


print(find_min_and_max([1, 2, 4,3, 2, 6, 7, 10 ,0 ,13, 1, 2]))

