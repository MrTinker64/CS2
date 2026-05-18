from classes import *

# Characters:

""" Your characters, e.g.:
parisa = Character('Parisa', 'Life is Math!')
"""
christina = Character('Christina', 'Sign in!')

# Things:
coffee = Thing('Coffee', 'The caffienated nectar of the gods.')
lockbox = Thing('Lockbox', 'A locked box with 4 dials all set to 0')

# Keys:
skeleton_key = Key('Skeleton Key', 'A key that unlocks many doors')

# (self, name, description, characters, things)

# Places:
front_desk = Place('Front Desk','I don\'t know why you say goodbye I say hello.', [christina], [coffee])
first_room = Place('First Room','I don\'t know why you say goodbye I say hello.', [], [lockbox])

# Exits:
first_room.add_exits([front_desk])

# Locked places
"""Your locked places, e.g.:
front_desk.locked = False
"""

# Player:
me = Player('Heir',first_room)