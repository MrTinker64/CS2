# A "simple" adventure game.

class Player:
    def __init__(self, name, place):
        """Create a player object."""
        self.name = name
        self.place = place
        self.backpack = []
        self.won = False
        self.night_time = False
        self.hasFlashlight = False

    def look(self):
        # TODO test this
        print('You are currently in the ' + self.place.name, end=". ")
        if self.place.name == 'Storage Closet':
            if not any(item.name == 'Flashlight' for item in self.backpack):
                print("The room is too dark to see in and the only light has broken.")
                return
            else:
                print("The room is too dark to see in and the only light bulb has broken. Luckily, you picked up the flashlight from earlier.\nYou turn on your flashlight and it illuminates:")
        else:
            print("You take a look around and see:")
        self.place.look()
        if self.place.name == 'Observatory' and self.night_time:
            print("Now that it is the early morning you are able to look through the telescope at the celestial objects listed on the wall.\nSoon you realize that all the objects you're looking at from double star clusters to binary stars or all manner of thin and cigar-shaped galaxies everything looks like either an 8 or a 1.\nBy the time you're done watching it has become day again.")
        if self.place.name == 'Lake' and any(item.name == 'Remote Controller' for item in self.backpack):
            print("You use the remote controller to drive the toy boat over to you. Sitting inside are some blueprints.\nThe blue prints seem to be for the very estate that your standing on. Though the left half has been damaged by water you can make out the lake and the building to the right.\nFrom this perspective they look like a 0 and a 9.")

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
        # TODO make this meditation and night time instead of morning
        self.night_time = True
        print("You get a good rest. When you wake up it appears to be the dark, early morning.")
        print(f"self.night_time = {self.night_time}")


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