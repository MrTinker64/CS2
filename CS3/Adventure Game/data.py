from classes import *

# Characters:

""" Your characters, e.g.:
parisa = Character('Parisa', 'Life is Math!')
"""
christina = Character('Christina', 'Sign in!')

# Things:
coffee = Thing('Coffee', 'The caffienated nectar of the gods.')

# Keys:
skeleton_key = Key('Skeleton Key', 'A key that unlocks many doors')

# (self, name, description, characters, things)

# Places:
front_desk = Place('Front Desk','I don\'t know why you say goodbye I say hello.', [christina], [coffee])

# Exits:
"""Your exits, e.g.:
front_desk.add_exits([admissions, conference_room, haight_street])
"""

# Locked places
"""Your locked places, e.g.:
front_desk.locked = False
"""

# Player:
me = Player('BYI',front_desk)