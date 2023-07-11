from egzP6btesty import runtests 

def jump ( M ):
    a = set()
    curr_pos = (0, 0)
    a.add((0, 0))
    R = {
        'UL': (-1, 2), 
        'LU': (-2, 1), 
        'UR': (1, 2), 
        'RU': (2, 1),
        'LD': (-2, -1),
        'DL': (-1, -2), 
        'DR': (1, -2),
        'RD': (2, -1)
    }
    for i in M:
        x, y = R[i]
        curr_pos = curr_pos[0] + x, curr_pos[1] + y 
        if curr_pos in a:
            a.remove(curr_pos)
        else:
            a.add(curr_pos)
    return len(a)
    
runtests(jump, all_tests = True)