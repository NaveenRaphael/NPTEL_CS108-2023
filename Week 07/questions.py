# ### Things to do for Connect 4:

# 1. Code a basic connect 4 game in the CLI
#     1. Get user input, and place tiles accordingly
#     2. Identify when a user wins
# 2. Make this more interactive by drawing a board, and updating the board as the game continues

board = [["\t" for i in range(7)] for i in range(6)]


def print_board():
    print("..Board..")
    for row in board:
        for cell in row:
            print(f"|{cell}|", end="")
        print()
    print("--Board end--")


def player_win(player_symbol, column, row):
    # case 1: vertical:
    if row <= 2:
        if (board[row][column] == board[row+1][column]) and (board[row][column] == board[row+2][column]) and (board[row][column] == board[row+3][column]):
            return True
    # case 2: Horizontal:
    row_check = max(column-3, 0)
    start = False
    counter = 0
    while row_check < 7:
        if not start:
            if board[row][row_check] == player_symbol:
                start = True
                counter = 1
        else:
            if board[row][row_check] != player_symbol:
                if row_check < column:
                    start = False
                else:
                    break
            else:
                counter = counter + 1
                if counter == 4:
                    return True
        # print(f"{row_check} and {start} and {counter}")
        row_check += 1

    # case 2 equal diagonals:
    i = -3
    i = max(-column, i)
    i = max(-row, i)

    start = False
    counter = 0
    while i <= 3:
        if row+i == 6:
            # print("breaking 1")
            break
        if column+i == 7:
            # print("breaking 2")
            break

        if not start:
            if board[row+i][column+i] == player_symbol:
                start = True
                counter = 1
        else:
            if board[row+i][column+i] != player_symbol:
                if row_check < column:
                    start = False
                else:
                    # print("breaking 3")
                    break
            else:
                counter = counter + 1
                if counter == 4:
                    return True

        # print(f"{i} and {start} and {counter}")
        i += 1

    # case 3 other diagonals:
    i = -3
    i = max(-column, i)
    i = max(row-5, i)

    start = False
    counter = 0
    print(f"{i} and {start} and {counter}")
    while i <= 3:
        if row-i == 0:
            break
        if column+i == 7:
            break

        if not start:
            if board[row-i][column+i] == player_symbol:
                start = True
                counter = 1
        else:
            if board[row-i][column+i] != player_symbol:
                if row_check < column:
                    start = False
                else:
                    break
            else:
                counter = counter + 1
                if counter == 4:
                    return True

        # print(f"{i} and {start} and {counter}")
        i += 1

    return False


def player_turn(player_name, player_symbol):
    print(f"{player_name} turn")
    col = int(input("Which column do you want to put the piece?"))-1

    i = 0
    if board[0][col] != "\t":
        print("That column is full")
        pass
    if board[5][col] == "\t":
        i = 5
    else:
        while i < 5:
            if board[i][col] != "\t":
                break
            i = i+1
        i = i-1

    print(f"row is {i}, col is {col}")
    board[i][col] = player_symbol

    if (player_win(player_symbol, col, i)):
        print(f"{player_name} won!")
        return True
    return False


player1_name = input("What is the player 1 name?")
player2_name = input("What is the player 2 name?")

player1_symbol = 'x\t'
player2_symbol = 'o\t'


counter = 0

while(True):
    counter += 1
    if counter % 2 == 0:
        if player_turn(player1_name, player1_symbol):
            print_board()
            break
    else:
        if player_turn(player2_name, player2_symbol):
            print_board()
            break

    print_board()
