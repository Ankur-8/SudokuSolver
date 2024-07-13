# Sample problem sudoku puzzle board
# 0 indicates empty spaces
# Board is in row-wise matrix format
board = [
    [2,9,0,0,0,0,0,8,7],
    [0,0,0,0,8,0,0,0,0],
    [0,0,5,2,7,0,0,4,1],
    [0,0,0,9,0,0,1,0,6],
    [0,0,1,0,0,0,9,0,0],
    [9,0,4,0,0,6,0,0,0],
    [7,6,0,0,3,8,4,0,0],
    [0,0,0,0,9,0,0,0,0],
    [3,1,0,0,0,0,0,9,8],
]

# Visualizes the board
def printBoard(bd):
    for i in range(len(bd)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - -")
        
        for j in range(len(bd[0])):
            if j % 3 == 0 and j != 0:
                print(" | ", end = "")
            
            if j == 8:
                print(str(bd[i][j]))
            else:
                print(str(bd[i][j]) + " ", end = "")

# Returns the (row, col) pair of first empty slot
# else returns False
def findEmpty(bd):
    for i in range(len(bd)):
        for j in range(len(bd[0])):
            if bd[i][j] == 0:
                return (i, j)
    return False

# Takes a board as input and returns True if valid else False
# board is sudoku board
# val is the value we are going to insert
# pos is the position in form of (row, col)
def isValid(bd, val, pos):
    # check row and col
    for i in range(len(bd)):
        if bd[pos[0]][i] == val and pos[1] != i:
            return False
        if bd[i][pos[1]] == val and pos[0] != i:
            return False
    # check box
    box_x = pos[1] // 3
    box_y = pos[0] // 3

    for i in range(box_y*3, box_y*3 + 3):
        for j in range(box_x*3, box_x*3 + 3):
            if bd[i][j] == val and (i,j) != pos:
                return False
    return True

def solve(bd):
    # base case
    pos = findEmpty(bd)
    if not pos:
        return True
    
    # recursion
    for i in range(1,10):
        if isValid(bd, i, pos):
            bd[pos[0]][pos[1]] = i

            if solve(bd):
                return True
            
            bd[pos[0]][pos[1]] = 0
    
    return False
