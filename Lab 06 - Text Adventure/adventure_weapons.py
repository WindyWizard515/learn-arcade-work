from adventure_classes import *

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

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

# Making the variable for the list of weapons that I am going to append all of the weapons to
weapon_list = []

# Append a placeholder so I dont have to find the difference of what the player puts in on the wall of weapons screen
weapon_list.append("placeholder")

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

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

""" Will Change based on the user input in the armory, the weapon indexes are:
                1=War Axe 2=Spear 3=Katana 4=Shortsword 5=Theif's Dagger 6=Fists The default weapons are Fists"""

weapon_choice = 6
chosen_weapon = weapon_list[weapon_choice]

