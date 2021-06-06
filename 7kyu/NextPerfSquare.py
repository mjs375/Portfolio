import math # math.sqrt(num) : returns square-root of num as floating-type

def find_next_square(sq):
    
    #--Is initial num a perfect square itself?
    if not math.sqrt(sq).is_integer():
        return -1
    
    """
    #--How NOT to do it:
    next = sq + 1
    # check each next number until you find a perfect square... huge num of iterations!
    while True:
        if math.sqrt(next).is_integer():
            print("!!!",next)
    """
    
    #--Find next perfect square:
    square = math.sqrt(sq)
    square += 1
    return square**2 # exponents are `**` in Python
  
"""
  You might know some pretty large perfect squares. But what about the NEXT one?
  Complete the findNextSquare method that finds the next integral perfect square after the one passed as a parameter. Recall that an integral perfect square is an integer n such that sqrt(n) is also an integer.
  If the parameter is itself not a perfect square then -1 should be returned. You may assume the parameter is non-negative.
    Examples:
      findNextSquare(121) --> returns 144
      findNextSquare(625) --> returns 676
      findNextSquare(114) --> returns -1 since 114 is not a perfect square
"""
