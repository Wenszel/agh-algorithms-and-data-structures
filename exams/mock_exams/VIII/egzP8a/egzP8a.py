from egzP8atesty import runtests 

def reklamy ( T, S, o ):
    n = len(T)
    output = 0
    A = [(T[i][0], T[i][1], S[i]) for i in range(n)]
    A.sort(key= lambda x: (x[0], x[1], -x[2]))
    for i in range(n):
        for j in range(n):
            if i == j:
                output = max(output, A[i][2])
            else:
                first_range = (A[i][0], A[i][1])
                second_range = (A[j][0], A[j][1])
                if first_range[0] > second_range[0]:
                    first_range, second_range = second_range, first_range
                if first_range[1] < second_range[0]:
                    output = max(output, A[i][2]+A[j][2])
    
    return output

runtests ( reklamy, all_tests=True )