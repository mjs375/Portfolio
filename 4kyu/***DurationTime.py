# https://www.codewars.com/kata/52742f58faf5485cae000b9a/train/python

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
    #  
    # MINUTES:
    if s >= 60:
        m = s // 60
        s = s % 60
        time["minute"] = m #
        time["second"] = s

        
    # HOURS:
    if m >= 60:
        h = m // 60
        m = m % 60
        time["minute"] = m #
        time["hour"] = h #

        
    # DAYS
    if h >= 24:
        d = h // 24
        h = h % 24
        time["hour"] = h #
        time["day"] = d #
            
    # YEARS
    if d >= 365:
        y = d // 365
        d = d % 365
        time["day"] = d #
        time["year"] = y #
    #
    #
    # time(dictionary) gives access to both value and key (unit: hour, minute)
    for i, v in time.items():
        print(i,v)
    print(f"ANS:{time['year']} y" if time["year"] else "TODO")
    
# f'My name {person["name"]} and my age {person["age"]}'
