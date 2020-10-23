import re #REGEX

def validate_pin(pin):
    pin_check = re.fullmatch("\d{4}|\d{6}", pin)
    #pin_check = re.search("^([0123456789]{4}|[0123456789]{6})$", pin)
    if pin_check:
        return True
    else: 
        return False


"""
ATM machines allow 4 or 6 digit PIN codes and PIN codes cannot contain anything but exactly 4 digits or exactly 6 digits.
If the function is passed a valid PIN string, return true, else return false.
  Examples
    "1234"   -->  true
    "12345"  -->  false
    "a234"   -->  false    
# # # # # # # # # # # # # #  # #
[]   A SET OF CHARACTERS    
.    ANY CHARACTER
^    STARTS WITH
$    ENDS WITH
*    ZERO OR MORE OCCURRENCES
+    1 OR MORE OCCURRENCES
{}    EXACTLY X NUM OF OCCURRENCES
|    EITHER OR
/d    RETURNS A MATCH WHERE STR CONTAINS DIGITS -9
/D    RETURNS MATCH WHERE STR DOES NOT CNTN 0-9
()    CAPTURE GROUP
re.fullmatch(pattern, string_text)
    Only returns a match-object if the WHOLE string matches the regex pattern
re.search()
    scans thru string looking for 1st location where the regex pattern finds a match, returns match object or NONE.
"""




#
