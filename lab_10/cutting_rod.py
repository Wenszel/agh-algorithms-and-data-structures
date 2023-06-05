# https://www.geeksforgeeks.org/cutting-a-rod-dp-13/
def cutting_rod(P, length):
    F = [0 for _ in range(length+1)]
    F[0] = 0
    for i in range(length):
        F[i+1] = P[i]
    for i in range(length+1):
        for j in range(i):
            F[i] = max(F[i], F[i-j] + F[j])
    return F


length = 10
L = [i for i in range(1, length + 1)]  # possible Lengths of cuts
P = [1, 3, 5, 8, 9, 10, 17, 17, 20, 24]  # Price for each length
print(cutting_rod(P, length))
