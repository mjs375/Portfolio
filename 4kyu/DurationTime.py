def format_duration(s):
    if s == 0: return "now"
    m = h = d = y = 0
    time = {} #dict()
    time["second"] = s #
    time["minute"] = m #
    time["hour"] = h #
    time["day"] = d #
    time["year"] = y #
    #
    # MINUTES:
    if s >= 60:
        m = s // 60
        s = s % 60
        time["minute"] = m #
        time["second"] = s #
    #
    # HOURS:
    if m >= 60:
        h = m // 60
        m = m % 60
        time["minute"] = m #
        time["hour"] = h #
    #
    # DAYS
    if h >= 24:
        d = h // 24
        h = h % 24
        time["hour"] = h #
        time["day"] = d #
    # 
    # YEARS
    if d >= 365:
        y = d // 365
        d = d % 365
        time["day"] = d #
        time["year"] = y #
    #
    #
    # time(dictionary) gives access to both value and key (unit: hour, minute)
    ans = ""
    c = 0
    #--Dictionary is iterated 'reversed', so each string is added to the front, stacking on that way
    for i, v in time.items():
        print(i, v)
        #--If on the second actual value, it will be the 2nd from the end, so end with "and ":
        if c == 1:
            if v == 1:
                c += 1
                ans = f"{v} {i} and " + ans
            elif v > 1:
                c += 1
                ans = f"{v} {i}s and " + ans
        #
        elif v == 1:
            c += 1
            ans = f"{v} {i}, " + ans
        elif v > 1:
            c += 1
            ans = f"{v} {i}s, " + ans   
    #
    #
    print(">>> ",ans[:-2]) # strip the last  ", ""
    return ans[:-2]

# https://www.codewars.com/kata/52742f58faf5485cae000b9a/train/python


"""
Your task in order to complete this Kata is to write a function which formats a duration, given as a number of seconds, in a human-friendly way.

The function must accept a non-negative integer. If it is zero, it just returns "now". Otherwise, the duration is expressed as a combination of years, days, hours, minutes and seconds.

It is much easier to understand with an example:

format_duration(62)    # returns "1 minute and 2 seconds"
format_duration(3662)  # returns "1 hour, 1 minute and 2 seconds"

"""
