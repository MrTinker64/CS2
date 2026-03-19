def frequency(myString):
    new_dict = {}
    for letter in myString:
        if letter not in new_dict:
            new_dict[letter] = 0
        new_dict[letter] += 1
    return new_dict

print(frequency("abracadabra"))

def most_freq_seq(myString, length):
    seqs = [myString[i:i + length] for i in range(len(myString) - length + 1)]
    counts = frequency(seqs)
    best = ""
    best_count = 0
    for seq in counts:
        if counts[seq] > best_count:
            best_count = counts[seq]
            best = seq
    return best

#print(most_freq_seq("abracadabra", 4))

def substitute_chars(myString, myDict):
    result = ""
    for char in myString:
        result += myDict.get(char, char)
    return result

#replacements = {'S':'Z', 'E':'U', 'T':'P', 'A':'M'}
#print(substitute_chars("SECRET MESSAGE",replacements))

def invert_dict(myDict):
    new_dict = {}
    for key in myDict:
        new_dict[myDict[key]] = key
    return new_dict

original = {'a': 5, 'b': 2, 'c': 1}
# print(invert_dict(original))
# print(original)

print(invert_dict(frequency("abracadabra")))

'''
{'a': 5, 'b': 2, 'r': 2, 'c': 1, 'd': 1}
{5: 'a', 2: 'r', 1: 'd'}
5. it overwrites the previous value. Because both "b" and "r" correspond to 2 the code first sets 2:"b" and then overwrites that with 2:"r"
6. M was never changed by the substitution, therefore the inverted substitution accidentally changes it. the only way to get around this is to make sure the keys contain all values and the values contain all keys
'''