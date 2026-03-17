A = [[1, 2], [3, 4]]
B = [[5, 6], [7, 8]]
L = [[9, -18, 27], [36, 55, 54]]
D = [[1], [2]]

def add(X, Y):
    return [[X[i][j] + Y[i][j] for j in range(len(X))] for i in range(len(X))]

def subtract(X, Y):
    return [[X[i][j] - Y[i][j] for j in range(len(X))] for i in range(len(X))]

def scalarMulitply(c, X):
    return [[c*X[i][j] for j in range(len(X))] for i in range(len(X))]

def mulitply(X, Y):
    rMax = len(X[0]) - 1
    return [[X[r][0]*Y[0][c] + X[r][rMax]*Y[rMax][c] for c in range(len(Y[0]))] for r in range(len(X))]

def transpose(X):
    return [[X[c][r] for c in range(len(X))] for r in range(len(X[0]))]

print(mulitply(A, D))