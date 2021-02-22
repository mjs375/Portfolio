def trouble(x, t):
    i = 0
    for _ in range(len(x)-1):
        if x[i] + x[i+1] == t:
            x.pop(i+1) 
            # remove 2nd elem, do NOT advance, 
            # need to check if previous adds to new next to == t!
            # list has 'stepped' up to the checkpoint
        else:
            i += 1 # only advance now,
            # you need to move the checkpoint to step to the list...
    return x
