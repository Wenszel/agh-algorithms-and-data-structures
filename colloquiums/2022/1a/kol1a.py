from kol1atesty import runtests

def string_score(string):
    suma = 0
    for letter in string:
        suma += ord(letter)
    return suma


def is_equivalent(s1, s2):
    return s1 == s2 or s1 == s2[::-1]


def qs_len(array, p, l):
    top = 0
    stos = [0 for _ in range(len(array))]
    stos[top] = p, l
    top += 1
    while top > 0:
        start, end = stos[top - 1]
        top -= 1
        s = partition(array, start, end)
        if s - 1 > start:
            stos[top] = start, s - 1
            top += 1
        if s + 1 < end:
            stos[top] = s + 1, end
            top += 1


def partition(array, start, end):
    pivot = array[end]
    i = start
    for j in range(start, end):
        if len(array[j]) <= len(pivot) and not is_equivalent(array[j], pivot):
            array[i], array[j] = array[j], array[i]
            i += 1
    array[i], array[end] = array[end], array[i]
    return i


def g(T):
    # tu prosze wpisac wlasna implementacje
    qs_len(T, 0, len(T)-1)
    biggest = 0
    streak = 1
    for i in range(len(T)-1):
        if is_equivalent(T[i], T[i+1]):
            streak += 1
        else:
            if biggest < streak:
                biggest = streak
            streak = 1
    return biggest


# Zamien all_tests=False na all_tests=True zeby uruchomic wszystkie testy
runtests( g, all_tests=True )
