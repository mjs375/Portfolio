import math

def is_prime(n):
    ### 0-1 not prime(nor composite)
    if n < 2: 
        return False
    ### Check for factors up to sqrt(n)
    for i in range(2, int(math.sqrt(n))+1):
        if n % i == 0:
            return False # (composite)
    return True # prime if no factors found
