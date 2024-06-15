from camel import *


def main():

    # Create the Variables for the loop and stats
    done = False
    miles_traveled = 0
    thirst = 0
    camel_fatigue = 0
    native_distance = 0 - 20
    canteen_sips = 3

    welcome()


    
    while not False:

        options()
        choice = input('\nWhat is your choice?: ')

        if choice.lower() =='q':
            quit()
            break
        elif choice.lower() == 'a':
            canteen_sips = thirst_option(canteen_sips)
            thirst = 0           
        elif choice.lower() == 'b':
            player_miles = moderate_speed()
            native_miles = native_speed()
            native_distance += native_miles
            miles_traveled += player_miles
            print(f'\nYou traveled {player_miles} miles!')
            if miles_traveled - native_distance <= 15:
                if native_distance >= miles_traveled:
                    print('The natives had caught up to you! You have lost.')
                    break
                else:
                    print('The natives are getting close!')
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
            if miles_traveled >= 200:
                print('''\n\n\n\n\n\n\n\n\n __     __          __          ___       _ 
 \ \   / /          \ \        / (_)     | |
  \ \_/ /__  _   _   \ \  /\  / / _ _ __ | |
   \   / _ \| | | |   \ \/  \/ / | | '_ \| |
    | | (_) | |_| |    \  /\  /  | | | | |_|
    |_|\___/ \__,_|     \/  \/   |_|_| |_(_)\n\n\n\n\n''')
                break
            oasis = randrange(1, 21)
            if oasis == 1:
                canteen_sips = 3
                camel_fatigue = 0
                thirst = 0
                print('You have found an oasis!')            
        elif choice.lower() == 'c':
            player_miles = randrange(10, 21)
            miles_traveled += player_miles
            native_miles = randrange(7, 15)
            native_distance += native_miles
            print(f'\nYou traveled {player_miles} miles!')
            random_camel = randrange(1, 4)
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
            oasis = randrange(1, 21)
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
                break
        elif choice.lower() == 'd':
            camel_fatigue = 0
            native_miles = randrange(7, 15)
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