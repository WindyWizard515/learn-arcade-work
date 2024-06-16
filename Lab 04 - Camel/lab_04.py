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


    
    while True:

        options()
        choice = input('\nWhat is your choice?: ')

        if choice.lower() =='q':
            print('\nYou have quit Camel.\n')
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
                win_screen()
                break
            oasis()           
        elif choice.lower() == 'c':
            player_miles = full_speed()
            miles_traveled += player_miles
            native_miles = native_speed()
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
            if miles_traveled >= 200:
                win_screen()
                break
            oasis()
        elif choice.lower() == 'd':
            camel_fatigue = 0
            native_miles = native_speed()
            native_distance += native_miles
            print('\nYour camel is very happy!')
            if miles_traveled - native_distance <= 15:
                if native_distance >= miles_traveled:
                    print('The natives had caught up to you! You have lost.')
                    break
                else:
                    print('The natives are getting close!')
        elif choice.lower() == 'e':
            status_check()
        else:
            print('You can\'t type that in!')
            print('The only options to type are:')
        


            
main()