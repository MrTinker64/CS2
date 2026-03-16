A = [[1, 2], [3, 4]]
B = [[5, 6], [7, 8]]
L = [[9, -18, 27], [36, 55, 54]]

def add(X, Y):
    return [[X[i][j] + Y[i][j] for j in range(len(X))] for i in range(len(X))]

print(add(A, B))