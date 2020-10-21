def calculator(x,y,op):
    if op == "+" or op == "-" or op =="/" or op =="*":
        if str(x).isdigit() and str(y).isdigit():
            if op == "+":
                return x+y
            if op == "-":
                return x-y
            if op == "/":
                return x/y
            if op == "*":
                return x*y
        else:
            return "unknown value"
    else:
        return "unknown value"
        
"""
You are required to create a simple calculator that returns the result of addition, subtraction, multiplication or division of two numbers.
Your function will accept three arguments:
The first and second argument should be numbers.
The third argument should represent a sign indicating the operation to perform on these two numbers.
If the variables are not numbers or the sign does not belong to the list above a message "unknown value" must be returned.
"""
