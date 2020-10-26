def solution(seq):
    streak = [] #keep track of streaks
    ans = [] #answer list
    
    first, *list = seq #first=first element, rest = elements 2-end.
    streak.append(first) #add first element to streak to begin with
    
    for num in list+['END']: #iterate seq[-3,-2,-1...19,20,END] (Need that 'END' bit because we need to iterate one past actual last element to see if that num was in a streak. END itself will be ignored, and isn't in 'ans')
        if num != streak[-1]+1: #if num is NOTEQUAL to last streak num+1: you are out of the streak
            if len(streak)>2: #is the streak 3+ in a row?
                ans.append(f'{streak[0]}-{streak[-1]}') #append the completed streak to the answer list
                #print(f'{streak[0]}-{streak[-1]}') #TEST
            else: #a single or only-double streak:
                ans += [str(num) for num in streak] #add the 'non-streak' numbers 1 at a time (using a loop if 2)
            streak = [num] #this conditional branch is only entered AFTER a streak is broken, so need to restart the streak-ing
        else: #num IS streaking with num-1, so just update the streak-list
            streak.append(num)

    
    # Sequence has now been processed: return it, removing clutter
    print(ans) #ans=['-6', '-3-1', '3-5', '7-11', '14'...]
    return ",".join(ans) #joins together 'ans' list elements, each linked by ","
    
    
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

# first, #rest = list
  # This splits the 'list' into 'first', containing the first element, and (*)'rest', which contains the rest of the list.
    # More familiar way to do this:
      # first, rest = list[0], list[1:] #(slice notation)



"""
A format for expressing an ordered list of integers is to use a comma separated list of either individual integers or a range of integers denoted by the starting integer separated from the end integer in the range by a dash, '-'. The range includes all integers in the interval including both endpoints. It is not considered a range unless it spans at least 3 numbers. For example "12,13,15-17".
  Complete the solution so that it takes a list of integers in increasing order and returns a correctly formatted string in the range format.
Example:
  solution([-6, -3, -2, -1, 0, 1, 3, 4, 5, 7, 8, 9, 10, 11, 14, 15, 17, 18, 19, 20])
    # returns "-6,-3-1,3-5,7-11,14,15,17-20"
"""
