import re
def lowercase_count(strng):
    return len(re.findall("[a-z]", strng))

# Your task is simply to count the total number of lowercase letters in a string.
