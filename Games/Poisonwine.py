""" A RIDDLE
C-3.53 An evil king has n bottles of wine, and a spy has just poisoned one of them. 
Unfortunately, they do not know which one it is. 
The poison is very deadly; just one drop diluted even a billion to one will still kill (any bottle of wine can be split among any `n` tasters).
Even so, it takes a full month for the poison to take effect (you can only do exactly one round of taste-testing). 
Design a scheme for determining exactly which one of the wine bottles was poisoned in just one month’s time,
while expending O(logn) taste testers. Each taster can taste as many wines as they must (no limit).
"""

import random

def find_poison(n):
    #
    #--Creating the bottles (binary labels)
    bottles = [ bin(bottle) for bottle in range(1,n+1) ]
    #
    #--One random bottle is poisoned
    mystery = bin( random.randrange(1,n+1) )
    print(f"The cellar has {n} bottles. (Bottle #{int(mystery,2)} is poisoned!).")
    #
    #--How many binary places are needed? (ie how many tasters)
    num = format(bin(n))
    places = len(num)-2
    #
    #--Conscript poison-testers (key=binaryplace L>R, True == alive)
    tasters = {i: True for i in range(places)}
    #
    #--Victims take a moment to pray:
    print("CHORUS: 'O old gods & the new, we pray deliverance...'")
    #
    #--Begin divvying out the sips of wine:
    for bottle in bottles: 
        #--Create sips of wine w/ labels
        sip = bottle[2:].zfill(places) # fix leading 0s
        #--Rotate tasters, who has to taste this one?:
        for taster in tasters.keys():
            if sip[taster] == "1":
                if bottle == mystery: # check is poisoned bottle
                    tasters[taster] = False # taster dies
    #
    #--Tasting over. Gather up the bodies & de-code the mystery:
    #
    
    #--Need some dirty work to help deal with order of binary/tasters:
    binary = [] # 1 2 4 8 16 (order will be reversed later)
    for i in range(places):
        binary.append(2**i)
    #
    #--
    number = 0 # tally to add up to the poisoned bottle number
    deaths = 0 # count of dead tasters
    for taster, place in zip(tasters, binary[::-1]):
        #print(taster, place)
        if tasters[taster] == False:
            number += place
            deaths += 1
    print(">>> Poisoned bottle:",number)
    print(f">>> Deaths: {deaths}/{places}")
    print(f"I, your beloved king, do thank thee for your noble sacrifice. It was worth it, it shall not be in vain– I and my fellow nobles will debauch this sublime night. It shall be a most beautiful rager. Cometh, my bros– CHUG, CHUG, CHUG!!")
    
    
find_poison(n=100000)
