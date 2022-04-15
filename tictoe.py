#tic tac toe, medo.
'''text func'''
from tracemalloc import stop
import random


def line():
    print ("------")

'''Importações e variáveis globais'''
board = ["-", "-", "-",
        "-", "-", "-",
        "-", "-", "-",]
currentPlayer = "X"
winner = None
gameRunning = True

#game board
def printBoard(board):

    print(board[0] + "|" + board[1] + "|" + board[2])
    line()
    print(board[3] + "|" + board[4] + "|" + board[5])
    line()
    print(board[6] + "|" + board[7] + "|" + board[8])

#player input
def playerInput (board):
    inp = int(input("Enter a number 1 - 9: "))
    if inp >= 1 and inp <= 9 and board[inp - 1] =="-":
        board[inp-1] = currentPlayer
    else:
        print ("W   R   O   N   G")
#check for win or tie
def checkHorizontal(board):
    global winner
    if board[0] == board[1] == board[2] and board[1] != "-":
        print ("Player " + currentPlayer + " Won!")
        winner = board[0]
        return True
    elif board[3] == board[4] == board[5] and board[3] != "-":
        print ("Player " + currentPlayer + " Won!")
        winner = board[0]
        return True
    elif board[6] == board[7] == board[8] and board[3] != "-":
        print ("Player " + currentPlayer + " Won!")
        winner = board[0]
        return True
###########
def checkRow(board):
    if board[0] == board[3] == board[6] and board[0] != "-":
        print ("Player " + currentPlayer + " Won!")
        winner = board[0]
        return True
    elif board[1] == board[4] == board[7] and board[1] != "-":
        print ("Player " + currentPlayer + " Won!")
        winner = board[1]
        return True
    elif board[2] == board[5] == board[8] and board[2] != "-":
        print ("Player " + currentPlayer + " Won!")
        winner = board[2]
        return True
    
###########
def checkDiag(board):
    if board[0] == board[4] == board[8] and board[0] != "-":
        print ("Player " + currentPlayer + " Won!")
        winner = board[0]
        return True
    elif board[2] == board[4] == board[6] and board[2] != "-":
        print ("Player " + currentPlayer + " Won!")
        winner = board[0]
        return True
def checkWin():
    if checkDiag(board) or checkHorizontal(board) or checkRow(board) == True:
        print(f"The Winner is {winner}")
    
    
    
#check tie
def checkTie(board):
    if "-" not in board:
        print ("TIE!")
        gameRunning = False
#switch the player
def switchPlayer():
    global currentPlayer
    if currentPlayer == "X":
        currentPlayer = "O"
    else:
        currentPlayer = "X"

### comp
def computer(board):
    while currentPlayer == "O":
        pos = random.randint(0,8)
        if board[pos] == "-":
            board[pos] = "O"
            switchPlayer()


#check for win or tie again

while gameRunning:
    printBoard(board)
    playerInput(board)
    checkWin()
    checkTie(board)
    switchPlayer()
    computer(board)
    checkWin()
    checkTie(board)
    if checkWin() == True:
        
        break

