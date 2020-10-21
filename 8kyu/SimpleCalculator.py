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


# # # # # B E T T E R : # # # # # 
def calculator(x,y,op):
    if type(x) == int and type(y) == int and str(op) in "+-/*":
        ans = eval(f'{x}{op}{y}')
        return ans
    else:
        return "unknown value"
#type()     returns 'type'
#eval(...)     returns result evaluated in inner expression(...)
    
    
# # # # # B E S T : # # # # # 
def calculator(x,y,op):
  return eval(f'{x}{op}{y}') if type(x) == type(y) == int and str(op) in '+-*/' else 'unknown value'
