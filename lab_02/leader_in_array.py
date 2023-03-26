from math import floor

# Leader - an element of an array that occurs more than n/2 times in it
def find(a):
    n = len(a)
    leader = a[0]
    points = 1
    for i in range(1, len(a)):
        if leader != a[i]:
            points -= 1
        else:
            points += 1
        if points < 0:
            points = 1
            leader = a[i]
    if count_quantity(a, leader) >= (n/2) + 1:
        return leader
    return None


# Leader - an element of an array that occurs more than n/3 times in it
def find_1_3(a):
    n = len(a)
    leader = a[0]
    points = 1
    for i in range(1, len(a)):
        print(points, leader)
        if leader != a[i]:
            points -= 1
        else:
            points += 1
        if points < -floor(n/3):
            points = 1
            leader = a[i]
    if count_quantity(a, leader) >= (n / 3) + 1:
        return leader
    return None


def count_quantity(a, leader):
    quantity = 0
    for i in range(len(a)):
        if leader == a[i]:
            quantity += 1
    return quantity


print(find([1, 2, 3, 1, 1, 1, 1]))
print(find([1, 2, 1, 2, 1, 2, 1, 2, 1, 3, 1, 1]))
print(find([2, 2, 2, 2, 2, 2, 2, 2]))
print(find([1, 2, 3, 4, 5, 6, 7, 8, 9]))
print(find_1_3([1, 1, 3, 4, 1, 3, 4, 1, 3, 3, 4, 1, 3, 1]))
