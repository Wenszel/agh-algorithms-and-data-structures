from egzP6atesty import runtests 


def cmp_strings(s1, s2) -> bool:
    n = len(s1)
    m = len(s2)
    if n < m:
        return True
    if n > m:
        return False
    if n == m:
        s1_letters = 0
        s2_letters = 0
        for i in range(n):
            if s1[i].isalpha():
                s1_letters += 1
            if s2[i].isalpha():
                s2_letters += 1
        if s1_letters == s2_letters:
            return n <= m
        else:
            return s1_letters <= s2_letters

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
        if cmp_strings(pivot, array[j]):
            array[i], array[j] = array[j], array[i]
            i += 1
    array[end], array[i] = array[i], array[end]
    return i


def google ( H, s ):
    return quick_select(H, 0, len(H) - 1, s-1)


runtests ( google, all_tests=True )