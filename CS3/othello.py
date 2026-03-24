import turtle
import math
import copy


# Constants and Global Variables
'''
    black = 1
    white = -1
'''
boardsize = 600
currentPlayer = 1
gameBoard = []


# Turtle and Screen Initialization
t = turtle.Turtle()
s = turtle.Screen()
s.bgcolor('forest green')
s.setup(boardsize, boardsize)
# t.hideturtle()
s.tracer(0,0)

# Functions

def drawBoard():
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




#s.tracer(1)
initialize()
