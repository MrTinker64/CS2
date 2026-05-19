from classes import *

# Things:
lockbox = Thing('Lockbox', 'A locked box with 4 dials all set to 0')
remote_controller = Thing('Remote Controller', '') # TODO describe these two
flashlight = Thing('Flashlight', '')

# Keys:
gear_key = Key('Gear Key', 'A gear-shaped item that looks like it might unlock something.')

# Places:
path = Place('Path','A straight gravel path from the dining room to the lake. Along the tree-lined path you make out two large circular buildings.', [])
observatory = Place('Observatory','A round room with a large telescope in the middle. On the wall you see a chart with instructions for how to see various celestial bodies.', [flashlight])
workshop = Place('Workshop','You see a remote controller lying on a shelf.', [remote_controller])

dining_room = Place('Dining Room','A long room with a long table running down the middle and chairs running all along it. A locked box sits in the middle of the table.', [lockbox])
kitchen = Place('Kitchen','The kitchen', []) # TODO come up with some fun food descriptions. Maybe desserts shaped like punctuation?
pantry = Place('Pantry','A room shaped like a right triangle', [gear_key])
guest_bedroom = Place('Guest Bedroom','A bedroom with a thank you note addressed to Mrs. G.\nThe guest remarked about the unique floorplan of this estate.', [])

lake = Place('Lake','A path leads out about 10 feet to an oval shaped lake. You see something in the middle of the glittering lake. As you squint against the glare, it looks like a little toy boat.', [])
arch_studio = Place('Architecture Studio','Collection of model buildings shaped like letters of the alphabet when viewed from above.', [])
storage_closet = Place('Storage Closet','', []) # TODO describe. Messy, dusty, architecture supplies, foam core, markers and velum, rulers, wood, old models. Maybe a even a number shaped building???
zendo = Place('Zendo','', [])

# Exits:
# eight
path.add_exits([observatory, dining_room, workshop])

# one
dining_room.add_exits([kitchen, lake, guest_bedroom])
pantry.add_exits([kitchen])

# zero
lake.add_exits([arch_studio])

# nine
zendo.add_oneway_exits([arch_studio])
storage_closet.add_exits([arch_studio, zendo])


# Locked places
workshop.locked = True

# Player:
me = Player('Heir',dining_room)