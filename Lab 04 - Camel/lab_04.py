import random

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

def main():

    welcome()

    options()

    choice = input('\nWhat is your choice?: ')
    
    while not done:

        if choice.lower() =='q':
            print('\nYou have quit Camel.')
            break
        elif choice.lower() == 'a':
            if canteen_sips == 0:
                print('\nYou don\'t have enough sips in your canteen for that!')
            else:
                canteen_sips -= 1
                print(f'\nYou took a sip of your canteen, you now have {canteen_sips} sips left')
                thirst = 0
        elif choice.lower() == 'b':
            player_miles = random.randrange(5, 13)
            miles_traveled += player_miles
            native_miles = random.randrange(7, 15)
            native_miles += native_miles
            print(f'\nYou traveled {player_miles} miles!')
            if miles_traveled - native_distance <= 15:
                break
            camel_fatigue += 1
            thirst += 1
            if thirst > 4:
                if thirst >= 6:
                    print('\nYou have died of thirst!')
                    break
                else:
                    print('\nYou are getting thirsty.')            
            if camel_fatigue > 5:
                if camel_fatigue == 8:
                    print('\nYour camel is dead, You have lost')
                    break
                else:
                    print('\nYour camel is getting tired')
            if miles_traveled - native_distance <= 15:
                if native_distance >= miles_traveled:
                    print('The natives had caught up to you! You have lost.')
                    break
                else:
                    print('The natives are getting close!')
            if miles_traveled >= 200:
                print('''\n\n\n\n\n\n\n\n\n __     __          __          ___       _ 
 \ \   / /          \ \        / (_)     | |
  \ \_/ /__  _   _   \ \  /\  / / _ _ __ | |
   \   / _ \| | | |   \ \/  \/ / | | '_ \| |
    | | (_) | |_| |    \  /\  /  | | | | |_|
    |_|\___/ \__,_|     \/  \/   |_|_| |_(_)\n\n\n\n\n''')
                break
            oasis = random.randrange(1, 21)
            if oasis == 1:
                canteen_sips = 3
                camel_fatigue = 0
                thirst = 0
                print('You have found an oasis!')            
        elif choice.lower() == 'c':
            player_miles = random.randrange(10, 21)
            miles_traveled += player_miles
            native_miles = random.randrange(7, 15)
            native_distance += native_miles
            print(f'\nYou traveled {player_miles} miles!')
            random_camel = random.randrange(1, 4)
            camel_fatigue += random_camel
            thirst += 1
            if thirst > 4:
                if thirst >= 6:
                    print('\nYou have died of thirst!')
                    break
                else:
                    print('\nYou are getting thirsty.')
            if camel_fatigue > 4:
                if camel_fatigue >= 8:
                    print('\nYour camel is dead, You have lost!')
                    print(f'{camel_fatigue}')
                    break
                else:
                    print('\nYour camel is getting tired')
            oasis = random.randrange(1, 21)
            if oasis == 1:
                canteen_sips = 3
                camel_fatigue = 0
                thirst = 0
                print('You have found an oasis!')
            if miles_traveled >= 200:
                print('''\n\n\n\n\n\n\n\n\n __     __          __          ___       _ 
 \ \   / /          \ \        / (_)     | |
  \ \_/ /__  _   _   \ \  /\  / / _ _ __ | |
   \   / _ \| | | |   \ \/  \/ / | | '_ \| |
    | | (_) | |_| |    \  /\  /  | | | | |_|
    |_|\___/ \__,_|     \/  \/   |_|_| |_(_)\n\n\n\n\n''')
        elif choice.lower() == 'd':
            camel_fatigue = 0
            native_miles = random.randrange(7, 15)
            native_distance += native_miles
            print('\nYour camel is very happy!')
            if miles_traveled - native_distance <= 15:
                if native_distance >= miles_traveled:
                    print('The natives had caught up to you! You have lost.')
                    break
                else:
                    print('The natives are getting close!')
        elif choice.lower() == 'e':
            native_distance_away = miles_traveled - native_distance
            print(f'\nYour current stats are:\n')
            print(f'Thirst: {thirst}')
            print(f'Miles Traveled: {miles_traveled}.')
            print(f'Camel Fatigue: {camel_fatigue}.')
            print(f'The natives are: {native_distance_away} miles away.')
        


            
main()