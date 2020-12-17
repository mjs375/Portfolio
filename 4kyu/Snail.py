# My / others' solutions

import unittest
import os


def snail(snail):

    trail = []

    #--Continue until no rows left:
    while len(snail) > 0:

        #--Go right:
        trail += snail[0]
        del snail[0]

        #--if rows remain, do D-L-U:
        if len(snail) > 0:

            #--Go down:
            for i in snail:
                trail += [i[-1]]
                del i[-1]

            #--Go left:
            if snail[-1]: #--if a bottom row...
                trail += snail[-1][::-1]
                del snail[-1]

            #--Go up:
            for i in reversed(snail):
                trail += [i[0]]
                del i[0]
            print(snail)


    #-- Answer:
    print("Answer:",trail)
    return trail

# # # # # # # # # # # # # # # #

os.system('reset')
array = [[1,2,3],
         [4,5,6],
         [7,8,9]]
#
expected = [1,2,3,6,9,8,7,4,5]
#
assert snail(array) == expected






# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

def snail(snail):
    #--Start with an empty list, you'll be adding (as below) each step of the 'snailing' as a new sublist
    ans = [[]]

    while True:
        try:
            ans.append(snail.pop(0))
            ans.append([x.pop(-1) for x in snail])
            ans.append(snail.pop(-1)[::-1])
            ans.append([x.pop(0) for x in snail][::-1])
        except:
            break
    print(sum(ans, []))
    return sum(ans, [])


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# BEAUTIFUL!

def snail(array):
    out = []
    while len(array):
        out += array.pop(0)
        array = list(zip(*array))[::-1] # Rotate
    return out

