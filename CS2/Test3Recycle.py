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
    if len(bills) < 2:
        return 1
    extra = 0
    if amount / bills[-1] >= 1:
        extra = floor(amount / bills[-1])
    return extra + count_change(amount, bills[:-1])


print(count_change(12, [1, 5, 10, 20]))
