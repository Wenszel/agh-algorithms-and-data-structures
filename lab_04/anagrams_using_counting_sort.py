import numpy as np
def anagram(a, b):
    z_code = ord("z")
    a_code = ord("a")
    len_a = len(a)
    len_b = len(b)
    if len_a != len_b:
        return False
    A = [0 for _ in range(z_code - a_code)]
    B = [0 for _ in range(z_code - a_code)]
    for i in range(len_a):
        A[ord(a[i]) - a_code] += 1
        B[ord(b[i]) - a_code] += 1
    return A == B


c = np.empty(2**21)
def anagram_numpy(a, b):
    na = len(a)
    nb = len(b)
    if na != nb:
        return False
    for i in range(na):
        c[ord(a[i])] = 0
        c[ord(a[i])] = 0
    for i in range(na):
        c[ord(a[i])] += 1
        c[ord(b[i])] -= 1
    for i in range(na):
        if c[ord(a[i])] != 0 or c[ord(b[i])] != 0:
            return False
    return True


print(anagram_numpy("abcdef", "feabcd"))
print(anagram("abcdef", "feabcd"))
print(anagram_numpy("abcdefg", "feabcde"))
print(anagram("abcdefg", "feabcde"))
