# Given array T = [c0, c1, ..., cn] representing forest
# c(i) - profit earned by cutting "i" tree
# Calculate maximum profit that can be reached but two trees next to each other can't be cut
def cutting_trees(T):
    # F(i, boolean) - maximum profit in sub forest contains trees from index 0 to i
    # DP table was replaced by two variables to save memory because we only look back by 1 element
    n = len(T)
    # F[0][0], F[0][1] = 0, T[0]
    not_took, took = 0, T[0]
    for i in range(1, n):
        # F[i][0] = max(F[i-1][0], F[i-1][1])
        # F[i][1] = F[i-1][0] + T[i]
        not_took, took = max(not_took, took), not_took + T[i]
    return max(not_took, took)


forests = [
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    [1, 3, 7, 5, 6, 6, 2],
    [15, 3, 3, 15]
]

for forest in forests:
    print(cutting_trees(forest))
