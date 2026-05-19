from classes import *

# Things:
lockbox = Thing('Lockbox', 'A locked box with 4 dials all set to 0')
# TODO remote controller

# Keys:
skeleton_key = Key('Skeleton Key', 'A key that unlocks many doors')

# Places:
dining_room = Place('Dining Room','A long dining room with a locked box sitting in the middle of the table', [lockbox])
kitchen = Place('Kitchen','The kitchen', [])
pantry = Place('Pantry','A room shaped like a right triangle', [])
bedroom_one = Place('Master Bedroom','The master bedroom. You see a remote controller lying on a shelf.', [])
bedroom_two = Place('Guest Bedroom','A bedroom with a thank you note addressed to Mrs. G.\nThe guest remarked about the unique floorplan of this estate.', [])

path = Place('Path','A straight gravel path from the dining room to the lake. Along the tree-lined path you make out two large circular buildings.', [])
observatory = Place('Observatory','A round room with a large telescope in the middle. On the wall you see a chart with various planets and stars that **only rise during the early morning**. Each has a instructions next to it of how to see them.', [])

lake = Place('Lake','', [])
workshop = Place('Workshop','', [])
storage_closet = Place('Storage Closet','', [])
zendo = Place('Zendo','', [])

# Exits:
dining_room.add_exits([bedroom_one, bedroom_two, kitchen, path])
kitchen.add_exits([pantry])
path.add_exits([observatory])

# Locked places
"""Your locked places, e.g.:
front_desk.locked = False
"""

# Player:
me = Player('Heir',dining_room)