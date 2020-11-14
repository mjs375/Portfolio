# # # # # # # # # # # # # # # # #
# # # T I C - T A C - T O E # # #
# # # # # # # # # # # # # # # # #

# $ python3 tictactoe.py

import re
import time
import sys

players = {1:"X", -1:"0"} # dict of turn/players



# # # Display the gameboard in the console:
def print_board(board):
    print("", board[:3], "\n", board[3:6], "\n", board[6:])
    time.sleep(0.5)
#
#
#
# # # Which player, which move?
def get_move(player, turn, board, move):
    ### Check if legal move (for re-try):
    if move != "%":
        if move in board and move != "X" and move != "0":
            return move
    ### Prompt for move
    move = input(f"What is your move, {player}?\n>>> ")
    ### Check if legal move (first time):
    if move == "r": # player(s) can resign(/call a draw) by declaring 'r' move
        sys.exit(f"Player {player} resigned.")
    if move in board and move != "X" and move != "0":
        return move
    else: #re-prompt for move recursively if invalid (until OK)
        time.sleep(0.5)
        print("That move isn't allowed!")
        time.sleep(0.5)
        print_board(board) # print board again
        move = get_move(player, turn, board, move) # recursive until legal move...
        return move
#
#
#
# # # Draw valid move on the board
def draw_move(move, board, turn):
    ### Which player, X or 0?:
    board = board.replace(move, players.get(turn))
    return board
#
#
#
# # # Did the latest move score the win?
def win_check(board):
    ### Winning conditions:
    wins = [ # only looking at X OR 0; not the both or blanks
        "ooo......", #Horizontal win, top
        "...ooo...", #Horizontal win, mid
        "......ooo", #Horizontal win, bottom
        "o...o...o", #Diagonal win, L-R
        "..o.o.o..", #Diagonal win, R-L
        "o..o..o..", #Vertical win, L
        ".o..o..o.", #Vertical win, mid
        "..o..o..o", #Vertical win, R
    ]
    ### Take a snapshot of the board (turn to X or 0 pieces only):
    checkEx = board.replace("X", "o").replace("0", ".")
    checkEx = re.sub("[1-9]", ".", board)
    checkOh = board.replace("0", "o").replace("X", ".")
    checkOh = re.sub("[1-9]", ".", board)
    ###
    win = ""
    for win in wins: # loop over all possible win conditions
        winReg = str(win.replace(".", "[o\.]{1}"))
        checkRegEx = re.search(str(winReg), str(checkEx))
        checkRegOh = re.search(str(winReg), str(checkOh))
        if checkRegEx:
            return "X"
        if checkRegOh:
            return "0"
        else:
            return ""



# ## ### #### ##### ###### ##### #### ### ## #
# # # Each step in game, looped until game-over:
def game():
    # # # Starting variables:
    board = "789456123"
    turn = -1
    # # # # # LOOP:
    for i in range(9):
        ### Show players the current board:
        if i == 0: # first turn
            print_board(board)
        ### Get active player's move:
        turn *= -1
        player = players.get(turn)
        move = "%"
        move = get_move(player, turn, board, move)
        ### Edit board:
        board = draw_move(move, board, turn)
        print_board(board)
        time.sleep(0.5)
        ### Check for win conditions:
        winner = win_check(board)
        ### Check for winner:
        if winner != "":
            return f"The winner is {winner}!"
        ### Rinse & Repeat!
    sys.exit("It's a draw!")
#
#
#
# # # Start the game:
print("Start!")
game()


"""
TESTER:
    $ python3 -m pdb game.py
- Next line of code: press 'n'
- Check full code: press 'l'
- Check variable value: press 'p' + 'variable_name'
"""
