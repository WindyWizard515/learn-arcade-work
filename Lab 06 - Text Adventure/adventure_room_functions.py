from adventure_weapons import *
"""                              Make the definitions for all the interactables in the rooms                            """

""" The function for the armory room """
def wall_of_weapons():
    from lab_06 import weapon_choice, weapon_list
    global chosen_weapon
    print("\nChoose a Weapon to aid you on your journey\n")
    print("1: War Axe, Damage = 25 speed = 1")
    print("2: Spear, Damage = 15, speed = 1.5")
    print("3: Katana, Damage = 15, speed = 1, block = 5")
    print("4: Shortsword, damage 10, speed 2")
    print("5: Theif's Dagger, damage 10, speed 2.5")
    print("6: Fists, damage 5, speed 1")
    weapon_choice = input("\nEnter the number of what weapon you would like: ")
    if weapon_choice.lower() == 'n' or weapon_choice.lower() == 'no':
        print("Ok")
    elif int(weapon_choice) > 6 or int(weapon_choice) < 1:
        print("You can't pick that number!")
    elif weapon_choice.isdigit() == True:
        chosen_weapon = weapon_list[int(weapon_choice)]
        print(f"The weapon you chose was {chosen_weapon.name}!")
    else:
        print(f"User input {weapon_choice} not understood")

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

""" The function for the kitchen room """
def ration_of_food():
    from lab_06 import add_inventory
    inventory_answer = input("Do you want to add a Ration of food to your inventory? ")
    if inventory_answer.lower == "y" or inventory_answer.lower() == "yes":
        print("You now have a ration of food in your inventory")
        add_inventory("Ration of food")
    elif inventory_answer.lower == "n" or inventory_answer.lower == "no":
        print("Ok")
    else:
        print(f"User input {inventory_answer} not understood.")


""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
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
