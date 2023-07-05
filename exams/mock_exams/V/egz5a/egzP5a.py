from egzP5atesty import runtests 

def inwestor ( T ):
    n = len(T)
    output = 0
    F = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        F[i][i] = T[i]
    output = 0
    for a in range(n):
        for b in range(a+1, n):
            length = b - a + 1
            profit_per_entity = F[a][b-1] / (length - 1)
            if profit_per_entity * (n - a) < output:
                break
            if profit_per_entity > T[b]: 
                F[a][b] = T[b] * length
            else:
                F[a][b] = profit_per_entity*length
            output = max(F[a][b], output)
    return output

runtests ( inwestor, all_tests=True )