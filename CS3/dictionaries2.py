def frequency(myString):
    new_dict = {}
    for letter in myString:
        if letter not in new_dict:
            new_dict[letter] = 0
        new_dict[letter] += 1
    return new_dict

print(frequency("abracadabra"))