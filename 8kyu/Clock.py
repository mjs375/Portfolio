def past(h, m, s):
    # Good Luck!
    ms = 0
    ms += (h * 3600000)
    ms += m * 60000
    ms += s * 1000
    return ms

"""
Clock shows 'h' hours, 'm' minutes and 's' seconds after midnight.

Your task is to make 'Past' function which returns time converted to milliseconds.

"""
