from classes import *

# Things:
lockbox = Thing('Lockbox', 'A locked box with 4 dials all set to 0')

# Keys:
skeleton_key = Key('Skeleton Key', 'A key that unlocks many doors')

# Places:
first_room = Place('First Room','A long dining room with a locked box sitting in the middle of the table', [], [lockbox])
kitchen = Place('Kitchen','The kitchen', [], [])
pantry = Place('Pantry','A room shaped like a right triangle', [], [])
bedroom_one = Place('Bedroom 1','A bedroom with a remote controller.', [], [])
bedroom_two = Place('Bedroom 2','A bedroom with a thank you note addressed to Mrs. G.\nThe guest remarked about the unique floorplan of this estate.', [], [])

# Exits:
first_room.add_exits([bedroom_one, bedroom_two, kitchen])
kitchen.add_exits([pantry])

# Locked places
"""Your locked places, e.g.:
front_desk.locked = False
"""

# Player:
me = Player('Heir',first_room)