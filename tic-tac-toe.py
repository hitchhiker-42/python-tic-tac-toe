# Author: Jaehee Hong, SNUCSE (Dept. of Computer Science and Engineering, Seoul National University)
# A simple tic-tac-toe game created for UPnL noob assignment.

"""
Board saves the status of the game by using the list.
-1 indicates empty space, 0 indicates the space occupied by the player,
10 indicates the space occupied by the computer.
"""
from random import randint
from time import sleep

board = [-1, -1, -1, -1, -1, -1, -1, -1, -1]

welcome = """Welcome to a simple tic-tac-toe game!
This game was created for UPnL noob assignment.

Author: Jaehee Hong
"""

initial_stauts = """Current Status:
You: O, Computer: X, Empty: -
| - | - | - |
| - | - | - |
| - | - | - |

"""

prompt = """YOUR TURN!
Press the corresponding key to select the space.
| 0 | 1 | 2 |
| 3 | 4 | 5 |
| 6 | 7 | 8 |
"""

# -1 means there's no winner yet, 0 means the player won, 1 means the computer won
win = -1

# Read values from the board and display it.
def board_print(board):
    board_text = ""
    for i in range(0, 9, 3):
        board_text += "|"
        for j in range(3):
            if board[i + j] == 0:
                board_text += " O |"
            elif board[i + j] == 10:
                board_text += " X |"
            else:
                board_text += " - |"
        board_text += "\n"

    print("Current status:")
    print("You: O, Computer: X, Empty: -")
    print(board_text)

# Checks if there's a winner
def check_win(board):
    row1 = board[0] + board[1] + board[2]
    row2 = board[3] + board[4] + board[5]
    row3 = board[6] + board[7] + board[8]
    col1 = board[0] + board[3] + board[6]
    col2 = board[1] + board[4] + board[7]
    col3 = board[2] + board[5] + board[8]
    diag_dr = board[0] + board[4] + board[8]
    diag_dl = board[2] + board[4] + board[6]

    if row1 == 0 or row2 == 0 or row3 == 0 or col1 == 0 or col2 == 0 or col3 == 0 or diag_dr == 0 or diag_dl == 0:
        return 0
    elif row1 == 30 or row2 == 30 or row3 == 30 or col1 == 30 or col2 == 30 or col3 == 30 or diag_dr == 30 or diag_dl == 30:
        return 1
    else:
        return -1

def player_turn(board):
    while True:
        print(prompt)
        try:
            player_input = int(input("Input your next move: "))
            if board[player_input] == -1:
                board[player_input] = 0
                break
            else:
                print("ERROR!\nYou chose an already occupied space!\n")
                board_print(board)
        except:
            print("INVALID INPUT! You chose an invalid space.\n")
            board_print(board)

def computer_turn(board):
    while True:
        computer_input = randint(0, 8)
        if board[computer_input] == -1:
            computer_msg = "COMPUTER'S TURN..."
            for i in range(len(computer_msg)):
                print(computer_msg[i], sep=' ', end=' ', flush=True); sleep(0.1)
            board[computer_input] = 10
            break

# Prompt for the end of the game
def endgame():
    if win == 0:
        win_msg = "YOU WIN!"
        for i in range(len(win_msg)):
            print(win_msg[i], sep=' ', end=' ', flush=True); sleep(0.3)
    elif win == 1:
        lose_msg = "YOU LOSE!"
        for i in range(len(lose_msg)):
            print(lose_msg[i], sep=' ', end=' ', flush=True); sleep(0.3)

# This part displays the actual game
print(welcome)
print(initial_stauts)

while True:
    player_turn(board)
    board_print(board)
    win = check_win(board)
    if win != -1:
        break
    computer_turn(board)
    board_print(board)
    win = check_win(board)
    if win != -1:
        break

endgame()