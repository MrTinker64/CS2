'''
   Problem 1
'''
print([x * 2 for x in range(4) if x % 2 == 1]) # Output: [2, 6]
print([letter for letter in 'Urban' if letter < 'm']) # Output: ['U', 'b', 'a']
print("".join([letter for letter in 'Urban' if letter < 'm'])) # Output: Uba
print("".join([word[0] for word in "Go Blues!".split() if not(len(word) == 2)])) # Output: B

'''
   Problem 2
'''
print([word[0] for word in ['apple', 'banana', 'orange'] if len(word) > 5])


'''
   Problem 3
'''
nums = [3, 42]
fav_nums = [['Richard',3],['Scott',20],['Parisa',42],['Raj',20]]
print([teacher[0] for teacher in fav_nums if teacher[1] in nums])

'''
   Problem 4
'''
def mySum(myList):
    return [sum(nums) for nums in myList]
print(mySum([[1,2],[-5,4]]))

'''
   Problem 5
'''
def subtractor(x):
    def inner(y):
        return x-y
    return inner


def myFunc(x):
    def rev(y):
        if len(y)==0:
            return x
        else:
            return y[-1]+rev(y[:-1])
    return rev

print(subtractor(6)(5))
print(myFunc('way')('Urban'))

'''
   Problem 6
'''
def applyFuncs(myList,n):
    return [func(n) for func in myList]

print(applyFuncs([lambda x: x + x, lambda x: x*x],4))

'''
   Problem 7
'''
def summation(n,f):
    return sum([f(num) for num in range(1,n+1)])

print(summation(5, lambda x: x * x * x))
print(summation(9, lambda x: x + 1))

'''
   Problem 8
'''
def couple(list1,list2):
    return [[item, list2[list1.index(item)]] for item in list1]

print(couple([1,2,3],[4,5,6]))

'''
   Problem 9
'''
def num_eights(numIn):
    n = [int(digit) for digit in str(numIn)]
    extra = 0
    if n[0] == 8:
        extra = 1
    if len(n) < 2:
        return extra
    return extra + num_eights(int("".join(map(str, n[1:]))))

print(num_eights(3))
print(num_eights(8))
print(num_eights(88888888))
print(num_eights(2638))