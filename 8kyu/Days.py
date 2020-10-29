def whatday(num):
    days = ["Sunday","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
    return days[num-1] if 0 < num < 8 else "Wrong, please enter a number between 1 and 7"
