def left(i): return 2 * i + 1
def right(i): return 2 * i + 2
def parent(i): return (i+1)//2
def heapify(A, i):
    while True:
        maxi = i
        l = left(i)
        r = right(i)
        if l < len(A) and A[l] > A[maxi]:
            maxi = l
        if r < len(A) and A[r] > A[maxi]:
            maxi = r
        if maxi != i:
            A[maxi], A[i] = A[i], A[maxi]
            i = maxi
        else:
            break


array = [16, 4, 10, 14, 7, 9, 3, 2, 8, 1]
heapify(array, 1)
print(array)
