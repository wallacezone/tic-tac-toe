# --------------------------------------------------------------------
#
# TIC TAC TOE with Python (v1.1)
#
# A simple game by Alessandro Barbieri
#
# https://github.com/wallacezone/tic-tac-toe
#
# --------------------------------------------------------------------

from random import randint
from sys import exit

# --------------------------- VARS & FUNCS ---------------------------

# count of victories
wins = {
    'X': 0,
    'O': 0
}

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

# input correspondences
in_corrs = {
    'TL': [0, 0], 'TM': [0, 1], 'TR': [0, 2],
    'ML': [1, 0], 'MM': [1, 1], 'MR': [1, 2],
    'LL': [2, 0], 'LM': [2, 1], 'LR': [2, 2]
}

# convert string input to list or viceversa depending on i_type arg
def convert_input(i, i_type):

    if i_type == 'string':

        # help
        if i == 'help':
            show_help()
            return [3,3]

        # exit
        if i == 'exit':
            print()
            exit(0)

        # convert input
        for key, value in in_corrs.items():
            if i == key:
                return value

        # if input is not valid
        return [3, 3]

    elif i_type == 'list':

        for key, value in in_corrs.items():
            if i == value:
                return key

# display the current board
def print_board(board):
    print('  ' + board[0][0] + ' | ' + board[0][1] + ' | ' + board[0][2])
    print(' ---+---+---')
    print('  ' + board[1][0] + ' | ' + board[1][1] + ' | ' + board[1][2])
    print(' ---+---+---')
    print('  ' + board[2][0] + ' | ' + board[2][1] + ' | ' + board[2][2])

# show help
def show_help():
    print()
    print(' Type the correspondent cell to move on that space:')
    print()
    print('  TL | TM | TR ')
    print(' ----+----+----')
    print('  ML | MM | MR ')
    print(' ----+----+----')
    print('  LL | LM | LR ')

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

    # if a corner is empty, fill it (choose a random corner) (only half times)
    r = randint(1,8)
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

    # print AI move
    print()
    print(' AI moved on ' + convert_input([x, y], 'list'))

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
    print(' Player: move on which space? (\'help\' to see moves, \'exit\' to ' +
        'exit)')
    print()
    move = input(' > ')

    # convert input
    x, y = convert_input(move, 'string')

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

# this func contains a single game
def game(board):
    # decide whether player or AI begins
    print()
    print(' You play X, AI plays O. Rolling dice to decide who begins...')
    begin = 'X' if randint(1,2) == 1 else '0'
    print()
    print(' ' + begin + ' begins!')

    # if AI begins, add just one AI turn at the beginning
    if begin == 'O':
        board, state, victor = ai_turn(board)

    # turn loop
    while True:

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

    # print result
    print()
    print_board(board)
    print()
    if victor == '':
        print(' It\'s a draw!')
    else:
        wins[victor] += 1
        print(' ' + victor + ' wins!')
    print()
    print(' Player has won ' + str(wins['X']) + ' time(s), AI has won ' + str(wins['O']) + ' time(s)')

# reset board
def reset_board(board):
    for x in range(3):
        for y in range(3):
            board[x][y] = ' '

# ------------------------------- MAIN -------------------------------

# title
print()
print(' ------ TIC TAC TOE with Python ------')
print()
print(' A simple game by Alessandro Barbieri')
print()
print(' Code available at: https://github.com/wallacezone/tic-tac-toe')

while True:

    # single game
    game(board)

    # check whether player wants to play again
    choice = ''
    while choice != 'y' and choice != 'n':
        print()
        print(' Do you want to play again? (y/n)')
        print()
        choice = input(' > ')
    if choice == 'y':
        reset_board(board)
        continue
    else:
        print()
        exit(0)



# TODO:
#
# - save num of victories in file
