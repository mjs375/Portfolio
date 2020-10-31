def format_duration(s):
    if s == 0: return "now"
    m = h = d = y = 0
    time = {} #dict()
    time["second"] = s #
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



























        
        
        
        
        
        





def format_duration(seconds):
    if seconds == 0: return "now"
    minutes = hours = days = years = 0
    #
    #  
    # MINUTES:
    if seconds >= 60:
        minutes = seconds // 60
        seconds = seconds % 60
        
    # HOURS:
    if minutes >= 60:
        hours = minutes // 60
        minutes = minutes % 60
        
    # DAYS
    if hours >= 24:
        days = hours // 24
        hours = hours % 24
        print(days, hours, minutes, seconds)
            
    # YEARS
    if days >= 365:
        years = days // 365
        days = days % 365
    #
    #
    print(f"{years} {days} {hours} {minutes} {seconds}")
    #
    #
    # Assemble the print statements: 
        # if any unit == 0, don't print it at all
        # if any unit == 1, print e.g. minute instead of minuteS
        # ", " after each block, except between the last 2: " and "
    #
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    def format_duration(s):
    if s == 0: return "now"
    m = h = d = y = 0
    #
    #  
    # MINUTES:
    if s >= 60:
        m = s // 60
        s = s % 60
        
    # HOURS:
    if m >= 60:
        h = m // 60
        m = m % 60
        
    # DAYS
    if h >= 24:
        d = h // 24
        h = h % 24
            
    # YEARS
    if d >= 365:
        y = d // 365
        d = d % 365
    #
    #
    print(f"{y} {d} {h} {m} {s}")
    # Assemble the print statements: 
        # if any unit == 0, don't print it at all
        # if any unit == 1, print e.g. minute instead of minuteS
        # ", " after each block, except between the last 2: " and "
    # f"{y} years" if m else "{d} days" if d else "{h} hours" if h else "{m} minutes" if m else "{s} seconds"
    ans = ""
    for i in [y,d,h,m,s]:
        #print(i)
        if i > 1:
            ans += f"{i} {repr(i)}, "
            #print(repr())
        elif i == 1:
            ans += f"{i} unit, "
        #else: pass
    print(ans)
    
