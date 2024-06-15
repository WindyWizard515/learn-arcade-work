# Import the random module for randrange
from random import randrange

# Create the Variables for the loop and stats
done = False
miles_traveled = 0
thirst = 0
camel_fatigue = 0
native_distance = 0 - 20
canteen_sips = 3

def welcome():
    print('\n\nWelcome to Camel!\n')
    print('You have stolen a camel to make your way across the great Mobi desert.')
    print('The natives want their camel back and are chasing you down! Survive your')
    print('desert trek and outrun the natives.\n')

def options():
    print('\n          OPTIONS:        \n')
    print('A. Drink from your canteen.')
    print('B. Ahead moderate speed.')
    print('C. Ahead full speed.')
    print('D. Stop for the night.')
    print('E. Status check.')
    print('Q. Quit.')

def quit():
    print('\nYou have quit Camel.')

def thirst_option(canteen_sips):
    if canteen_sips == 0:
        print('\nYou don\'t have enough sips in your canteen for that!')
    else:
        canteen_sips -= 1
        print(f'\nYou took a sip of your canteen, you now have {canteen_sips} sips left')

    return canteen_sips

def native_speed():
    native_miles = randrange(7, 15)
    return native_miles

def moderate_speed():
    player_miles = randrange(5, 13)
    return player_miles

