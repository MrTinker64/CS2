adj = [[0,1,0,0,1],[1,0,1,1,1],[0,1,0,1,0],[0,1,1,0,1],[1,1,0,1,0]]

def vertexDegree(vertex, graph):
    return sum(graph[vertex])

print(vertexDegree(1,adj))