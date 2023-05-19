from math import log
# We have a given array [n][n] with exchange rates.
# The algorithm finds currency swap opportunities on which we can make money.
# Such opportunities are simply negative cycles, which we find using the Bellman-Ford algorithm
def currency_arbitrages(M, s):
    M = [[-log(val) for val in row] for row in M]
    n = len(M)
    distances = [float('inf')] * n
    parent = [-1] * n
    distances[s] = 0
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if distances[j] > distances[i] + M[i][j]:
                    parent[j] = i
                    distances[j] = distances[i] + M[i][j]
    output = []
    for i in range(n):
        for j in range(n):
            if distances[j] > distances[i] + M[i][j]:
                cycle = [j, i]
                while parent[i] not in cycle:
                    cycle.append(parent[i])
                    i = parent[i]
                cycle.append(parent[i])
                output.append(cycle[::-1])
    return output


matrix_of_rates = [
    [1, 0.23, 0.25, 16.43, 18.21, 4.94],
    [4.34, 1, 1.11, 71.40, 79.09, 21.44],
    [3.93, 0.90, 1, 64.52, 71.48, 19.37],
    [0.061, 0.014, 0.015, 1, 1.11, 0.30],
    [0.055, 0.013, 0.014, 0.90, 1, 0.27],
    [0.20, 0.047, 0.052, 3.33, 3.69, 1],
]

currencies = ('PLN', 'EUR', 'USD', 'RUB', 'INR', 'MXN')
for l in currency_arbitrages(matrix_of_rates, 0):
    for index in l:
        print(currencies[index], end=" ")
    print("\n")
