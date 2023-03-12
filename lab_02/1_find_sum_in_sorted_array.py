def linear(a, x):
    i = 0
    j = len(a) - 1
    while a[i] + a[j] != x:
        if i == j:
            return False
        if a[i] + a[j] > x:
            j -= 1
        if a[i] + a[j] < x:
            i += 1
    return a[i], a[j]


print(linear([1, 3, 5, 9, 13, 15, 28], 22))
