import turtle
import math
import copy


# Constants and Global Variables
'''
    black = 1
    white = -1
'''
kScreenSize = 600
kCellSize = 60
kBoardSize = 8*kCellSize # 480
currentPlayer = 1
gameBoard = []


# Turtle and Screen Initialization
t = turtle.Turtle()
s = turtle.Screen()
s.bgcolor('forest green')
s.setup(kScreenSize, kScreenSize)
# t.hideturtle()
s.tracer(0,0)

# Functions

def drawBoard():
    for i in range(9):
        # columns
        t.penup()
        t.goto(i*kCellSize-kBoardSize / 2, -kBoardSize / 2)
        t.pendown()
        t.goto(i*kCellSize-kBoardSize / 2, kBoardSize / 2)
        # rows
        t.penup()
        t.goto(-kBoardSize / 2, i*kCellSize-kBoardSize / 2)
        t.pendown()
        t.goto(kBoardSize / 2, i*kCellSize-kBoardSize / 2)
    pass

def whichRow(y):
    pass

def whichColumn(x):
    pass

def xFromColumn(col):
    pass

def yFromRow(row):
    pass

def stampPlayer(row, col, player):
    pass

def allMoves(board,player):
    pass

def stampAllMoveS(player):
    pass

def validMove(player,row,col):
    pass

def nextBoard(board,player,move):
    pass

def updateGameBoard(player,move):
    pass

def stampBoard():
    pass

def calculateScores(board):
    pass

def stampScores():
    pass

def initialize():
    pass

def playMove(x,y):
    pass

def evaluate(board):
    pass

def bestMove(board,player):
    pass

def MM(board, depth, alpha, beta, max, current, move):
    pass




# initialize()
drawBoard()
s.tracer(1)
turtle.mainloop()
