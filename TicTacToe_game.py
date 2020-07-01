import random
import time

# Function that prints out board.

board = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']


def display_board(board):
    print(board[7]+'|'+ board[8]+'|'+ board[9])
    print('-----')
    print(board[4]+'|'+ board[5] +'|'+ board[6])
    print('-----')
    print(board[1]+'|'+ board[2]+'|'+ board[3])


# Function that takes in a player input and assign their marker as 'X' or 'O'.


def player_input():
    player1 = ''
    player2 = ''

    while (player1 != 'X') and (player1 != 'O'):
        player1 = input("Player 1 please pick a marker 'X' or 'O' ")

        if player1 == 'X':
            player2 = 'O'
        elif player1 == 'O':
            player2 = 'X'

    print("\n"+f"Player 1 is {player1} and Player 2 is {player2}")

    return player1,player2


# Function that takes in the board list object, a marker ('X' or 'O'), and a desired position (number 1-9)
# and assigns it to the board.

def place_marker(board, marker, position):

    index = int(position)
    board.pop(index)
    board.insert(index,marker)

# Function that takes in a board and a mark (X or O) and then checks to see if that mark has won.


def win_check(board, mark):

    if board[7] == board[8] == board[9] == mark:
        return True
    elif board[4] == board[5] == board[6] == mark:
        return True
    elif board[1] == board[2] == board[3] == mark:
        return True
    elif board[7] == board[4] == board[1] == mark:
        return True
    elif board[8] == board[5] == board[2] == mark:
        return True
    elif board[9] == board[6] == board[3] == mark:
        return True
    elif board[7] == board[5] == board[3] == mark:
        return True
    elif board[9] == board[5] == board[1] == mark:
        return True

    else:
        return False


# Function that randomly decides which player goes first.


def choose_first():
    goes_first = random.randint(1, 2)

    if goes_first == 1:
        print('\n'+'Player 1 goes first')
    else:
        print('\n'+'Player 2 goes first')

    return goes_first


# Function that returns a boolean indicating whether a space on the board is freely available.

def space_check(board, position):

    if str(position) in board:
        return True
    else:
        return False


# Function that checks if the board is full and returns a boolean value. True if full, False otherwise.


def full_board_check(board):

    for i in range(1,10):
        if space_check(board, i):
            return False
    return True


# Function that asks for a player's next position. Using the space_check function to check if the position
# is available


def player_choice(board):

    position = int(input('\n'+'Place your marker: '))
    if space_check(board,position) == True:
        place_marker(board, marker, position)
    else:
        print('Position taken please try again ')
        position = int(input('\n'+'Place your marker: '))
        place_marker(board, marker, position)


# Function that asks the player if they want to play again and
# returns a boolean True if they do want to play again.

def replay():

    ask = input('\n'+'Do you want to play again? Y/N ')
    if ask.upper() == 'Y':
        return True
    else:
        print("\n"*100)
        print('\n'+'Thank you for playing!')
        return False


# Code to run the game:

while True:

    board = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    print('Welcome to Tic Tac Toe! \n')
    time.sleep(1)
    print('Please decide who is Player 1 and who is Player 2 \n')

    time.sleep(5)
    player1_marker, player2_marker = player_input()
    time.sleep(1)
    goes_first = choose_first()
    time.sleep(1)
    print("\n"+"GAME START!")
    time.sleep(2)
    print('\n'*100)
    display_board(board)

    game_on = True
    if not game_on:
        print('\n' * 100)
        break

    while game_on:

        player1_turn = True
        while True:

            if goes_first == 1:
                marker = player1_marker
            elif goes_first == 2:
                marker = player2_marker

            if game_on == True:
                player_choice(board)
                print('\n'*100)
                display_board(board)

            if win_check(board, marker):
                print('\n'+'BOOYA you have won!!')
                game_on = False

            if full_board_check(board) and not win_check(board, marker):
                print('\n'*100)
                print('\n'+"GAME OVER!! It's a tie!")
                game_on = False
            break

        player2_turn = True
        while True:

            if goes_first == 1:
                marker = player2_marker
            elif goes_first == 2:
                marker = player1_marker

            if game_on == True:
                player_choice(board)
                print('\n'*100)
                display_board(board)

            if win_check(board, marker):
                print('\n'+'BOOYA you have won!!')
                game_on = False

            if full_board_check(board) and not win_check(board, marker):
                print('\n'*100)
                print('\n'+"GAME OVER!! It's a tie!")
                game_on = False
            break

    if not replay():
        game_on = False
        break
    else:
        print('\n'*100)
        continue

