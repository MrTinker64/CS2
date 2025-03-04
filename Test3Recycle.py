from math import floor


def f2(N):
    if N == 1:
        return 1
    else:
        return f2(N / 2)


""" 
7a Algorithm 3 = O(n)
n/2, n/4, n/8 ... geometric series
7b Algorithm 3 = O(n)
"""


def swap_values(A, B):
    A = B
    B = A


me = 20
you = 50
swap_values(me, you)
print(me)  # 20


def b(word):
    return word + word


print(b(b(2)))  # 8


def mystery(n, lst):
    return list(filter(lambda x: not lst[n][x] == 0, range(len(lst))))


print(mystery(2, [[0, 1, 1], [1, 0, 1], [1, 1, 0]]))  # [0, 2]


def count_change(amount, bills):
    if len(bills) < 1:
        return 0
    elif amount % bills[-1] == 0:
        return 1 + count_change(amount, bills[:-1])
    elif amount % bills[-1] >= amount:
        return count_change(amount, bills[:-1])
    else:
        combinations = 0
        for n in range(floor(amount / bills[-1])):
            leftover = amount % bills[-1] + bills[-1] * n
            for bill in bills[:-1]:
                if leftover % bill == 0:
                    combinations += 1
        return combinations + count_change(amount, bills[:-1])


print(count_change(12, [1, 5, 10, 20]))
