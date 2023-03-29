def find(a):
    if a[0] != 0:
        return 0
    i = 0
    while i + 1 < len(a):
        if a[i+1] - a[i] > 1:
            return a[i] + 1
        i += 1
    return a[i] + 1


print(find([0, 1, 2, 6, 9]))
print(find([4, 5, 10, 11]))
print(find([0, 1, 2, 3]))
print(find([0, 1, 2, 3, 4, 5, 6, 7, 10]))
