# There is a king on an n x m size chessboard located in position [0, 0].
# Count the unique paths by which king can reach position [n - 1, m - 1] by moving only down or right.
def chessboard(n, m):
    quantity_of_paths = [[1 for _ in range(m)] for _ in range(n)]
    for r in range(1, n):
        for c in range(1, m):
            quantity_of_paths[r][c] = quantity_of_paths[r-1][c] + quantity_of_paths[r][c-1]
    return quantity_of_paths[n - 1][m - 1]


print(chessboard(18, 18))
