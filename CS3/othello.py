import turtle
import math
import copy

# * Test boards
# gameBoard = [
#     [0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 1,-1, 0, 0, 0, 0],
#     [0, 0,-1,-1, 1, 0, 0, 0],
#     [0, 1,-1, 1,-1, 0, 0, 0],
#     [0, 0, 0, 1, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0],
# ]
# gameBoard = [
#     [ 1,-1, 0, 0, 0, 0,-1, 1],
#     [-1,-1, 0, 0, 0, 0, 1, 0],
#     [ 0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0,-1, 1, 0, 0, 0],
#     [0, 0, 0, 1,-1, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0],
#     [ 0, 1, 0, 0, 0, 0,-1, 0],
#     [-1,-1, 0, 0, 0, 0,-1, 1],
# ]
# gameBoard = [
#     [ 1, 0, 0, 0, 0, 0, 0, 0],
#     [ 0,-1, 0, 0, 0, 0, 0, 0],
#     [ 0, 0,-1, 0, 0, 0, 0, 0],
#     [ 0, 0, 0,-1, 0, 0, 0, 0],
#     [ 0, 0, 0, 0,-1, 0, 0, 0],
#     [ 0, 0, 0, 0, 0,-1, 0, 0],
#     [ 0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0],
# ]

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
gameBoard = [
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0,-1, 1, 0, 0, 0],
    [0, 0, 0, 1,-1, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
]


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
    t.penup()
    for col in range(8):
        for row in range(8):
            # numbers
            t.goto(xFromColumn(col), yFromRow(row))
            t.write(f"{gameBoard[row][col]}", font=("Arial", 20, "normal"))

def whichColumn(x):
    return (x + kHalfBoard) // kCellSize

def whichRow(y):
    return -(y - kHalfBoard) // kCellSize

def xFromColumn(col):
    return  -kHalfBoard + kCellSize / 2 + col*kCellSize

def yFromRow(row):
    return kHalfBoard - kCellSize / 2 - row*kCellSize

# def test(x, y):
#     print(f"\nx,y: {x}, {y}\ncol,row: {whichColumn(x)}, {whichRow(y)}\ncalc x,y: {xFromColumn(whichColumn(x))}, {yFromRow(whichRow(y))}")

def stampPlayer(col, row, player):
    if col > 7 or row > 7 or col < 0 or row < 0:
        return
    t.penup()
    t.goto(xFromColumn(col), yFromRow(row))
    if player > 0:
        t.color('black')
    else:
        t.color('white')
    t.shape('circle')
    t.stamp()
    gameBoard[row][col] = player

def allMoves(board,player):
    moves_list = []
    for col in range(8):
        for row in range(8):
            piece = board[row][col]
            if piece != 0:
                continue
            
            cMin = -1
            cMax = 2
            if col == 0:
                cMin = 0
            elif col == 7:
                cMax = 1

            rMin = -1
            rMax = 2
            if row == 0:
                rMin = 0
            elif row == 7:
                rMax = 1
            
            # Look at surrounding squares (col & row -1 to +1) to see if any have your opponents color
            piece_surroundings = [[board[int(row + r)][int(col + c)] for c in range(cMin, cMax)] for r in range(rMin, rMax)]
            
            found = False
            for cAdd in range(cMin, cMax):
                if found:
                    break
                for rAdd in range(rMin, rMax):
                    if rAdd == 0 and cAdd == 0:
                        continue
                    if piece_surroundings[-rMin+rAdd][-cMin+cAdd] == -player:
                        if recursiveCheck(col, row, board, [cAdd, rAdd], player):
                            moves_list.append([row, col])
                            found = True
                            break
    return moves_list

# keep looking in that direction until you find a blank spot or your piece
def recursiveCheck(ogCol, ogRow, board, direction, player):
    new_col = ogCol + direction[0]
    new_row = ogRow + direction[1]
    if new_col > 7 or new_row > 7 or new_col < 0 or new_row < 0:
        return False
    next_piece = board[new_row][new_col]
    if next_piece == player:
        return True
    elif next_piece == -player:
        return recursiveCheck(new_col, new_row, board, direction, player)
    else:
        return False

def stampAllMoves(player):
    radius = 15
    for move in allMoves(gameBoard, player):
        t.penup()
        t.goto(xFromColumn(move[1]), yFromRow(move[0]) - radius)
        t.pencolor('black')
        t.pensize(1)
        t.pendown()
        t.circle(radius)

def validMove(player,row,col):
    if (row, col) in allMoves(gameBoard, player):
        return True
    return False

def nextBoard(board,player,move):
    new_board = copy.copy(board)
    
    row = move[0]
    col = move[1]
    
    cMin = -1
    cMax = 2
    if col == 0:
        cMin = 0
    elif col == 7:
        cMax = 1

    rMin = -1
    rMax = 2
    if row == 0:
        rMin = 0
    elif row == 7:
        rMax = 1
    
    # Look at surrounding squares (col & row -1 to +1) to see if any have your opponents color
    piece_surroundings = [[new_board[int(row + r)][int(col + c)] for c in range(cMin, cMax)] for r in range(rMin, rMax)]
    
    for cAdd in range(cMin, cMax):
        for rAdd in range(rMin, rMax):
            if rAdd == 0 and cAdd == 0:
                continue
            if piece_surroundings[-rMin+rAdd][-cMin+cAdd] == -player:
                recursiveCheckWithFlipping(col, row, new_board, [cAdd, rAdd], player)

    return new_board

# keep looking in that direction until you find a blank spot or your piece
def recursiveCheckWithFlipping(ogCol, ogRow, board, direction, player):
    new_col = ogCol + direction[0]
    new_row = ogRow + direction[1]
    if new_col > 7 or new_row > 7 or new_col < 0 or new_row < 0:
        return
    next_piece = board[new_row][new_col]
    if next_piece == -player:
        next_piece = player
        return recursiveCheck(new_col, new_row, board, direction, player)
    else:
        return

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
print(stampAllMoves(-1))
s.tracer(1)
# s.onclick(lambda x, y: stampPlayer(whichColumn(x), whichRow(y), 1))
turtle.mainloop()
