# Return the Nth Even Number
import random
def nth_even(n):
    x = random.choice([True, False])
    if x == True:
        return 2 * (n - 1)
    else:
        return (2 * n) - 2
