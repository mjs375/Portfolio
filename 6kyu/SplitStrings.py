def solution(s):
    x = len(s)
    ans = []
    if len(s) % 2: # if odd
        s += "_"
    for i in range(0, x, 2):
        try:
            ans.append(s[i] + s[i+1])
        except:
            ans.append(s[i] + s[i+1])
    return ans
"""
Complete the solution so that it splits the string into pairs of two characters. If the string contains an odd number of characters then it should replace the missing second character of the final pair with an underscore ('_').

Examples:

solution('abc') # should return ['ab', 'c_']
solution('abcdef') # should return ['ab', 'cd', 'ef']
"""
