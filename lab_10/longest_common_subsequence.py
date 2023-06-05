def lcs(s1, s2):
    n = len(s1)
    m = len(s2)
    F = [[0 for _ in range(m+1)] for _ in range(n+1)]
    for i in range(n+1):
        for j in range(m+1):
            if i == 0 or j == 0:
                F[i][j] = 0
            elif s1[i-1] == s2[j-1]:
                F[i][j] = F[i-1][j-1] + 1
            else:
                F[i][j] = max(F[i-1][j], F[i][j-1])
    return F[n][m]

def print_lcs(s1, s2, lcs_length):
    p1 = len(s1)
    p2 = len(s2)
    output = []
    while lcs_length > 0:
        if s1[p1-1] == s2[p2-1]:
            output.insert(0, s1[p1-1])
            p1 -= 1
            p2 -= 1
            lcs_length -= 1
        elif s1[p1-1] > s2[p2-1]:
            p1 -= 1
        elif s1[p1-1] < s2[p2-1]:
            p2 -= 1
    print("".join(output))


S1 = list("AGGTAB")
S2 = list("GXTXAYB")
print(lcs(S1, S2))
print_lcs(S1, S2, lcs(S1, S2))

