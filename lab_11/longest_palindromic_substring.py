def longest_palindromic_substring(S):
    n = len(S)
    F = [[0] * n for _ in range(n)]
    for i in range(n):
        F[i][i] = 1
    for length in range(2, n + 1):
        for i in range(0, n - length + 1):
            if is_palindrome(S, i, length):
                F[i][i + length - 1] = F[i + 1][i + length - 2] + 2
    maxi = -1
    a = -1
    for i in range(n):
        for j in range(n):
            if F[i][j] > maxi:
                maxi = F[i][j]
                a = i
    return S[a:a + maxi]


def is_palindrome(string, i, length):
    substring = string[i:i + length]
    reversed_substring = substring[::-1]
    return substring == reversed_substring
