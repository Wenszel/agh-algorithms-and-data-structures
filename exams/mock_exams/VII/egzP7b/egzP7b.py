from egzP7btesty import runtests 
	
NOT_TAKEN = -1
TAKEN = 0
OVERTAKEN = 1

def ogrod( S, V ):
    n = len(S)
    m = len(V)
    output = 0
    for i in range(n):
        is_taken = [NOT_TAKEN for _ in range(m)]
        temp_output = 0
        for j in range(i+1, n):
            if is_taken[S[j]-1] == NOT_TAKEN:
                temp_output += V[S[j]-1]
                is_taken[S[j]-1] = TAKEN
                
            elif is_taken[S[j]-1] == TAKEN:
                temp_output -= V[S[j]-1]
                is_taken[S[j]-1] = OVERTAKEN
            output = max(output, temp_output)  
    return output
runtests(ogrod, all_tests = True)