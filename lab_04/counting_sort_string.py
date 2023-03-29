def counting_sort(A):
    n = len(A)
    r = 26  # quantity of letters a-z
    B = [0] * n
    C = [0] * 26

    for i in range(n):
        C[get_index(A[i])] += 1

    for i in range(1, r):
        C[i] += C[i-1]

    for i in range(n - 1, -1, -1):
        B[C[get_index(A[i])] - 1] = A[i]
        C[get_index(A[i])] -= 1

    for i in range(n):
        A[i] = B[i]

def get_index(letter):
    max_index = 25
    z_index = ord("z")
    letter_index = ord(letter)
    return max_index - (z_index - letter_index)


test_string = "oiahfnbfnbzvwiofazaanfza"
test_array = list(test_string)
counting_sort(test_array)
print("".join(test_array))

