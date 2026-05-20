# A "simple" adventure game.

class Player:
    def __init__(self, name, place):
        """Create a player object."""
        self.name = name
        self.place = place
        self.backpack = []
        self.won = False
        self.night_time = True
        self.hasFlashlight = False

    def look(self):
        # TODO demonstrate it's night vs day time at the Path and the Lake
        print('You are currently in the ' + self.place.name, end=". ")
        if self.place.name == 'Closet':
            if not any(item.name == 'Flashlight' for item in self.backpack):
                print("The room is too dark to see in and the only light has broken.")
                return
            else:
                print("The room is too dark to see in and the only light bulb has broken.\nLuckily, you picked up the flashlight from earlier. You turn on your flashlight and it illuminates:")
        else:
            print("You take a look around and see:")
        if self.place.name == 'Observatory' and self.night_time:
            print()
            print("Now that it is the early morning you are able to look through the telescope at the celestial objects listed on the wall.\nEventually you see an odd pattern emerging in the objects you're looking at.\nFirst you saw lots of double star clusters and binary stars which looked like an 8.\nFurther down the list there was a variety thin or cigar-shaped galaxies reminding you of a 1.\nBy the time you're done watching both the room, and your brain, have been enlightened.")
        if self.place.name == 'Lake' and any(item.name == 'RC' for item in self.backpack):
            print()
            print("You use the remote controller to drive the toy boat over to you. Sitting inside are some blueprints.\nThe blue prints seem to be for the very estate that your standing on.\nThough the left half has been damaged by water you can make out the lake and architecture studio on the right half of the sheet.\nFrom the top-down view of the blueprint they look like a 0 and a 9.")
        print()
        if isinstance(self.place, Outside_Place) and self.night_time:
            self.place.look_at_night()
        else:
            self.place.look()

    def go_to(self, location):
        """Go to a location if it's among the exits of player's current place and it is unlocked."""
        if type(location) != str:
            print('Location has to be a string.')
            return
        destination = self.place.get_neighbor(location)
        if destination is not self.place:
            if destination.locked:
                print(destination.name + ' is locked! You need to unlock it first.')
            else:
                self.place = destination
                self.look()


    def take(self, thing):
        """Take a thing if thing is at player's current place
        """
        if type(thing) != str:
            print('Thing should be a string.')
            return
        if thing in self.place.things:
            item = self.place.take(thing)
            self.backpack.append(item)
            print('You take the ' + item.name + '.')
            if item.name == 'Flashlight':
                self.hasFlashlight = True
        else:
            print(thing + ' is not here.')

    def check_backpack(self):
        """Print each item with its description and return a list of item names.
        """
        if not self.backpack:
            print('Your backpack is empty.')
        else:
            for item in self.backpack:
                print(item.name, '-', item.description)
        return [item.name for item in self.backpack]


    def unlock(self, place):
        """If player has a key, unlock a locked neighboring place.
        """
        if type(place) != str:
            print("Place must be a string")
            return
        key = None
        for item in self.backpack:
            if isinstance(item, Key):
                key = item
                break
        if key is None:
            print("You don't have a key.")
            return
        if place not in self.place.exits:
            print("Can't find " + place + " nearby.")
            return
        destination = self.place.exits[place][0]
        key.use(destination)
        
    def keycode(self, code):
        if type(code) != str:
            print("Code must be a string")
            return
        if len(code) != 4:
            print("Code must be 4 digits")
            return
        if code == '8109':
            self.won = True
        else:
            print("Unfortunately that is not the correct code")
            
    def meditate(self):
        self.night_time = True
        print("At first you sit uncomfortably on the cushion, unsure of what to do. As you slow down and focus on your breathing the world starts to\n\nfade away\n\nYou open your eyes and notice it\'s now dark out. Through the window you see stars twinkling up above.")


class Thing:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def use(self, place):
        print("You can't use a {0} here".format(self.name))



class Key(Thing):
    def use(self, place):
        if place.locked:
            place.locked = False
            print("Unlocked " + place.name)
        else:
            print(place.name + " is already unlocked")



class Place:
    def __init__(self, name, description, things):
        self.name = name
        self.description = description
        self.things = {thing.name: thing for thing in things}
        self.locked = False
        self.exits = {}

    def look(self):
        print(self.description)
        print()
        print('Things:')
        if not self.things:
            print('nothing in particular')
        else:
            for thing in self.things.values():
                print('   ', thing.name, '-', thing.description)
        self.check_exits()

    def get_neighbor(self, exit):
        if type(exit) != str:
            print('Exit has to be a string.')
            return self
        elif exit in self.exits:
            exit_place = self.exits[exit][0]
            return exit_place
        else:
            print("Can't go to {} from {}.".format(exit, self.name))
            print("Try looking around to see where to go.")
            return self

    def take(self, thing):
        return self.things.pop(thing)

    def check_exits(self):
        print()
        print('You can go to:')
        for exit in self.exits:
            print('   ', exit)

    def add_exits(self, places):
        for place in places:
            self.exits[place.name] = (place, place.description)
            place.exits[self.name] = (self, self.description)
            
    def add_oneway_exits(self, places):
        for place in places:
            self.exits[place.name] = (place, place.description)
            
class Outside_Place(Place):
    def __init__(self, name, description, night_description, things):
        super().__init__(name, description, things)
        self.night_description = night_description

    def look_at_night(self):
        print(self.night_description)
        print()
        print('Things:')
        if not self.things:
            print('nothing in particular')
        else:
            for thing in self.things.values():
                print('   ', thing.name, '-', thing.description)
        self.check_exits()