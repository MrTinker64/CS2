class_dict = {'Math':'1A', 'English': 'Shakespeare', 'CS':'3'}

# class_dict['Math'] = '1B'
# print(class_dict['Math'])

# print('Philosophy' in class_dict)
# print('10' in class_dict.values())
# print(class_dict.keys())

fav_numbers = {'Henri': 68, 'Richard': 19, 'Parisa': 42, 'Jessica': 4}
nums = [68, 42]

for person in fav_numbers:
    fav_numbers[person] += len(list(person))
    
print(fav_numbers)