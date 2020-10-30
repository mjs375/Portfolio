def solution(s, comments):
    lines = s.split('\n') #split string into list of lines
    for i, line in enumerate(lines): #iterate each line
        for comment in comments: #check both '#' and '!' (or whatever)
            end = line.find(comment) #get index of first instance of comment
            if end == -1: 
                pass # find() returns '-1' if no match
            else: #comment found...:
                line = line[:end] #cut off line just before 'end' (index 'stop' is stop-1)
        lines[i] = line.strip(" ") #glue on
    return '\n'.join(lines) #tie together all lines again, glued by '\n'



"""
Description:
Complete the solution so that it strips all text that follows any of a set of comment markers passed in. Any whitespace at the end of the line should also be stripped out.

Example:

Given an input string of:

apples, pears # and bananas
grapes
bananas !apples
The output expected would be:

apples, pears
grapes
bananas
"""
