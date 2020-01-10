def used_row(board,num,row):
    for i in range(9):
        if board[row][i] == num:
            return True

    return False 

def used_col(board,num,col):
    for i in range(9):
        if board[i][col]==num:
            return True

    return False       

def used_box(board,num,col,row):
    for i in range(3):
        for j in range(3):
            if board[i+row][j+col]==num:
                return True
    
    return False

def is_valid(row, col, board,num):
    return not used_box(board,num,col-col%3,row-row%3) and not used_col(board,num,col) and not used_row(board,num,row)



def cursor(l, board):
    for row in range(9):
        for col in range(9):
            if board[row][col]==0:
                l[0]=row
                l[1]=col    
                return True

    return False


def print_solution(board):
    for i in range(9):
        print()
        for j in range(9):
            print(board[i][j],end='|' if not (j+1)%3 else ',')


def solve_sudoku(board):
    l=[0,0]

    if not cursor(l,board):
        return True

    row,col=l[0],l[1]

    for i in range(1,10):
        if is_valid(row,col,board,i):

            board[row][col]=i
            
            if solve_sudoku(board):
                return True
            else:
                board[row][col]=0

    #triggers the backtracking
    return False    


if __name__ == '__main__':
    board=[ [0,5,0,0,3,0,0,9,0],
            [9,0,2,0,0,4,0,0,1],
            [0,0,0,0,7,0,0,2,0],
            [0,2,0,7,0,6,0,0,0],
            [4,0,8,0,0,0,6,0,2],
            [0,0,0,8,0,9,0,1,0],
            [0,3,0,0,8,0,0,0,0],
            [1,0,0,5,0,0,3,0,8],
            [0,8,0,0,6,0,0,4,0]]
    if(solve_sudoku(board)):
        print_solution(board)
    else:
        print('fddasddf')
