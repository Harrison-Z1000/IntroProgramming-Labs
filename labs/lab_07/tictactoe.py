# CMPT 120 Intro to Programming
# Lab #7 - Tic-Tac-Toe Game
# Author: Harrison Zheng
# Date: 2019-11-6


def printRow(board, row):
    # Prints a row of the board based on the value in each square
    # Player 1 is represented with x, player 2 with o, and 0 denotes a blank square
    print("|", end='')
    for square in range(len(board[row])):
        numberInSquare = board[row][square]
        if numberInSquare == 0:
            print("   ", end='|')
        elif numberInSquare == 1:
            print(" x ", end='|')
        elif numberInSquare == 2:
            print(" o ", end='|')
        else:
            print("Invalid input")
    print(" ")
    pass


def printBoard(board):
    # Prints the board one row at a time with a border above and below each
    topBorder = "+-----------+"
    print(topBorder)
    for row in range(len(board)):
        printRow(board, row)
        print(topBorder)
    pass


def markBoard(board, row, col, player):
    # Checks whether the desired square is blank
    if board[row][col] == 0:
        board[row][col] = player
    else:
        print("This square is taken.")
        # If the square is filled, the computer will ask the user to pick another one
        row, col = getPlayerMove()
        markBoard(board, row, col, player)
    pass


def getPlayerMove():
    row = int(input("Enter the row number (the tic-tac-toe board is 3X3): "))
    column = int(input("Enter the column number (the tic-tac-toe board is 3X3): "))
    # Most people will enter '1' and not '0' when referring to the first row so 1 needs to be subtracted from the
    # user's input
    return (row - 1), (column - 1)


def hasBlanks(board):
    # Checks if there are any blank squares on the board
    for row in range(len(board)):
        for square in range(len(board[row])):
            if board[row][square] == 0:
                return True
            elif board[0][0] != 0:
                continue
            else:
                return False


def completeRow(board, player):
    # Checks whether the player who made the last move won by filling a row
    if board[0][0] == player and board[0][1] == player and board[0][2] == player:
        return True
    elif board[1][0] == player and board[1][1] == player and board[1][2] == player:
        return True
    elif board[2][0] == player and board[2][1] == player and board[2][2] == player:
        return True
    else:
        return False


def completeCol(board, player):
    # Checks whether the player who made the last move won by filling a column
    if board[0][0] == player and board[1][0] == player and board[2][0] == player:
        return True
    elif board[0][1] == player and board[1][1] == player and board[2][1] == player:
        return True
    elif board[0][2] == player and board[1][2] == player and board[2][2] == player:
        return True
    else:
        return False


def completeDiag(board, player):
    # Checks whether the player who made the last move won by filling a diagonal
    if board[0][0] == player and board[1][1] == player and board[2][2] == player:
        return True
    elif board[0][2] == player and board[1][1] == player and board[2][0] == player:
        return True
    else:
        return False


def checkWinner(board, player):
    # If the player who made the last move won, the computer prints a message and exits the game
    if completeRow(board, player):
        print("Congratulations Player", player, "! You won !")
        raise SystemExit
    elif completeCol(board, player):
        print("Congratulations Player", player, "! You won !")
        raise SystemExit
    elif completeDiag(board, player):
        print("Congratulations Player", player, "! You won !")
        raise SystemExit
    else:
        pass


def main():
    board = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    player = 1
    while hasBlanks(board):
        printBoard(board)
        row, col = getPlayerMove()
        markBoard(board, row, col, player)
        checkWinner(board, player)
        # Switches player for next turn
        player = player % 2 + 1


main()
