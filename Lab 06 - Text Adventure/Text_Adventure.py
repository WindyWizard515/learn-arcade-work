""" Create All of the Classes """

# Create a Class called Room()
class Room():
    def __init__(self, description, north, east, south, west, intereactables):
        self.description = description
        self.north = north
        self.east = east
        self.south = south
        self.west = west
        self.intereactables = intereactables
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



""" Create all of the Instances of the Classes that we made above """

"""                          Rooms                              """
# Create the Armory Room
armory = Room("\n\n       You are in the Armory, you see a big wall of weapons.\
                \n              You may take a weapon or move East or West\n\n", None, 1, None, 2, "Wall of Weapons")


# Create the Kitchen Room
kitchen = Room("\n\n       You are in the Kitchen, you see a box of bread that is just in your reach.\
                \n                   You may pick up the box of bread or move West\n\n", None, None, None, 0, "Box of Bread")


# Create the Library Room
library = Room("\n\n       You are in the Library, you see nothing of interest.\
                \n                      You may move North or East\n\n", 3, 0, None, None, None)


# Create the Child's Bedroom Room
child_bedroom = Room("\n\n       You are in the Child's Bedroom, you see nothing of interest.\
                        \n                         You may move East or South\n\n", None, 4, 2, None, None)


# Create the Bedroom Room
bedroom = Room("\n\n       You are in the Bedroom, along a dusty bookshelf, you can see a book the stands out more than the rest.. There is less dust on it!\
                \n                                                 You may interact with The Book or move West\n\n", None, None, None, 3, "Book")


boss_room = Room("\n\n      You are now in the Boss Room! The passageway Closed behind you and you can see a weak and frail man sitting in the center of the arena,\
                        suddenly, he starts to glow with an eerie light, and starts rising in the air! You can't see anything, but suddenly it seems like time freezes.\
                        Then in the middle of the arena you see the Old Man, but suddenly he points what looks like a wand at you and suddenly a big bolt of lightning crashes out of the want at you\
                                                                        He missed... This time.\n\n", None, None, None, None, None)


"""                                 Weapons                     """
# War Ax deals 20 damage
war_ax = Weapon("War Axe", 20)

# Spear deals 15 damage
spear = Weapon("Spear", 15)

# Katana deals 15 damage
katana = Weapon("Katana", 15)

# Shortsword deals 15 damage
shortsword = Weapon("Shortsword", 10)

# Thief's Dagger
theif_dagger = Weapon("Theif's Dagger", 10)

# Fists
barehanded = Weapon("Barehanded", 5)