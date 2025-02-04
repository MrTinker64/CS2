'''
   Problem 1
'''
print([x * 2 for x in range(4) if x % 2 == 1]) # [2, 6]
print([letter for letter in 'Urban' if letter < 'm']) # ['U', 'b', 'a']
print("".join([letter for letter in 'Urban' if letter < 'm'])) # Uba
print("".join([word[0] for word in "Go Blues!".split() if not(len(word) == 2)])) # B

'''
   Problem 2
'''
#Your code here


'''
   Problem 3
'''
#Your code here

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



