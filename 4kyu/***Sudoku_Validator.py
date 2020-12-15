from math import sqrt

class Sudoku(object):
    def __init__(self, data):
        #--Board itself:
        self.data = data
        #--Transposed board:
        self.step = list(zip(*data[::-1]))
        self.transpose = self.untuple(self.step)
        #--Size of board, N (e.g. 9x9, 4x4):
        self.length = len(self.data)
        #--Numbers in any row (e.g. [1,2,3,4] for N=4):
        self.check = [num for num in range(1,len(self.data)+1)]
    #
    def untuple(self, matrix):
        return [list(elem) for elem in matrix]
    
    def printer(self, board):
        N = len(board)
        print("Game board size:",N,"x",N)
        for i in range(N):
            print(board[i])
    #
    def is_valid(self):
        #--Some printouts:
        self.printer(self.data)
        #self.printer(self.transpose)
        #--Check is valid game: NxN
        counter = 0
        for row in self.data:
            for col in row:
                counter +=1
        if counter != (self.length*self.length):
            print("Invalid game board")
            return False
        #--Check horizontal rows:
        horz = self.line_check(self.data)
        print(" > Horizontal check:",horz)
        #--Check vertical cols:
        vert = self.line_check(self.transpose)
        print(" > Vertical check", vert)
        #--Check boxes:
        boxes = self.boxes_check()
        print(" > Boxes check", boxes)
        if horz and vert and boxes:
            return True
        else:
            return False

            
    def line_check(self, board):
        for i in range(self.length):
            row = board[i]
            check = self.check
            row.sort()
            check.sort()
            if check != row:
                return False
        #--Each row checked out, all ROWS are 1-9 once only:
        return True
    
    def boxes_check(self):
        """ Size of little square (√N*√N). """
        N = self.length
        n = sqrt(N)
        square_size = sqrt(N)*sqrt(N)
        print(n,"x", n)
        
        
        
        
        # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #  
"""
xx xx
xx xx

xx xx
xx xx




xxx xxx xxx
xxx xxx xxx
xxx xxx xxx

xxx xxx xxx
xxx xxx xxx
xxx xxx xxx

xxx xxx xxx
xxx xxx xxx
xxx xxx xxx




"""

#
