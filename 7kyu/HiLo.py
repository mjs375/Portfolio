def high_and_low(numbers):
    list = numbers.split(" ")
    list2 = []
    for i in list:
        list2.append(int(i))
    hi, lo = max(list2), min(list2)
    return str(hi) + " " + str(lo)
    
"""
In this little assignment you are given a string of space separated numbers, and have to return the highest and lowest number.

Example:

high_and_low("1 2 3 4 5")  # return "5 1"
high_and_low("1 2 -3 4 5") # return "5 -3"
high_and_low("1 9 3 4 -5") # return "9 -5"
"""
