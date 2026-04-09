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
s.setup(kScreenSize, kScreenSize)

t.penup()
t.hideturtle()
s.tracer(0)

# Functions

def drawBoard():
    s.tracer(0)
    s.bgcolor('forest green')
    t.color('black')
    for i in range(9):
        # columns
        t.goto(i*kCellSize-kHalfBoard, -kHalfBoard)
        t.pendown()
        t.goto(i*kCellSize-kHalfBoard, kHalfBoard)
        t.penup()
        # rows
        t.goto(-kHalfBoard, i*kCellSize-kHalfBoard)
        t.pendown()
        t.goto(kHalfBoard, i*kCellSize-kHalfBoard)
        t.penup()
    # for col in range(8):
    #     for row in range(8):
    #         # numbers
    #         t.goto(xFromColumn(col), yFromRow(row))
    #         t.write(f"{gameBoard[row][col]}", font=("Arial", 20, "normal"))

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
    t.goto(xFromColumn(col), yFromRow(row))
    if player > 0:
        t.color('black')
    else:
        t.color('white')
    t.dot(30)
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
    for move in allMoves(gameBoard, player):
        t.goto(xFromColumn(move[1]), yFromRow(move[0]))
        t.dot(30, 'black')
        t.dot(28, 'forest green')

def validMove(player,row,col):
    if [row, col] in allMoves(gameBoard, player):
        return True
    return False

def nextBoard(board,player,move):
    new_board = copy.deepcopy(board)
    
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

    new_board[int(row)][int(col)] = player
    return new_board

# keep looking in that direction until you find a blank spot or your piece
def recursiveCheckWithFlipping(ogCol, ogRow, board, direction, player):
    new_col = ogCol + direction[0]
    new_row = ogRow + direction[1]
    if new_col > 7 or new_row > 7 or new_col < 0 or new_row < 0:
        return False
    next_piece = board[int(new_row)][int(new_col)]
    if next_piece == player:
        return True
    elif next_piece == -player:
        if recursiveCheckWithFlipping(new_col, new_row, board, direction, player):
            board[int(new_row)][int(new_col)] = player
            return True
        return False
    else:
        return False

def updateGameBoard(player,move):
    global gameBoard
    gameBoard = nextBoard(gameBoard, player, move)

def stampBoard():
    for row in range(8):
        for col in range(8):
            player = gameBoard[row][col]
            if player != 0:
                stampPlayer(col, row, gameBoard[row][col])

def calculateScores(board):
    black_score = 0
    white_score = 0
    for row in range(8):
        for col in range(8):
            if board[row][col] == 1:
                black_score += 1
            if board[row][col] == -1:
                white_score += 1
    return [black_score, white_score]

def stampScores():
    scores = calculateScores(gameBoard)
    t.goto(-150, 260)
    t.color('black')
    t.write(scores[0], font=("Arial", 15, "normal"))
    t.goto(150, 260)
    t.color('white')
    t.write(scores[1], font=("Arial", 15, "normal"))
    
def stampCurrentPlayer():
    t.goto(0, 260)
    if currentPlayer > 0:
        t.color('black')
        t.write(f"black's move", align="center", font=("Arial", 15, "normal"))
    else:
        t.color('white')
        t.write(f"white's move", align="center", font=("Arial", 15, "normal"))

def initialize():
    global gameBoard
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
    drawBoard()
    stampBoard()
    stampScores()
    # update current player if needed
    stampAllMoves(currentPlayer)
    stampCurrentPlayer()
    s.update()

def playMove(x,y):
    turtle.onscreenclick(None) # type: ignore
    global currentPlayer
    col = whichColumn(x)
    row = whichRow(y)
    t.clear()
    if validMove(currentPlayer,row, col):
        updateGameBoard(currentPlayer, [row, col])
        currentPlayer *= -1
        if len(allMoves(gameBoard, currentPlayer)) == 0:
            currentPlayer *= -1
        else:
            stampCurrentPlayer()
        if currentPlayer == -1:
            computer_move = bestMove(gameBoard, currentPlayer)
            playMove(xFromColumn(computer_move[1]), yFromRow(computer_move[0]))
            return
    else:
        t.goto(0, 260)
        t.color('red')
        t.write(f"invalid move", align="center", font=("Arial", 15, "normal"))
        turtle.onscreenclick(playMove)
    drawBoard()
    stampScores()
    stampBoard()
    stampAllMoves(currentPlayer)
    print(currentPlayer)
    print(bestMove(gameBoard, currentPlayer))
    s.update()
    turtle.onscreenclick(playMove)

def evaluate(board, player):
    return calculateScores(board)[int((1-player)/2)]

def bestMove(board,player):
    best_move = [0, 0]
    best_score = 0
    for move in allMoves(board, player):
        move_score = evaluate(nextBoard(board, player, move), player)
        if move_score > best_score:
            best_move = move
            best_score = move_score
    return best_move

def MM(board, depth, max, current, move):
    moves = allMoves(board, current)
    opponent = -current
    opp_moves = allMoves(board, opponent)
    
    if depth is 0 or (len(moves) == 0 and len(opp_moves) == 0):
        return [evaluate(board, current), None]

    if len(moves) == 0:
        MM(board, depth - 1, not max, opponent, move)

    best_move = None

    if max:
        best_value = -10000
        for m in moves:
            nBoard = nextBoard(board, current, m)
            mmOnBoard = MM(nBoard, depth - 1, not max, opponent, move)
            if mmOnBoard[1] > best_value:
                best_value = mmOnBoard[1]
                best_move = mmOnBoard[0]
        return [best_move, best_value]

    if not max:
        best_value = 10000
        for m in moves:
            nBoard = nextBoard(board, current, m)
            mmOnBoard = MM(nBoard, depth - 1, max, opponent, move)
            if mmOnBoard[1] < best_value:
                best_value = mmOnBoard[1]
                best_move = mmOnBoard[0]
        return [best_move, best_value]




initialize()
turtle.onscreenclick(playMove)
turtle.mainloop()
