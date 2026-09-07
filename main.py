# Series of small games user can choose from
def main():
    pick_option = input("Pick an Option: ")
    return pick_option

def tic_tac_toe():
    board = [[0, 0, 0] for _ in range(3)]
    print_board(board)
    win = False
    while not win:
        choice = input("Where would you like to input your piece?")
        board = input_piece(board)
        won = detect_win(board)
        if won == "True":
            win = True
        elif won == "lost":
            return False
    return True

def print_board(b):
    for row in b:
        for column in row:
            print(column + " ", end = "")
        print()
    return 

def input_piece(b):

    print_board(b)
    return b

def detect_win(b):
    return bool
    
# true = win, false = lose
if __name__ == "__main__":
    option = main()
    if option == "a":
        tic_tac_toe()