from zad1testy import runtests

def ceasar(s):
    longest = 1
    for i in range(1, len(s)-1):
        if i-longest >= 0 and i+longest < len(s) and s[i+longest] == s[i-longest]:
            j = 1
            while i-j >= 0 and i+j < len(s) and s[i+j] == s[i-j]:
                j += 1
            if longest < j:
                longest = j
    return longest * 2 - 1

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( ceasar , all_tests = False )
