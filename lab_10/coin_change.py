def coin_change(system, value):
    counts = [float('inf')] * (value + 1)
    counts[0] = 0
    for i in range(1, value + 1):
        for coin in system:
            if i - coin >= 0:
                counts[i] = min(counts[i - coin] + 1, counts[i])
    return counts[value]


print(coin_change([186, 419, 83, 408], 6249))
