adj = [[0,1,0,0,1],[1,0,1,1,1],[0,1,0,1,0],[0,1,1,0,1],[1,1,0,1,0]]

def vertexDegree(vertex, graph):
    degreeCount = 0
    for degree in graph[vertex]:
        if degree != 0:
            degreeCount += 1
    return degreeCount

def numberOddDegreeVertices(graph):
    return len([v for v in adj if vertexDegree(graph.index(v), graph) % 2 != 0])

def neighborhood(vertex,graph):
    edges = graph[vertex]
    connections = []
    for i in range(len(edges)):
        edge = edges[i]
        if edge != 0:
            connections.append(i)
    return connections

print(neighborhood(1, adj))