from classes import *

# Things:
lockbox = Thing('Lockbox', 'A locked box with 4 dials all set to 0')
remote_controller = Thing('Remote Controller', 'A circuit board with some 3D printed handholds and two small joysticks. You can\'t see any antenna but you\'re sure there is a connector somewhere in there.')
flashlight = Thing('Flashlight', 'After fiddling with the buttons for a little bit you figured out there are three modes: dim red, dim white, and bright white light.')
snacks = Thing('Snacks', 'Animal crackers, but they are shaped like +, -, ÷, x. M&M\'s with little punctuation marks on each one.')

# Keys:
gear_key = Key('Gear Key', 'A gear-shaped item that looks like it might unlock something.')

# Places:
path = Place('Path','A straight gravel path leading into the woods, it is about 10 ft wide. One either side of the tree-lined path you make out two large circular buildings 30 feet away.', [])
observatory = Place('Observatory','A round room with a large telescope in the middle 20 feet in diameter. On the wall you see a chart with instructions for how to see various celestial bodies.', [flashlight])
workshop = Place('Workshop','Another circular room 20 feet in diameter. The walls are lined with shelves full of part way finished projects and different tools. A remote controller is lying in the middle of a work table near you.', [remote_controller])

dining_room = Place('Dining Room','An ornately carved long room. Standing in the center it stretches 15 ft in either direction and is 10 ft wide.\nThere is a long table running down the middle and chairs all around it. A locked box sits in the middle of the table.\nTo your right is the kitchen, the left is a bedroom, ahead is a path into the woods, and behind is a beautiful lake.', [lockbox])
kitchen = Place('Kitchen','A clean, modern looking kitchen that is a 10x10 foot square with a door to your left. Lots of stainless-steel surfaces and spotless white tile floors. You check the cupboard and find some snacks.', [snacks])
pantry = Place('Pantry','The pantry is an isosceles right triangle with one short edge flush with the kitchen and the other on your left.\nThe shelves are full with dried and canned goods like flour, sugar, pickles, pears, etc. Amongst all the food you see a little glimmer of metal.', [gear_key])
guest_bedroom = Place('Guest Bedroom','A bedroom with a thank you note addressed to Mrs. G. Most of it is fluffy nice things, but you notice the guest emphasizing the odd and unique floorplan of this estate. The room goes 15ft in either direction and 10ft back.', [])

lake = Place('Lake','A path leads out about 10 feet to an oval shaped lake laying perpendicular to you. However, Lake might be a generous term as it is only 30 feet across and 50 feet long. On the far side of the lake is what looks like an artists studio, also 50 feet long.\nAs you walk along the path around the lake, you see something in the middle of the glittering lake. As you squint against the glare, it looks like a little toy boat.', [])
arch_studio = Place('Architecture Studio','Such a large space for architecture emphasizes the love Mrs. G had for it. All around there are cutting mats, sketches, and models. Most of the miniature buildings seem to resemble letters of the alphabet when viewed from above.\nAbout 10 feet in front of you, in the middle of the otherwise blank wall, you see a simple wooden door with no handle. You can also just make out another door, about 25 feet to your left, at the edge of studio leading in the same direction as this mysterious, handless door.', [])
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