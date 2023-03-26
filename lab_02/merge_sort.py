def merge_sort(array):
    length = len(array)
    if length > 1:
        middle = length // 2
        left = array[:middle]
        right = array[middle:]
        merge_sort(left)
        merge_sort(right)
        merge(array, left, right)


def merge(array, left, right):
    len_l = len(left)
    len_r = len(right)
    index_left = 0
    index_right = 0
    index_array = 0

    while index_left < len_l and index_right < len_r:
        if left[index_left] <= right[index_right]:
            array[index_array] = left[index_left]
            index_left += 1
        else:
            array[index_array] = right[index_right]
            index_right += 1
        index_array += 1

    while index_left < len_l:
        array[index_array] = left[index_left]
        index_left += 1
        index_array += 1

    while index_right < len_r:
        array[index_array] = right[index_right]
        index_right += 1
        index_array += 1


test_array = [5, 3, 4, 6, 7, 1, 2, 2]
merge_sort(test_array)
print(test_array)
