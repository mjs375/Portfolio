def reverseWords(s):
    a = s.split(" ")
    b = ""
    for i in reversed(a):
        b += i + " "
    return b[:-1]
"""
Complete the solution so that it reverses all of the words within the string passed in.

Example:

reverseWords("The greatest victory is that which requires no battle")
=> "battle no requires which that is victory greatest The"
