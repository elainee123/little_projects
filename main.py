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
    if b[0][0] == b[0][1] == b[0][2]:
        return True
    elif b[1][0] == b[1][1] == b[1][2]:
        return True
    elif b[2][0] == b[2][1] == b[2][2]:
        return True
    elif b[0][0] == b[1][0] == b[2][0]:
        return True
    elif b[0][1] == b[1][1] == b[2][1]:
        return True
    elif b[0][2] == b[1][2] == b[2][2]:
        return True
    elif b[0][0] == b[1][1] == b[2][2]:
        return True
    elif b[0][3] == b[1][1] == b[2][0]:
        return True
    return bool
    
# true = win, false = lose
if __name__ == "__main__":
    option = main()
    if option == "a":
        tic_tac_toe()