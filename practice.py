# og = list("hannah")
# reverseList = og.copy()
# reverseList.reverse()
# print(reverseList==og)

def isPalindrome(s):
    reverseList = list(s)
    reverseList.reverse()
    return list(s) == reverseList
    # if (len(list(s)) < 2):
    #     return True
    # elif (list(s)[0] == list(s)[-1]):
    #     return isPalindrome(''.join(list(s)[1:-1]))
    # else:
    #     return False

print(isPalindrome("racecar"))