from zad1testy import runtests


def merge(array, left, right):
    l = r = a = 0
    while l < len(left) and r < len(right):
        if left[l][0] <= right[r][0]:
            array[a] = left[l]
            l += 1
        else:
            array[a] = right[r]
            r += 1
        a += 1
    while l < len(left):
        array[a] = left[l]
        l += 1
        a += 1
    while r < len(right):
        array[a] = right[r]
        r += 1
        a += 1


def merge_sort(array):
    if len(array) > 1:
        middle = len(array) // 2
        left = array[:middle]
        right = array[middle:]
        merge_sort(left)
        merge_sort(right)
        merge(array, left, right)


def chaos_index(T):
    n = len(T)
    t = [(T[i], i) for i in range(n)]
    merge_sort(t)
    k = 0
    for i in range(n):
        k = max(k, abs(i - t[i][1]))
    return k


runtests(chaos_index)
