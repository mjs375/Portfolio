def reverse(n):
    # n = 123
    print(n)
    reverse = 0
    while n > 0:
        lastdig = n % 10 # = 3, 2
        reverse = (reverse*10) + lastdig
        n = n//10 #round down (same as n = n/10 - lastdigit)
    return reverse
    
 """
 Get the 'reverse' of a number,
    e.g. 1234 >>> 4321
    e.g. 4572 >>> 2754
 """
