from Text_Adventure import *

"""                 List of Command that do not currently work:
        'i' 'interact' 'b' 'backpack' 'inventory' 'u' 'utilize' 'a' 'attack' """
""" Weapon speed and weapon Block do not currently work"""
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

    """ Will Change based on the user input in the armory, the weapn indexes are:
                    1=War Axe 2=Spear 3=Katana 4=Shortsword 5=Theif's Dagger 6=Fists"""
    
    weapon_choice = 4
    chosen_weapon = weapon_list[weapon_choice]

    # Create an instance of the Player class for health, armor, weapon, and the amount of damage they do
    
    player_status = Player(100, 5, chosen_weapon)

    """ Print the directions and how to control the player """
    instructions_print()
    player_input = input("Once you have read the instructions and are ready\
 to start the game, press enter: ")
    while True:
        if player_input == '':
            break
        else:
            pass

    """ Print the beginning text of the game before the options """

    print("\n\nWelcome, brave adventurer, to \"The Dark Tower,\" a captivating text adventure.")
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

        # Interact
        elif user_input.lower() == "i" or user_input.lower() == "interact":
            if room_list[current_room].interactables == None:
                print("\n           There is nothing to interact with!")
            else:
                room_list[current_room].interact()

        # Display current weapon
        elif user_input.lower() == "weapon":
            print(f"You current weapon is {chosen_weapon.name}")

        # Quit
        elif user_input.lower() == "q" or user_input.lower() == "quit":
            print("\n                    You have now quit the game :(\n")
            break

        # User input is not undersood
        else:
            print(f"\nThe user input: '{user_input}' was not understood.\n              Please Try again.")


main()