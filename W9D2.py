adj = [[0,1,0,0,1],[1,0,1,1,1],[0,1,0,1,0],[0,1,1,0,1],[1,1,0,1,0]]

def vertexDegree(vertex, graph):
    return sum(graph[vertex])

def numberOddDegreeVertices(graph):
    return len([v for v in adj if vertexDegree(graph.index(v), graph) % 2 != 0])

print(numberOddDegreeVertices(adj))