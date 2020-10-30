def chess_board_cell_color(cell1, cell2):
    color = []
    for cell in [cell1, cell2]:
        if cell[0] in "ACEG":
            color.append("black") if int(cell[1]) % 2 != 0 else color.append("white")
        else: # if cell[0] in "bdfh":                
            color.append("white") if int(cell[1]) % 2 != 0 else color.append("black")
    return True if color[0] == color[1] else False





# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #



# A more unnecessarily convoluted function, 
# because I wanted to practice for later chess programs...

def chess_board_cell_color(cell1, cell2):
    
    # # # CREATE THE B/W BOARD:
    switch = False #switch will off-set each row (white,black,white)
    board = []  #list to put board tiles in (list of lists)
    #
    for i in range(8): # create a list with nested lists:THE BOARD
        board.append([]) #each ROW, create another list containing the COL tiles
        switch = not switch #alterate black/white by toggling switch
        for n in range(8): # 8 rows, 8 cols
            if switch == True:
                board[i].append("o") # fills nested lists with data
                switch = False
            else:
                board[i].append("•")
                switch = True
    #print(board)

    rankfile = {
        "A":0,
        "B":1,
        "C":2,
        "D":3,
        "E":4,
        "F":5,
        "G":6,
        "H":7,
        "8":0,
        "7":1,
        "6":2,
        "5":3,
        "4":4,
        "3":5,
        "2":6,
        "1":7,
    }
    
    # Translate index to actual rankfile coordinate notation
    x1, y1 = rankfile.get(cell1[0]), rankfile.get(cell1[1])
    x2, y2 = rankfile.get(cell2[0]), rankfile.get(cell2[1])
    # Get the value of each tile: black/white? (o/•)
    tile1, tile2 = board[x1][y1], board[x2][y2]
    return True if tile1 == tile2 else False
    
                


"""
Given two cells on the standard chess board, determine whether they have the same color or not.
  Example
    For cell1 = "A1" and cell2 = "C3", the output should be true.
"""
