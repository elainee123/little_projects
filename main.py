# Series of small games user can choose from
def main():
    pick_option = input("Pick an Option: ")
    return pick_option

def tic_tac_toe():
    board = [[0, 0, 0] for _ in range(3)]
    print_board(board)
    win = False
    while not win:
        column = input("Where would you like to input your piece? (column)")
        row = input("Where would you like to input your piece? (row)")
        board = input_piece(column, row, board)
        won = detect_win(board)
        if won == "True":
            win = True
        elif won == "lost":
            return False
        opponent_play(board)
    return True

def opponent_play(b):
    pass

def print_board(b):
    for row in b:
        for column in row:
            print(column + " ", end = "")
        print()
    return 

def input_piece(column, row, b):
    if b[column][row] == 0:
        b[column][row] = 'x'
    else:
        return False
    print_board(b)
    return b

def detect_win(b):
    return bool
    
# true = win, false = lose
if __name__ == "__main__":
    option = main()
    if option == "a":
        tic_tac_toe()