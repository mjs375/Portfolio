def solution(a, z):
    l = len(z)
    if a[-l:] == z or l ==0:
        return True
    else:
        return False


"""
Complete the solution so that it returns true if the first argument(string) passed in ends with the 2nd argument (also a string).

Examples:

solution('abc', 'bc') # returns true
solution('abc', 'd') # returns false
"""
