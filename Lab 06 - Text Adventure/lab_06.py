from Text_Adventure import *

def main():

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

    """ Create a variable that we will change based on the user input for each room. The room numbers are:
                    0=Armory 1=Kitchen 2=Library 3=Child's Bedroom 4=Bedroom 5=Boss Room"""
    current_room = 0

    # Create an instance of the Weapon class whose paramaters are name, and damage
    weapon_list = []

    # Append all of the weapons to weapon_list
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

    """ Will Change based on the user input in the armory, the weapn indexes are:
                    0=War Axe 1=Spear 2=Katana 3=Shortsword 4=Theif's Dagger 5=Fists"""
    chosen_weapon = weapon_list[5]

    # Create an instance of the Player class for health, armor, weapon, and the amount of damage they do
    
    player_status = Player(100, 5, chosen_weapon)






    
    """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
    """ Create the main loop of the game that includes the input of the player """
    while True:

        # Print the description of the room you are currently in
        print(room_list[current_room].description)

        # Ask the user what they would like to do
        user_input = input("                   What do you choose to do?  ")

        # Testing for all of the commands that the user could input:

        # North
        if user_input.lower() == "n" or user_input.lower() == "north":
            next_room = room_list[current_room].north
            if next_room == None:
                print("\n                         You can't go that way!")
            else:
                current_room = next_room

        # East
        elif user_input.lower() == "e" or user_input.lower() == "east":
            next_room = room_list[current_room].east
            if next_room == None:
                print("\n                         You can't go that way!")
            else:
                current_room = next_room

        # South
        elif user_input.lower() == "s" or user_input.lower() == "south":
            next_room = room_list[current_room].south
            if next_room == None:
                print("\n                         You can't go that way!")
            else:
                current_room = next_room

        # West
        elif user_input.lower() == "w" or user_input.lower() == "west":
            next_room = room_list[current_room].west
            if next_room == None:
                print("\n                         You can't go that way!")
            else:
                current_room = next_room

        # Interactables

        # Quit
        elif user_input.lower() == "q" or user_input.lower() == "quit":
            print("\n                    You have now quit the game :(\n")
            break

        # User input is not undersood
        else:
            print(f"\nThe user input: '{user_input}' was not understood.\n              Please Try again.")


main()