""" Create All of the Classes """

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


"""                                 Weapons                     """
# Create an instance of the Weapon class whose paramaters are name, and damage
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

weapon_list = []

# Append all of the weapons to weapon_list
# Append a placeholder so I dont have to find the difference of what the player puts in on the wal of weapons screen
weapon_list.append("placeholder")
# Append the War ax
weapon_list.append(war_ax)

# Append the Spear
weapon_list.append(spear)

# Append the Katana
weapon_list.append(katana)

# Append the Shortsword
weapon_list.append(shortsword)

# Append the Thief's Dagger
weapon_list.append(theif_dagger)

# Append the Fists
weapon_list.append(barehanded)

""" Make the definitions for all the interactables in the rooms """

def wall_of_weapons():
    print("Choose a Weapon to aid you on your journey\n")
    print("1: War Axe, Damage = 25 speed = 1")
    print("2: Spear, Damage = 15, speed = 1.5")
    print("3: Katana, Damage = 15, speed = 1, block = 5")
    print("4: Shortsword, damage 10, speed 2")
    print("5: Theif's Dagger, damage 10, speed 2.5")
    print("6: Fists, damage 5, speed 1")
    weapon_choice = input("\nEnter the number of what weapon you would like: ")
    try:
        int(weapon_choice)
        chosen_weapon = weapon_list[weapon_choice]
        print(f"The weapon you chose was {chosen_weapon}!")
    except ValueError:
        print("You can't do that!")
    except TypeError:
        pass

""" Create all of the Instances of the Classes that we made above """

"""                          Rooms                              """
# Create the Armory Room
armory = Room("\n\n       You are in the Armory, you see a big wall of weapons.\
                \n              You may take a weapon or move East or West\n\n", None, 1, None, 2, "Wall of Weapons", wall_of_weapons)


# Create the Kitchen Room
kitchen = Room("\n\n       You are in the Kitchen, you see a box of bread that is just in your reach.\
                \n                   You may pick up the box of bread or move West\n\n", None, None, None, 0, "Box of Bread", None)


# Create the Library Room
library = Room("\n\n       You are in the Library, you see nothing of interest.\
                \n                      You may move North or East\n\n", 3, 0, None, None, None, None)


# Create the Child's Bedroom Room
child_bedroom = Room("\n\n       You are in the Child's Bedroom, you see nothing of interest.\
                        \n                         You may move East or South\n\n", None, 4, 2, None, None, None)


# Create the Bedroom Room
bedroom = Room("\n\n       You are in the Bedroom, along a dusty bookshelf, you can see a book the stands out more than the rest.. There is less dust on it!\
                \n                                                 You may interact with The Book or move West\n\n", None, None, None, 3, "Book", None)


boss_room = Room("\n\n      You are now in the Boss Room! The passageway Closed behind you and you can see a weak and frail man sitting in the center of the arena,\
                        suddenly, he starts to glow with an eerie light, and starts rising in the air! You can't see anything, but suddenly it seems like time freezes.\
                        Then in the middle of the arena you see the Old Man, but suddenly he points what looks like a wand at you and suddenly a big bolt of lightning crashes out of the want at you\
                                                                        He missed... This time.\n\n", None, None, None, None, None, None)




""" The instructions of how to play the game and move around """

def instructions_print():
    """ Print the directions and how to control the player """
    print("\n\nWelcome to the text adventure game \"The Dark Tower.\"")
    print("To play, use directional commands to navigate:")
    print("- Type 'n' or 'north' to go north,")
    print("- Type 'e' or 'east' to go east,")
    print("- Type 's' or 'south' to go south,")
    print("- Type 'w' or 'west' to go west.\n")
    print("To interact with objects or characters in your surroundings, press 'i', or type 'interact'.")
    # print("Access your inventory by pressing 'b' or typing 'backpack' or 'inventory'.")
    # print("Use 'u' or 'use' to utilize any items you have collected.")
    # print("If you encounter an enemy, press 'a' or type 'attack' to engage in combat.")
    print("If you type in 'weapon' it will display current weapon {Work In Progress}")
    print("If you want to quit the game just press 'q' or type 'quit'")
    print("Follow the prompts and descriptions provided in the game to explore, solve puzzles,\
and advance through the story.\n")

