def productFib(prod):
    a, b = 0, 1 # 1st nums of Fibonacci
    #--Handle initial 'exceptions'
    if prod == 1:
        return [1,1,True]
    if prod == 0:
        return [0,1,True]
    #
    while True:
        #--Calc next Fib num
        a, b = b, a+b 
        #--Check if prod or if > prod:
        if a*b == prod:
            return [a,b, True]
        elif a*b > prod:
            return [a,b,False]

# REFACTORED:
def productFib(prod):
    a,b = 0,1
    while a*b < prod:
        a,b = b, b+a
    return [a, b, a*b == prod]


"""

The Fibonacci numbers are the numbers in the following integer sequence (Fn):
  0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, ...
such as
  F(n) = F(n-1) + F(n-2) with F(0) = 0 and F(1) = 1.
Given a number, say prod (for product), we search two Fibonacci numbers F(n) and F(n+1) verifying
  F(n) * F(n+1) = prod.
Your function productFib takes an integer (prod) and returns an array:
    [F(n), F(n+1), true] or {F(n), F(n+1), 1} or (F(n), F(n+1), True)
depending on the language if F(n) * F(n+1) = prod.
If you don't find two consecutive F(n) verifying F(n) * F(n+1) = prodyou will return
    [F(n), F(n+1), false] or {F(n), F(n+1), 0} or (F(n), F(n+1), False)
F(n) being the smallest one such as F(n) * F(n+1) > prod.

productFib(714) # should return (21, 34, true), 
                # since F(8) = 21, F(9) = 34 and 714 = 21 * 34
"""
