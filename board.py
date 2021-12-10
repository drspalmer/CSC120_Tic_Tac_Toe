board = [['-', '-', '-'], ['-', '-', '-'], ['-', '-', '-']]

def print_board(board_marked, player_id=0 ,row=0, col=0, show_board=true):
    try:
        if show_board = true:
            board_marked[row][col]=player_id
        for row in board:
            print(row)
        return board_marked
    except IndexError as e:
        print("Input row/col as 0-2", e)

board = print_board(board, show_board=false)

def check_mark(row,col)

def place_mark(row,col,player_id)
    if player_id=1:
        board[row][col]='X';
    else
        board[row][col]'O';
def check_win(board):
    #vertical win
    for i in range(len(board)):
        check=[]

        for row in board:
            check.append(row[i])
        if check.count(check[0]) == len(check) and check[0] != 0:
        print("Congratulations! ${player_id} won!")
        #horizontal win
        for row in board:
            print(row)
        if row.count(row[0]) == len(row) and row[0] != 0:
            print("Congratulations! ${player_id} won!")
    #diagonal win
        diagonals = []
        for y in range(len(board)):
            diagonals.append(board[y][y])
            if diagonals.count(diagonals[0]) == len(diagonals) and diagonals[0] != 0:
            print("Congratulations! ${player_id} won!")
        for col,row in enumerate(reversed(range(len(board)))):
            diagonals.append(board[row][col])
            if diagonals.count(diagonals[0]) == len(diagonals) and diagonals[0] != 0:
            print("Congratulations! ${player_id} won!")

play = true
players =[1,2]
while play:
    board = [['-', '-', '-'], ['-', '-', '-'], ['-', '-', '-']]
    game_won = false
    while not game_won:
        player_id = 1
        row_choice = input("Which row, 0-2?: ")
        col_choice = input("Which column, 0-2?: ")

