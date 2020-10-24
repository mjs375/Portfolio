def fizzbuzz(n):
    return list(map(fizzbuzzer, range(1, n+1)))
    ##RUNTIME: 631ms
    
def fizzbuzzer(i):
    if not i % 15:
        return "FizzBuzz"
    elif not i % 3:
        return "Fizz"
    elif not i % 5:
        return "Buzz"
    else:
        return i
# # # # # # # # # # # # # # # # # # # # # # # # # # # # 

def fizzbuzz(n):
    ans = []
    for i in range(1, n+1): #zero-indexed...
        if not i % 15:
            ans.append("FizzBuzz")
        elif not i % 3:
            ans.append("Fizz")
        elif not i % 5:
            ans.append("Buzz")
        else:
            ans.append(i)
    return ans
    ## RUNTIME: 625ms
