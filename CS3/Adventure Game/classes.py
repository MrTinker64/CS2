# A "simple" adventure game.

class Player:
    def __init__(self, name, place):
        """Create a player object."""
        self.name = name
        self.place = place
        self.won = False

    def look(self):
        self.place.look()

    def go_to(self, location):
        """Go to a location if it's among the exits of player's current place and it is unlocked."""
   
        "*** YOUR CODE HERE ***"


    def talk_to(self, person):
        """Talk to person if person is at player's current place.
        """
        if type(person) != str:
            print('Person has to be a string.')
        "*** YOUR CODE HERE ***"


    def take(self, thing):
        """Take a thing if thing is at player's current place
        """
        
        if type(thing) != str:
            print('Thing should be a string.')
        "*** YOUR CODE HERE ***"

    def check_backpack(self):
        """Print each item with its description and return a list of item names.
        """
        "*** YOUR CODE HERE ***"


    def unlock(self, place):
        """If player has a key, unlock a locked neighboring place.
        """
        if type(place) != str:
            print("Place must be a string")
            return
        key = None
        
    def keycode(self, code):
        if type(code) != str:
            print("Code must be a string")
            return
        if len(code) != 4:
            print("Code must be 4 digits")
            return
        if code == '1804':
            self.won = True
        else:
            print("Unfortunately that is not the correct code")


class Character:
    def __init__(self, name, message):
        self.name = name
        self.message = message

    def talk(self):
        return self.message


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
    def __init__(self, name, description, characters, things):
        self.name = name
        self.description = description
        self.characters = {character.name: character for character in characters}
        self.things = {thing.name: thing for thing in things}
        self.locked = False
        self.exits = {} # {'name': (exit, 'description')}

    def look(self):
        print('You are currently at ' + self.name + '. You take a look around and see:')
        print('Characters:')
        if not self.characters:
            print('    no one in particular')
        else:
            for character in self.characters:
                print('   ', character)
        print('Things:')
        if not self.things:
            print('    nothing in particular')
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
        print('You can exit to:')
        for exit in self.exits:
            print('   ', exit)

    def add_exits(self, places):
        for place in places:
            self.exits[place.name] = (place, place.description)