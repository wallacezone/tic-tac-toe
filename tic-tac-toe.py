from random import randint

# --------------------------- VARS & FUNCS ---------------------------

# the basic structure of the board
board = [
    [' ', ' ', ' '],
    [' ', ' ', ' '],
    [' ', ' ', ' ']
]

#          y
#    00 | 01 | 02
#   ----|----|----
# x  10 | 11 | 12
#   ----|----|----
#    20 | 21 | 22

# convert player's more readable input to list format
def convert_input(i):

    # workaround if user inputs a string != 2 chars
    if len(i) != 2:
        return [3, 3]

    # convert x value
    if i[0] == 'T':
        x = 0
    elif i[0] == 'M':
        x = 1
    elif i[0] == 'L':
        x = 2
    else:
        x = 3

    # convert y value
    if i[1] == 'L':
        y = 0
    elif i[1] == 'M':
        y = 1
    elif i[1] == 'R':
        y = 2
    else:
        y = 3

    # if return value is 3, the index will be out of range and the error
    # will be managed after calling this function
    return [x, y]

# display the current board
def print_board(board):
    print('  ' + board[0][0] + ' | ' + board[0][1] + ' | ' + board[0][2])
    print(' ---+---+---')
    print('  ' + board[1][0] + ' | ' + board[1][1] + ' | ' + board[1][2])
    print(' ---+---+---')
    print('  ' + board[2][0] + ' | ' + board[2][1] + ' | ' + board[2][2])

# compute the AI move based on the current board
def compute_ai(board):

    # if there is a line of 2 Os and the third space is empty,
    # fill it to win
    for x in range(3):
        if board[x][0] == 'O' and board[x][1] == 'O' and board[x][2] == ' ':
            return [x, 2]
        if board[x][0] == 'O' and board[x][1] == ' ' and board[x][2] == 'O':
            return [x, 1]
        if board[x][0] == ' ' and board[x][1] == 'O' and board[x][2] == 'O':
            return [x, 0]
    for y in range(3):
        if board[0][y] == 'O' and board[1][y] == 'O' and board[2][y] == ' ':
            return [2, y]
        if board[0][y] == 'O' and board[1][y] == ' ' and board[2][y] == 'O':
            return [1, y]
        if board[0][y] == ' ' and board[1][y] == 'O' and board[2][y] == 'O':
            return [0, y]
    if board[0][0] == 'O' and board[1][1] == 'O' and board[2][2] == ' ':
        return [2, 2]
    if board[0][0] == 'O' and board[1][1] == ' ' and board[2][2] == 'O':
        return [1, 1]
    if board[0][0] == ' ' and board[1][1] == 'O' and board[2][2] == 'O':
        return [0, 0]
    if board[0][2] == 'O' and board[1][1] == 'O' and board[2][0] == ' ':
        return [2, 0]
    if board[0][2] == 'O' and board[1][1] == ' ' and board[2][0] == 'O':
        return [1, 1]
    if board[0][2] == ' ' and board[1][1] == 'O' and board[2][0] == 'O':
        return [0, 2]

    # if there is a line of 2 Xs and the third space is empty,
    # block it
    for x in range(3):
        if board[x][0] == 'X' and board[x][1] == 'X' and board[x][2] == ' ':
            return [x, 2]
        if board[x][0] == 'X' and board[x][1] == ' ' and board[x][2] == 'X':
            return [x, 1]
        if board[x][0] == ' ' and board[x][1] == 'X' and board[x][2] == 'X':
            return [x, 0]
    for y in range(3):
        if board[0][y] == 'X' and board[1][y] == 'X' and board[2][y] == ' ':
            return [2, y]
        if board[0][y] == 'X' and board[1][y] == ' ' and board[2][y] == 'X':
            return [1, y]
        if board[0][y] == ' ' and board[1][y] == 'X' and board[2][y] == 'X':
            return [0, y]
    if board[0][0] == 'X' and board[1][1] == 'X' and board[2][2] == ' ':
        return [2, 2]
    if board[0][0] == 'X' and board[1][1] == ' ' and board[2][2] == 'X':
        return [1, 1]
    if board[0][0] == ' ' and board[1][1] == 'X' and board[2][2] == 'X':
        return [0, 0]
    if board[0][2] == 'X' and board[1][1] == 'X' and board[2][0] == ' ':
        return [2, 0]
    if board[0][2] == 'X' and board[1][1] == ' ' and board[2][0] == 'X':
        return [1, 1]
    if board[0][2] == ' ' and board[1][1] == 'X' and board[2][0] == 'X':
        return [0, 2]

    # if the center is empty, fill it (only half the times)
    if board[1][1] == ' ' and randint(1,2) == 1:
        return [1, 1]

    # if a corner is empty, fill it (choose a random corner)
    r = randint(1,4)
    if r == 1:
        if board[0][0] == ' ':
            return [0, 0]
        if board[0][2] == ' ':
            return [0, 2]
        if board[2][2] == ' ':
            return [2, 2]
        if board[2][0] == ' ':
            return [2, 0]
    elif r == 2:
        if board[0][2] == ' ':
            return [0, 2]
        if board[2][2] == ' ':
            return [2, 2]
        if board[2][0] == ' ':
            return [2, 0]
        if board[0][0] == ' ':
            return [0, 0]
    elif r == 3:
        if board[2][2] == ' ':
            return [2, 2]
        if board[2][0] == ' ':
            return [2, 0]
        if board[0][0] == ' ':
            return [0, 0]
        if board[0][2] == ' ':
            return [0, 2]
    elif r == 4:
        if board[2][0] == ' ':
            return [2, 0]
        if board[0][0] == ' ':
            return [0, 0]
        if board[0][2] == ' ':
            return [0, 2]
        if board[2][2] == ' ':
            return [2, 2]

    # if a side is empty, fill it (choose a random side)
    r = randint(1,4)
    if r == 1:
        if board[0][1] == ' ':
            return [0, 1]
        if board[1][2] == ' ':
            return [1, 2]
        if board[2][1] == ' ':
            return [2, 1]
        if board[1][0] == ' ':
            return [1, 0]
    elif r == 2:
        if board[1][2] == ' ':
            return [1, 2]
        if board[2][1] == ' ':
            return [2, 1]
        if board[1][0] == ' ':
            return [1, 0]
        if board[0][1] == ' ':
            return [0, 1]
    elif r == 3:
        if board[2][1] == ' ':
            return [2, 1]
        if board[1][0] == ' ':
            return [1, 0]
        if board[0][1] == ' ':
            return [0, 1]
        if board[1][2] == ' ':
            return [1, 2]
    elif r == 4:
        if board[1][0] == ' ':
            return [1, 0]
        if board[0][1] == ' ':
            return [0, 1]
        if board[1][2] == ' ':
            return [1, 2]
        if board[2][1] == ' ':
            return [2, 1]

