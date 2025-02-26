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


graph = friends(5)
for line in graph:
    print(f"{line},")
