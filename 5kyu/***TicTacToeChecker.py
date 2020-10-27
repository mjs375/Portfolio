def is_it_possible(field): #"XXXOOOXXX" <= [str]
    print("GAME:")
    print("", field[:3], "\n", field[3:6], "\n", field[6:])
    
    wins = [
        "ooo......", #Horizontal win, top
        "...ooo...", #Horizontal win, mid
        "......ooo", #Horizontal win, bottom
        "o...o...o", #Diagonal win, L-R
        "..o.o.o..", #Diagonal win, R-L   ####
        "o..o..o..", #Vertical win, L
        ".o..o..o.", #Vertical win, mid
        "..o..o..o", #Vertical win, R
    ]
    
    
    
    
    # Test 1: Equal number of plays, X goes first (Xs must equal or surpass 0s by 1)
    # # # # #
    Oh, Ex = field.count('0'), field.count('X')
    #
    if Oh > Ex: return False # Exs equal or surpass Ohs by 1 (X goes first)
    if Ex - Oh > 1: return False
    
        
    
    
    
    # Test 2: More than one winning triple
    # # # # #
    win_count_ex, win_count_oh = 0, 0 #only 1 person can win a game
    checkfieldEx = field.replace("X","o").replace("0", ".").replace("_", ".")
    checkfieldOh = field.replace("0", "o").replace("X", ".").replace("_", ".")
    #print(checkfieldEx)
    #print(checkfieldOh)
    print("#")
    print("", checkfieldOh[:3], "\n", checkfieldOh[3:6], "\n", checkfieldOh[6:])
    print("#")
    print("", checkfieldEx[:3], "\n", checkfieldEx[3:6], "\n", checkfieldEx[6:])


    
    for win in wins: #iterate over each winning condition, check against gameboard
        #print("Checking for wins...")
        if checkfieldEx == win: #Check all for Ex wins
            win_count_ex += 1
            print("X Win:", win)
        if checkfieldOh == win: #Check for all Oh wins
            win_count_oh += 1
            print("0 Win:", win)
    #
    #
    print("X wins:",win_count_ex)
    print("0 wins:",win_count_oh)
    if win_count_ex + win_count_oh > 1: return False #Only 1 WIN on the board allowed
    
    # When X wins, 0 will always have 1 less mark on the field
    if win_count_ex == 1 and Ex - Oh != 1: return False
    #
    if win_count_oh == 1 and Ex > Oh: return False
    
    
    
    
    
    
    
    return True # Passed all tests, so must be a valid game!
    
    
    
