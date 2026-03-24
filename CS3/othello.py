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
kHalfBoard = kBoardSize / 2
currentPlayer = 1
gameBoard = [[0,0,0,0,0,0,0,0], [0,0,0,0,0,0,0,0], [0,0,0,0,0,0,0,0], [0,0,0,0,0,0,0,0], [0,0,0,0,0,0,0,0], [0,0,0,0,0,0,0,0], [0,0,0,0,0,0,0,0], [0,0,0,0,0,0,0,0]]


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
        t.goto(i*kCellSize-kHalfBoard, -kHalfBoard)
        t.pendown()
        t.goto(i*kCellSize-kHalfBoard, kHalfBoard)
        # rows
        t.penup()
        t.goto(-kHalfBoard, i*kCellSize-kHalfBoard)
        t.pendown()
        t.goto(kHalfBoard, i*kCellSize-kHalfBoard)

def whichColumn(x):
    return (x + kHalfBoard) // kCellSize

def whichRow(y):
    return -(y - kHalfBoard) // kCellSize

def xFromColumn(col):
    return  -kHalfBoard + kCellSize / 2 + col*kCellSize

def yFromRow(row):
    return kHalfBoard - kCellSize / 2 - row*kCellSize

def test(x, y):
    print(f"\nx,y: {x}, {y}\ncol,row: {whichColumn(x)}, {whichRow(y)}\ncalc x,y: {xFromColumn(whichColumn(x))}, {yFromRow(whichRow(y))}")

def stampPlayer(col, row, player):
    t.penup()
    t.goto(xFromColumn(col), yFromRow(row))
    if player > 0:
        t.color('black')
    else:
        t.color('white')
    t.shape('circle')
    t.stamp()

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
# s.onclick(test)
# s.onclick(lambda x, y: stampPlayer(whichColumn(x), whichRow(y), 1))
turtle.mainloop()
