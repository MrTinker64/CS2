from classes import *

# Characters:

""" Your characters, e.g.:
parisa = Character('Parisa', 'Life is Math!')
christina = Character('Christina', 'Sign in!')
"""

# Things:
""" Your things, e.g.: 
coffee = Thing('Coffee', 'The caffienated nectar of the gods.')
"""

# Keys:
try:
    skeleton_key = Key('Skeleton Key', 'A key that unlocks many doors')
except NameError as e:
    skeleton_key = Thing('Not a Skeleton Key', 'You must first implement the Key class')


# Places:
""" Your places, e.g:
front_desk = Place('Front Desk','I don\'t know why you say goodbye I say hello.', [christina], ['trivia question board'])
"""




# Exits:
"""Your exits, e.g.:
front_desk.add_exits([admissions, conference_room, haight_street])
"""

# Locked places
"""Your locked places, e.g.:
front_desk.locked = False
"""


# Player:
"""Initialize your player, e.g.:
me = Player('BYI',front_desk)
"""


