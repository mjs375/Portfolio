def positive_sum(arr):
    total = int()
    for i, value in enumerate(arr):
        #print(index, value)
        if value > 0:
            total += value
    return total
