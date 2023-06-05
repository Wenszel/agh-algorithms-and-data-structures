# https://www.geeksforgeeks.org/longest-monotonically-increasing-subsequence-size-n-log-n/
def binary_search(A, val):
    left = 0
    right = len(A) - 1
    while left <= right:
        mid = (left + right) // 2
        if val > A[mid]:
            left = mid + 1
        else:
            right = mid - 1
    return left

def lis(A):
    n = len(A)
    tail_table = [A[0]]
    for i in range(1, n):
        if A[i] < tail_table[0]:
            tail_table[0] = A[i]
        elif A[i] > tail_table[-1]:
            tail_table.append(A[i])
        else:
            index = binary_search(tail_table, A[i])
            tail_table[index] = A[i]
    return tail_table


print(lis([2, 5, 3, 7, 11, 8, 10, 13, 6]))
