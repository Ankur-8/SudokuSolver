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
def print_board(board):
    for i in range(len(board)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - -")
        
        for j in range(len(board[0])):
            if j % 3 == 0 and j != 0:
                print(" | ", end = "")
            
            if j == 8:
                print(str(board[i][j]))
            else:
                print(str(board[i][j]) + " ", end = "")

# Returns the (row, col) pair of first empty slot
# else returns False
def find_empty(board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 0:
                return (i, j)
    return False



# print_board(board)
# print(find_empty(board))