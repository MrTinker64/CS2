class_dict = {'Math':'1A', 'English': 'Shakespeare', 'CS':'3'}

# class_dict['Math'] = '1B'
# print(class_dict['Math'])

# print('Philosophy' in class_dict)
# print('10' in class_dict.values())
# print(class_dict.keys())

fav_numbers = {'Henri': 68, 'Richard': 19, 'Parisa': 42, 'Jessica': 4}
nums = [68, 42]

# for person in fav_numbers:
#     fav_numbers[person] += len(list(person))
    
# print([person for person in fav_numbers if nums.__contains__(fav_numbers[person])])

dictA = {'Dan':3, 'Charlotte': 15}
dictB = {'Lauren': 3, 'Charlotte': -1, 'Dan': 2}

def merge_dicts(dict1, dict2):
    newDict = dict1.copy()
    for key, val in dict2.items():
        newDict[key] = newDict.get(key, 0) + val
    return newDict
        
# print(merge_dicts(dictA, dictB))

"""
a. 4
b. ['fruit', 'veggie', 'beverage', 'grain']
c. error
d. true and false
e. true and true
f. nothing. you need to do food_dict[food]

8. an empty list bc copy is just a reference to food_dict not an actual copy
9. error bc you can't have a dictionary key/value pairing as a value
"""