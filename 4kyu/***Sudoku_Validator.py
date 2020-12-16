# RE-FACTORING NEEDED...

import numpy as np
from copy import deepcopy
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
        for i, row in enumerate(self.data):
            for j, col in enumerate(row):
                if isinstance(self.data[i][j], bool):
                    return False
                counter +=1
        if counter != (self.length*self.length):
            print("Invalid game board")
            return False
        #--Check horizontal rows:
        board = deepcopy(self.data)
        horz = self.line_check(board)
        print(" > Horizontal check:",horz)
        #--Check vertical cols:
        vert = self.line_check(self.transpose)
        print(" > Vertical check", vert)
        #--Check boxes:
        #boxes = self.boxes_check()
        #print(" > Boxes check", boxes)
        if horz and vert:
            squares = self.block(self.data)
            if squares:
                return True
            else:
                print("Squares False")
                return False
        else:
            print("Horz/Vert false")
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
    
    def block(self, board):
        B= board
        n = int(sqrt(len(self.data)))
        for i in range(0, self.length, n): # (0,9,3)
            for j in range(0, self.length, n): # (0,9,3)
                #print(B[i][j], i, j)
                square = []
                for a in range(0,n,1):
                    for b in range(0,n,1):
                        print(B[i+a][j+b])
                        square.append(B[i+a][j+b])
                # Check each square:
                check = self.check
                check.sort()
                square.sort()
                if check != square:
                    print("(i,j)",i,j)
                    print(check, "\n", square)
                    return False
        return True
    

# # # # # # # # # # # # # # # # # # # # # # # # # # # 

"""

Given a Sudoku data structure with size NxN, N > 0 and √N == integer, 
write a method to validate if it has been filled out correctly.
    The data structure is a multi-dimensional Array, i.e:

[
  [7,8,4,  1,5,9,  3,2,6],
  [5,3,9,  6,7,2,  8,4,1],
  [6,1,2,  4,3,8,  7,5,9],

  [9,2,8,  7,1,5,  4,6,3],
  [3,5,7,  8,4,6,  1,9,2],
  [4,6,1,  9,2,3,  5,8,7],

  [8,7,6,  3,9,4,  2,1,5],
  [2,4,3,  5,6,1,  9,7,8],
  [1,9,5,  2,8,7,  6,3,4]
]

Rules for validation
    Data structure dimension: NxN where N > 0 and √N == integer
    Rows may only contain integers: 1..N (N included)
    Columns may only contain integers: 1..N (N included)
    'Little squares' (3x3 in example above) may also only contain integers: 1..N (N included)

"""
