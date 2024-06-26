"""                                     Create All of the Classes                              """

# Create a Class called Room()
class Room:
    def __init__(self, description, north, east, south, west, interactables, interact_action):
        self.description = description
        self.north = north
        self.east = east
        self.south = south
        self.west = west
        self.interactables = interactables
        self.interact_action = interact_action

    def interact(self):
        """
        Property for interactables that runs a piece of code when accessed.
        """
        self.interact_action()
        
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

class Player():
    def __init__(self, health, armor, weapon):
        self.health = health
        self.armor = armor
        self.weapon = weapon

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

# Create a Weapon Class
class Weapon():
        """ Create a Weapon Class """
        def __init__(self, name, damage):
            self.name = name
            self.damage = damage

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

# Create an Enemy Class
class Enemy():
    """ Create an Enemy Class """
    def __init__(self, name, damage, health):
        self.name = name
        self.damage = damage
        self.health = health
        