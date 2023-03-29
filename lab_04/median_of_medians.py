def find_median(A, k):
    full_chunks = len(A) // 5
    chunks = [A[i: i+5] for i in range(0, full_chunks * 5, 5)]
    overflow = len(A) % 5
    if overflow > 0:
        chunks.append(A[full_chunks * 5: (full_chunks * 5) + overflow])
    for i in chunks:
        insertion_sort(i)
    medians = [chunk[len(chunk) // 2] for chunk in chunks]
    if len(medians) <= 5:
        pivot = insertion_sort(medians)[len(medians)//2]
    else:
        pivot = find_median(medians, len(medians) // 2)
    p = partition(A, pivot)
    if k == p:
        return pivot
    if k < p:
        return find_median(A[0:p], k)
    else:
        return find_median(A[p + 1:len(A)], k - p - 1)

def partition(arr, pivot):
    left = 0
    right = len(arr) - 1
    i = 0
    while i <= right:
        if arr[i] == pivot:
            i += 1
        elif arr[i] < pivot:
            arr[left], arr[i] = arr[i], arr[left]
            left += 1
            i += 1
        else:
            arr[right], arr[i] = arr[i], arr[right]
            right -= 1
    return left

def insertion_sort(array: list[int]) -> list:
    for i in range(1, len(array)):
        key: int = array[i]
        j: int = i-1
        while j >= 0 and key < array[j]:
            array[j+1] = array[j]
            j -= 1
        array[j + 1] = key
    return array


test_array = [25, 24, 33, 39, 3, 18, 19, 31, 23, 49, 45, 16, 1, 29, 40, 22, 15, 20, 24, 4, 13, 34]

print(find_median(test_array, len(test_array)//2))



