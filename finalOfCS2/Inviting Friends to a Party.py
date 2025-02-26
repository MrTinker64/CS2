import random


def friends(n):
    graph = []
    for i in range(n):
        if i == 0:
            graph = [[0] + randomWeights(n - 1)]
        else:
            graph += [randomWeights(i) + [0] + randomWeights(n - i - 1)]
    return graph


def randomWeights(i) -> list:
    return [random.randint(0, 1) for _ in range(i)]


def isClique(cq, graph):
    for vertex in cq:
        neighbors = neighborhood(vertex, graph)
        for v in cq:
            if neighbors.count(v) < 1 and v != vertex:
                return False
    return True


def neighborhood(vertex, graph):
    edges = graph[vertex]
    connections = []
    for i in range(len(edges)):
        edge = edges[i]
        if edge != 0:
            connections.append(i)
    return connections


graph = friends(3)
for line in graph:
    print(f"{line},")

cq = [0, 1, 2]

print(f"Is {cq} clique: {isClique(cq, graph)}")
