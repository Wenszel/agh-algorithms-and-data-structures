def quick_select(array, left, right, k):
    if left == right:
        return array[left]
    p_index = partition(array, left, right)
    if k == p_index:
        return array[p_index]
    if k < p_index:
        return quick_select(array, left, p_index - 1, k)
    if k > p_index:
        return quick_select(array, p_index + 1, right, k)


def partition(array, start, end):
    pivot = array[end]
    i = start
    for j in range(start, end):
        if pivot >= array[j]:
            array[i], array[j] = array[j], array[i]
            i += 1
    array[end], array[i] = array[i], array[end]
    return i


k = 5
print(quick_select([5, 3, 4, 6, 7, 1, 2, 2], 0, 7, k - 1))
