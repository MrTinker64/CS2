from classes import *

# Things:
lockbox = Thing('Lockbox', 'A locked box with 4 dials all set to 0')
# TODO remote controller
# TODO toy boat with blue prints of this house that got water damaged so you can't make them out

# Keys:
skeleton_key = Key('Skeleton Key', 'A key that unlocks many doors')

# Places:
path = Place('Path','A straight gravel path from the dining room to the lake. Along the tree-lined path you make out two large circular buildings.', [])
observatory = Place('Observatory','A round room with a large telescope in the middle. On the wall you see a chart with instructions for how to see various celestial bodies.', [])
workshop = Place('Workshop','You see a remote controller lying on a shelf.', [])

dining_room = Place('Dining Room','A long room with a long table running down the middle and chairs running all along it. A locked box sits in the middle of the table.', [lockbox])
kitchen = Place('Kitchen','The kitchen', [])
pantry = Place('Pantry','A room shaped like a right triangle', [])
guest_bedroom = Place('Guest Bedroom','A bedroom with a thank you note addressed to Mrs. G.\nThe guest remarked about the unique floorplan of this estate.', [])

lake = Place('Lake','A path leads out about 10 feet to an oval shaped lake. You see something in the middle of the lake. When you squint closer it looks like a toyboat.', [])
arch_studio = Place('Architecture Studio','Collection of model buildings shaped like letters of the alphabet when viewed from above.', [])
storage_closet = Place('Storage Closet','', [])
zendo = Place('Zendo','', [])

# Exits:
# eight
path.add_exits([observatory, workshop, dining_room])

# one
dining_room.add_exits([guest_bedroom, kitchen])
kitchen.add_exits([pantry])

# zero
lake.add_exits([arch_studio, dining_room])

# nine
zendo.add_oneway_exits([arch_studio])
storage_closet.add_exits([arch_studio, zendo])


# Locked places
"""Your locked places, e.g.:
front_desk.locked = False
"""

# Player:
me = Player('Heir',dining_room)