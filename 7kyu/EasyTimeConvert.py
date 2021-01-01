def time_convert(num):
    print(num, "minutes")
    
    if num <= 0:
        return "00:00"
    
    min = num % 60
    hr = num - min
    hr = hr // 60
    
    print(hr, min)
    answer = str()
    if len(str(hr)) < 2:
        answer += "0"+str(hr)
    else:
        answer += str(hr)
    #
    answer += ":"
    #
    if len(str(min)) < 2:
        answer += "0"+str(min)
    else:
        answer += str(min)
    return answer
"""
This kata requires you to convert minutes (int) to hours and minutes in the format hh:mm (string).

If the input is 0 or negative value, then you should return "00:00"

Hint: use the modulo operation to solve this challenge. The modulo operation simply returns the remainder after a division. For example the remainder of 5 / 2 is 1, so 5 modulo 2 is 1.

Example
If the input is 78, then you should return "01:18", because 78 minutes converts to 1 hour and 18 minutes.
"""
