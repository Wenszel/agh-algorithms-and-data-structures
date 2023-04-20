from zad3testy import runtests
# Wiktor Smaga
# Algorytm odwraca slowa aby wszystkie zaczynaly sie od litery mniejszej niz konczyly
# nastepnie sortuje slowa alfabetycznie i tak zeby obok siebie byly slowa rowne sobie
# Algorytm nastepnie zlicza ile takich odpowiadajacych sobie elementow sie pojawilo
# zlozonosc: O(N+ NlogN)   N - ilosc slow


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
        if array[j] <= pivot and not is_equivalent(array[j], pivot):
            array[i], array[j] = array[j], array[i]
            i += 1
    array[i], array[end] = array[end], array[i]
    return i


def strong_string(T):
    for i in range(len(T) - 1):
        if T[i][0] > T[i][-1]:
            T[i] = T[i][::-1]
    qs_len(T, 0, len(T) - 1)
    biggest = 0
    streak = 1
    for i in range(len(T) - 1):
        if is_equivalent(T[i], T[i + 1]):
            streak += 1
        else:
            if biggest < streak:
                biggest = streak
            streak = 1
    return biggest


runtests( strong_string, all_tests=True)
