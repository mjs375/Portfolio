def killer(suspect_info, dead):
    for killer, victims in suspect_info.items():
        #print(killer, victims) # e.g. James ['Jacob', 'Bill', 'Lucas']
        if all(victim in victims for victim in dead):
            #if victim is in 'victims', looking at each victim
            #Loop each victim in list1, check if in list2; do for each victim
            return killer #if BOTH (a victim common to both lists), you've found the killer (the original key)
    


"""
all()    Returns True if all statements are True


# # # # # # # # # # # #  #
Who is the killer?
Some people have been killed!
You have managed to narrow the suspects down to just a few. Luckily, you know every person who those suspects have seen on the day of the murders.
    Task.
        Given a dictionary with all the names of the suspects and everyone that they have seen on that day which may look like this:
{'James': ['Jacob', 'Bill', 'Lucas'],
 'Johnny': ['David', 'Kyle', 'Lucas'],
 'Peter': ['Lucy', 'Kyle']}
        ...and also a list of the names of the dead people:
['Lucas', 'Bill']
        ...return the name of the one killer, in our case 'James' because he is the only person that saw both 'Lucas' and 'Bill'
"""
