import random

adj = [[0,1,0,0,1],[1,0,1,1,1],[0,1,0,1,0],[0,1,1,0,1],[1,1,0,1,0]]

def vertexDegree(vertex, graph):
    degreeCount = 0
    for degree in graph[vertex]:
        if degree != 0:
            degreeCount += 1
    return degreeCount

def numberOddDegreeVertices(graph):
    return len([v for v in range(len(adj)) if vertexDegree(v, graph) % 2 != 0])

def neighborhood(vertex,graph):
    edges = graph[vertex]
    connections = []
    for i in range(len(edges)):
        edge = edges[i]
        if edge != 0:
            connections.append(i)
    return connections

def isWalk(a, b, graph):
    if graph[a][b] != 0:
        return True
    else:
        for v in neighborhood(a, graph):
            if graph[v][b] != 0:
                return True
    return False

def generateGraph(n):
    graph = []
    for i in range(n):
        if i == 0:
            graph = [[0] + [random.randrange(0, 2, 1) for _ in range(n-1)]]
        else:
            graph += [[v[i] for v in graph] + [0] + [random.randrange(0, 2, 1) for _ in range(n-i-1)]]
    return graph

def isClique(cq, graph):
    for vertex in cq:
        neighbors = neighborhood(vertex, graph)
        for v in cq:
            if neighbors.count(v) < 1 and v != vertex:
                return False
    return True

def generateDirectedGraph(n):
    graph = []
    for i in range(n):
        if i == 0:
            graph = [[0] + [random.randrange(0, 2, 1) for _ in range(n-1)]]
        else:
            graph += [[random.randrange(0, 2, 1) for _ in range(i)] + [0] + [random.randrange(0, 2, 1) for _ in range(n-i-1)]]
    return graph

print(generateDirectedGraph(4))