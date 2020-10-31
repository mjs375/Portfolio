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
    
