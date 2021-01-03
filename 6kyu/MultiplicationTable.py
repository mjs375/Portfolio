def multiplication_table(size):
    table = []
    for i in range(size):
        table.append([])
        for j in range(size):
            if i == 0: # Top row, 1-n:
                table[i].append(j+1)
            elif j == 0: # Left col, 1-n:
                table[i].append(i+1)
            else: #--Multiplication Table Itself:
                #table[i].append(0)
                #print(table[0][j] , "X" , table [i][0])
                table[i].append(table[0][j] * table [i][0])    
    #
    #
    [print(row) for row in table]
    #
    return table
"""
Your task, is to create NxN multiplication table, of size provided in parameter. 
For example, when given size is 3:
  1 2 3
  2 4 6
  3 6 9
For given example, the return value should be: 
  [ [1,2,3],
    [2,4,6],
    [3,6,9] ]
"""
