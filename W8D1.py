'''
   Problem 1
'''
# Uncomment if you want them to run
# print([x * 2 for x in range(4) if x % 2 == 1]) # Output: [2, 6]
# print([letter for letter in 'Urban' if letter < 'm']) # Output: ['U', 'b', 'a']
# print("".join([letter for letter in 'Urban' if letter < 'm'])) # Output: Uba
# print("".join([word[0] for word in "Go Blues!".split() if not(len(word) == 2)])) # Output: B

'''
   Problem 2
'''
# print([word[0] for word in ['apple', 'banana', 'orange'] if len(word) > 5])


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
    return

# Code for Problems 5

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

'''
   Problem 6
'''
def applyFuncs(myList,n):
    #Your code here
    return

'''
   Problem 7
'''
def summation(n,f):
    #Your code here
    return

'''
   Problem 8
'''
def couple(list1,list2):
    #Your code here
    return

'''
   Problem 9
'''
def num_eights(number):
    #Your code here
    return



