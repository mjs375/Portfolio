import itertools

def get_pins(PIN):
    #--Adjacent nums (including num itself):
    adjacents = {
        1: [1, 2, 4],
        2: [1, 2, 3, 5],
        3: [2, 3, 6],
        4: [1, 4, 5, 7],
        5: [2, 4, 5, 6, 8],
        6: [3, 5, 6, 9],
        7: [4, 7, 8],
        8: [5, 7, 8, 9, 0],
        9: [6, 8, 9],
        0: [0, 8],
    }
    
    
    #--Create list of lists for PIN <> adjacents
    biglist = []
    for num in PIN:
        #--Get adjacent numbers for each num:
        adj = adjacents[int(num)]
        #--Extend list by sublist:
        biglist.extend([adj])
    #print(biglist)
        
    #--Create all possible combinations of possible PINs:
    answer = []
    PINs = list(itertools.product(*biglist))
    #print("PINs:",PINs)
    for PIN in PINs:
        a = str()
        for num in PIN:
            a += str(num)
        answer.append(a)
    
    
    
    
    print(">>>",answer)
    return answer
    
    
    
    
    
    
    
    
    
"""
Alright, detective, one of our colleagues successfully observed our target person, Robby the robber. We followed him to a secret warehouse, where we assume to find all the stolen stuff. The door to this warehouse is secured by an electronic combination lock. Unfortunately our spy isn't sure about the PIN he saw, when Robby entered it.

The keypad has the following layout:

┌───┬───┬───┐
│ 1 │ 2 │ 3 │
├───┼───┼───┤
│ 4 │ 5 │ 6 │
├───┼───┼───┤
│ 7 │ 8 │ 9 │
└───┼───┼───┘
    │ 0 │
    └───┘
He noted the PIN 1357, but he also said, it is possible that each of the digits he saw could actually be another adjacent digit (horizontally or vertically, but not diagonally). E.g. instead of the 1 it could also be the 2 or 4. And instead of the 5 it could also be the 2, 4, 6 or 8.

He also mentioned, he knows this kind of locks. You can enter an unlimited amount of wrong PINs, they never finally lock the system or sound the alarm. That's why we can try out all possible (*) variations.

* possible in sense of: the observed PIN itself and all variations considering the adjacent digits
"""
