from zad7testy import runtests
def maze(L):
    n = len(L)
    F = [[[-1, -1, -1] for _ in range(n)] for _ in range(n)]
    F[0][0] = [0, 0, 0]
    for c in range(n):
        for r in range(n):
            F[r][c][0] = max(F[r][c - 1]) + 1 if c - 1 >= 0 and max(F[r][c-1]) != -1 and L[r][c] != "#" else -1
            F[r][c][1] = max(F[r - 1][c]) + 1 if r - 1 >= 0 and max(F[r-1][c]) != -1 and L[r][c] != "#" else -1
        for r in range(n - 1, -1, -1):
            if c == 0 and r == 0:
                continue
            F[r][c][2] = max(F[r + 1][c][0], F[r+1][c][2]) + 1 if r + 1 < n and \
                            (F[r+1][c][0] != -1 or F[r+1][c][2] != -1) and L[r][c] != "#" else -1
    return max(F[n - 1][n - 1])


runtests(maze, all_tests=True)