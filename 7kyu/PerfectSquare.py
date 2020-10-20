import math

def is_square3(n):
    if n >= 0:
        a = math.sqrt(n) #get square root
        b = math.floor(a) #round number down
        if a - b == 0:
            return True
        else:
            return False
    else:
        return False
#
#
#
def is_square2(n):
    if n >= 0:
        a = math.sqrt(n)
        b = a % 1 #gives the decimal digits only
        if b == 0:
            return True
        else:
            return False
    else:
        return False
#
#
#
def is_square(n):
    if n >= 0 and (math.sqrt(n)) % 1 == 0:
        return True
    else:
        return False
