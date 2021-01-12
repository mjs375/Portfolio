def max_multiple(divisor, bound):
    print(divisor, bound)
    for i in range(bound,divisor,-1):
        if i % divisor == 0:
            return i

"""
Task:
  Given a Divisor and a Bound , Find the largest integer N , Such That ,
Conditions:
  N is divisible by divisor
  N is less than or equal to bound
  N is greater than 0.
Examples:
  maxMultiple (10,50)  ==> return (50)
  maxMultiple (2,7) ==> return (6)
Explanation:
  (6) is divisible by (2), (6) is less than or equal to bound (7) , and (6) is > 0 .
"""
