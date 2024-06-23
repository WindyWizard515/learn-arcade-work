from adventure_classes import *
from adventure_weapons import *
from adventure_room_functions import *
import os

"""            Create all of the Instances of the Classes that we made in adventure_classes """

"""                                                Rooms                                       """
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
bedroom = Room("\n\nYou are in the Bedroom, along a dusty bookshelf, you can see a book the stands out more than the rest.. There is less dust on it!\
                \n                                          You may interact with The Book or move West\n\n", None, None, None, 3, "Book", None)


boss_room = Room("\n\n      You are now in the Boss Room! The passageway Closed behind you and you can see a weak and frail man sitting in the center of the arena,\
                        suddenly, he starts to glow with an eerie light, and starts rising in the air! You can't see anything, but suddenly it seems like time freezes.\
                        Then in the middle of the arena you see the Old Man, but suddenly he points what looks like a wand at you and suddenly a big bolt of lightning crashes out of the want at you\
                                                                        He missed... This time.\n\n", None, None, None, None, None, None)

# Create an empty list where we will append all of the rooms that we create
room_list = []

# Append all of the variables to Room_ list

# Armory
room_list.append(armory)

# Kitchen
room_list.append(kitchen)
# Library
room_list.append(library)

# Child's Bedroom
room_list.append(child_bedroom)

# Bedroom
room_list.append(bedroom)

# Boss Room
room_list.append(boss_room)

""" Create the main() function that hold the main loop and the stuff that prints on the screen """
def main():



    """ Create a variable that we will change based on the user input for each room. The room numbers are:
                    0=Armory 1=Kitchen 2=Library 3=Child's Bedroom 4=Bedroom 5=Boss Room"""
    
    current_room = 0

    # Create an instance of the Player class for health, armor, weapon, and the amount of damage they do
    
    player_status = Player(100, 5, chosen_weapon)

    """ Print the directions and how to control the player """
    instructions_print()
    player_input = input("If you ever want to see the instructions again, type in \'instructions\' Once you have read the instructions and are ready\
 to start the game, press enter: ")
    while True:
        if player_input == '':
            os.system("clear")
            break
        else:
            pass

    """ Print the beginning text of the game before the options """
    os.system("clear")
    print("Welcome, brave adventurer, to \"The Dark Tower,\" a captivating text adventure.")
    print("You find yourself inside the ominous Dark Tower, a place of malevolence and power.")
    print("Legends speak of a formidable evil lurking within these walls, and only the daring have ventured inside.")
    print("As you navigate the tower's dark corridors and hidden chambers,")
    print("your courage, wit, and resourcefulness will determine your fate.")
    print("Will you conquer the tower, or will it ensare you in its dark embrace?\n")


    """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""



    """ Create the main loop of the game that includes the input of the player """
    while True:
        # Print the description of the room you are currently in
        print(room_list[current_room].description)

        # Ask the user what they would like to do
        user_input = input("                   What do you choose to do? ")

        # Testing for all of the commands that the user could input:

        # North
        if user_input.lower() == "n" or user_input.lower() == "north":
            next_room = room_list[current_room].north
            if next_room == None:
                print("\n                         You can't go that way!")
            else:
                current_room = next_room
                os.system("clear")

        # East
        elif user_input.lower() == "e" or user_input.lower() == "east":
            next_room = room_list[current_room].east
            if next_room == None:
                print("\n                         You can't go that way!")
            else:
                current_room = next_room
                os.system("clear")

        # South
        elif user_input.lower() == "s" or user_input.lower() == "south":
            next_room = room_list[current_room].south
            if next_room == None:
                print("\n                         You can't go that way!")
            else:
                current_room = next_room
                os.system("clear")

        # West
        elif user_input.lower() == "w" or user_input.lower() == "west":
            next_room = room_list[current_room].west
            if next_room == None:
                print("\n                         You can't go that way!")
            else:
                current_room = next_room
                os.system("clear")

        # Interact
        elif user_input.lower() == "i" or user_input.lower() == "interact":
            if room_list[current_room].interactables == None:
                print("\n           There is nothing to interact with!")
            else:
                os.system("clear")
                room_list[current_room].interact()

        # Display current weapon
        elif user_input.lower() == "weapon":
            os.system("clear")
            print(f"\n                   Your current weapon is {chosen_weapon.name}")

        # Quit
        elif user_input.lower() == "q" or user_input.lower() == "quit":
            print("\n                    You have now quit the game :(\n")
            os.system("clear")
            break

        # User input is not undersood
        else:
            os.system("clear")
            print(f"\nThe user input: '{user_input}' was not understood.\n              Please Try again.")


main()