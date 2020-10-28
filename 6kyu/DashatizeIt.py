def dashatize(num):
    ans = ""
    if num == None: return str(None)
    for digit in str(num):
        if  digit == "-": pass #negative number sign
        elif int(digit) % 2 == 0: ans += digit
        else:
            if ans == "": #first iteration, if odd
                ans += digit + "-"
            elif ans[-1] == "-": #if already a preceding "-":
                ans += digit + "-"
            else:
                ans += "-" + digit + "-"
    if ans[-1] == "-":
        return ans[:-1]
    return ans
    
# # # # # # # # # # # # # # # # # #
Given a number, return a string with dash'-'marks before and after each odd integer, but do not begin or end the string with a dash mark.
  Ex:
    dashatize(274) -> '2-7-4'
    dashatize(6815) -> '68-1-5'
