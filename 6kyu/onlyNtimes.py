#--My/First solution:
def delete_nth(order,max):
    tally = {num:0 for num in order}
    ans = []
    for n in order:
        if tally[n] < max:
            ans.append(n)
        tally[n] += 1
    return ans
            
#--Another cool solution:
def delete_nth(order,max_e):
    ans = []
    for o in order:
        if ans.count(o) < max_e: ans.append(o)
    return ans
    


"""
Given a list lst and a number N, create a new list that contains each number of lst at most N times without reordering. For example if N = 2, and the input is [1,2,3,1,2,1,2,3], you take [1,2,3,1,2], drop the next [1,2] since this would lead to 1 and 2 being in the result 3 times, and then take 3, which leads to [1,2,3,1,2,3].
"""
