def street_fighter_selection(fighters, pos, moves):

    if not moves:
        return []
    passby = [] #fighters iterated over as u/d/l/r...

    for move in moves:
        x = list(pos) # position  list-ified [row, col](updown,leftright)
        if move == "left":
            if x[1] == 0: #(updown,leftright)
                x[1] = 5 #update the list
                pos = tuple(x) #turn back into tuple
                passby = choose(fighters,pos,passby) #call the function, input: list of fighters, current position, list of 'hovered' fighters
            else:
                y = x[1] #5
                x[1] = y - 1
                pos = tuple(x) #re-tuple the coordinate
                passby = choose(fighters,pos,passby)
        elif move == "right":
            if x[1] == 5: #(updown,leftright)
                x[1] = 0 #'circle' around from right-side of screen to left!
                pos = tuple(x) #turn back into tuple
                passby = choose(fighters,pos,passby) #call the function, input: list of fighters, current position, list of 'hovered' fighters
            else: #can move without consideration for circling...
                y = x[1] #5
                x[1] = y + 1
                pos = tuple(x) #re-tuple the coordinate
                passby = choose(fighters,pos,passby)
        elif move == "down":
            if x[0] == 0: #can move down normally
                y = x[0] #
                x[0] = y + 1
                pos = tuple(x) #re-tuple the coordinate
                passby = choose(fighters,pos,passby)
            else: #x[0] == 1
                passby=choose(fighters,pos,passby) #no change to coordinate
        else: #move == "up":
            if x[0] == 1: #move up normally
                y = x[0] #
                x[0] = y - 1
                pos = tuple(x) #re-tuple the coordinate
                passby = choose(fighters,pos,passby)
            else:
                passby = choose(fighters,pos,passby)
    return passby

def choose(fighters,pos,passby): #which fighter is at (tuple) position?
    x = list(pos)
    y,z = x[0], x[1]
    name = fighters[y][z]
    passby.append(name)
    return passby




















# # # # # # # # # # # # U N F A C T O R E D _ V E R S I O N : # # # # # # # # # # # #

def street_fighter_selection(fighters, pos, moves):
    #POS: tuple
    #print(fighters[1][0]) ==> Ken #row,col
    print(pos)
    if not moves:
        return []
    passby = [] #fighters iterated over as u/d/l/r...
    #
    # #
    # # #  #   #    #
    # #
    #
    for move in moves:
        
        x = list(pos) # position  list-ified [row, col](updown,leftright)
        
        # LLL EEE FFF TTT
        if move == "left":
            print(move,pos)
            if x[1] == 0: #(updown,leftright)
                x[1] = 5 #update the list
                pos = tuple(x) #turn back into tuple
                passby = choose(fighters,pos,passby) #call the function, input: list of fighters, current position, list of 'hovered' fighters
            else: #can simply move left
                #-1 to x[1]:
                y = x[1] #5
                print(x[1])
                x[1] = y - 1
                pos = tuple(x) #re-tuple the coordinate
                passby = choose(fighters,pos,passby)
        # RRR III GGG HHH TTT
        elif move == "right":
            print(move,pos)
            if x[1] == 5: #(updown,leftright)
                x[1] = 0 #'circle' around from right-side of screen to left!
                pos = tuple(x) #turn back into tuple
                passby = choose(fighters,pos,passby) #call the function, input: list of fighters, current position, list of 'hovered' fighters
            else: #can move without consideration for circling...
                y = x[1] #5
                print(x[1])
                x[1] = y + 1
                pos = tuple(x) #re-tuple the coordinate
                passby = choose(fighters,pos,passby)
        elif move == "down":
            print(move,pos)
            #if x[0] == 1: #(updown,leftright)   #CAN'T CIRCLE THE WAGON!
                #x[0] = 0
                #pos = tuple(x) #turn back into tuple
                #passby = choose(fighters,pos,passby) #call the function, input: list of fighters, current position, list of 'hovered' fighters
            if x[0] == 0: #can move down normally
                y = x[0] #
                print(x[0])
                x[0] = y + 1
                pos = tuple(x) #re-tuple the coordinate
                passby = choose(fighters,pos,passby)
            else: #x[0] == 1
                passby=choose(fighters,pos,passby) #no change to coordinate
        else: #move == "up":
            print(move,pos)
            #if x[0] == 0: #(updown,leftright)
                #x[0] = 1
                #pos = tuple(x) #turn back into tuple
                #passby = choose(fighters,pos,passby) #call the function, input: list of fighters, current position, list of 'hovered' fighters
            if x[0] == 1: #move up normally
                y = x[0] #
                print(x[0])
                x[0] = y - 1
                pos = tuple(x) #re-tuple the coordinate
                passby = choose(fighters,pos,passby)
            else:
                passby = choose(fighters,pos,passby)

                
    # AFTER LOOP OF MOVES ENDS:
    return passby

def choose(fighters,pos,passby): #which fighter is at (tuple) position?
    x = list(pos)
    y = x[0]
    z = x[1]
    name = fighters[y][z]
    print(name)
    passby.append(name)
    return passby

    
"""
    e.g. print(fighters[1][4]) == Sagat
0| Ryu0  | E.Honda1 | Blanka2  | Guile3   | Balrog4 | Vega5    |
1| Ken0  | Chun Li1 | Zangief2 | Dhalsim3 | Sagat4  | M.Bison5 |

# Going L/R 'out of bounds' flips over to opposite side of screen.

# Update a TUPLE:
    ex = (0,1) #tuple
    x = list(x) #make into a list
    x[0] = 4 #update the list
    ex = tuple(x) => (4,0) Tuple now updated
    
# list1[0][2]
"""
    
