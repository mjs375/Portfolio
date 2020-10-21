def set_alarm(employed, vacation):
    return True if employed == True and vacation == False else False

# PYTHON TERNARY OPERATORS: condense if/else to 1 line...
    # value_if_true if condition else value_if_false

"""
Write a function named setAlarm which receives two parameters. The first parameter, employed, is true whenever you are employed and the second parameter, vacation is true whenever you are on vacation. The function should return true if you are employed and not on vacation (because these are the circumstances under which you need to set an alarm). It should return false otherwise. 
"""

# # # # # # # # B E S T _ P  R A C T I C E : # # # # # # # #

def set_alarm(employed, vacation):
    return employed and not vacation
