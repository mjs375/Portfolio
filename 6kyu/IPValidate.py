import re

def is_valid_IP(strng):
    nums = strng.split(".")
    # 4 "."-separated octets?
    if len(nums) != 4:
        return False
    #
    for octet in nums:
        if not octet.isdigit():
            return False
        if octet[0] == "0" and len(octet) > 1:
            return False
        if int(octet) > 255:
            return False
    #
    #
    #
    return True

    
    
    
    # REGEX
    #--Match any number 1-255, no leading zeros:
    #nums = "2[012345][0-9]|1[0-9][0-9]|[1-9][1-9]"
    


"""
Write an algorithm that will identify valid IPv4 addresses in dot-decimal format. IPs should be considered valid if they consist of four octets, with values between 0 and 255, inclusive.
Valid inputs examples:
  0.0.0.0
  1.2.3.4
  123.45.67.89
Invalid input examples:
  1.2.3
  1.2.3.4.5
  123.456.78.90
  123.045.067.089
Notes:
  Leading zeros (e.g. 01.02.03.04) are considered invalid
  Inputs are guaranteed to be a single string
"""