# check victory
def has_won(board):

    # default victory to False
    victory = False

    # check for victory in rows (skip if a cell is empty)
    for x in range(3):
        if board[x][0] != ' ':
            if board[x][0] == board[x][1] and board[x][1] == board[x][2]:
                victory = True

    # check for victory in cols
    for y in range(3):
        if board[0][y] != ' ':
            if board[0][y] == board[1][y] and board[1][y] == board[2][y]:
                victory = True

    # check diagonals
    if board[1][1] != ' ':
        if (board[0][0] == board[1][1] and board[1][1] == board[2][2]):
            victory = True
        if (board[0][2] == board[1][1] and board[1][1] == board[2][0]):
            victory = True

    return victory

# check if board is complete
def board_is_complete(board):
    board_complete = True
    for x in range(3):
        for y in range(3):
            if board[x][y] == ' ':
                board_complete = False
    return board_complete

# AI's turn
def ai_turn(board):

    # AI move
    x, y = compute_ai(board)
    board[x][y] = 'O'

    # check whether AI has won
    if has_won(board):
        victor = 'O'
        return [board, 'break', victor]

    # check if board is complete
    if board_is_complete(board):
        return [board, 'break', '']

    return [board, '', '']

# player's turn
def player_turn(board):

    # print current board
    print()
    print_board(board)
    print()

    # ask for player's move
    print(' Player: move on which space? (TL/TM/TR/ML/MM/MR/LL/LM/LR)')
    print()
    move = input(' > ')

    # convert input
    x, y = convert_input(move)

    # try to insert player's move into the board or ask again
    try:
        if board[x][y] == ' ':
            board[x][y] = 'X'
        else:
            return [board, 'continue', '']
    except IndexError:
        return [board, 'continue', '']

    # check whether player has won
    if has_won(board):
        victor = 'X'
        return [board, 'break', victor]

    # check if board is complete
    if board_is_complete(board):
        return [board, 'break', '']

    return [board, '', '']

# ------------------------------- MAIN -------------------------------

# title
print()
print(' ------ TIC TAC TOE with Python ------')
print()

# decide whether player or AI begins
print(' You play X, AI plays O. Rolling dice to decide who begins...')
begin = 'X' if randint(1,2) == 1 else '0'
print()
print(' ' + begin + ' begins!')

# main loop
while True:

    if begin == 'X':

        # player's turn
        board, state, victor = player_turn(board)
        if state == 'continue':
            continue
        elif state == 'break':
            break

        # AI's turn
        board, state, victor = ai_turn(board)
        if state == 'break':
            break

    else:

        # AI's turn
        board, state, victor = ai_turn(board)
        if state == 'break':
            break

        # player's turn
        board, state, victor = player_turn(board)
        if state == 'continue':
            continue
        elif state == 'break':
            break

# print result
print()
print_board(board)
print()
if victor == '':
    print(' It\'s a draw!')
else:
    print(' ' + victor + ' wins!')
input()
