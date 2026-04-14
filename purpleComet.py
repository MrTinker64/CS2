import random

count = 0
special = 0

while count < 100000:
    mySet = []
    papers = ['r', 'r', 'r', 'w', 'w', 'w', 'b', 'b', 'b']
    stickers = ['p', 'p', 'p', 'y', 'y', 'y', 'b', 'b', 'b']
    combinations = [['r', 'p'], ['r', 'y'], ['r', 'b'], ['w', 'p'], ['w', 'y'], ['w', 'b'], ['b', 'p'], ['b', 'y'], ['b', 'b']]
    for i in range(9):
        n = 8 - i
        p = random.randint(0, n)
        s = random.randint(0, n)
        combo = [papers.pop(p), stickers.pop(s)]
        mySet.append(combo)
        try:
            combinations.remove(combo)
        except ValueError:
            count += 1
            break
    if len(combinations) == 0:
        special += 1
    count += 1

print(f"sp {special}, ct {count}, ratio {special/count}")

# 69 / 1000