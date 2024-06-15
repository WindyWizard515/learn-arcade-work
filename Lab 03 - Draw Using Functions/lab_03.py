# Import arcade and all of the functions
# Folder for functions is in learn-arcade-work
from functions import Lab_03

def main():
    
    # Open the window
    Lab_03.arcade.open_window(600, 600, "Cat Cafe")

    # Set the background color
    Lab_03.arcade.set_background_color((100, 50, 0))

    # Get ready to draw
    Lab_03.arcade.start_render()

    # Draw the background wall of the cafe
    Lab_03.draw_cafe_background()

    # Draw the body of the Sun
    Lab_03.draw_sun()

    # Draw the rays of the Sun
    Lab_03.draw_sun_rays()

    # Draw the outline of the cafe along the edges of the screen
    Lab_03.outline_cafe()

    # Draw the cafe door ihe midde of the screen
    Lab_03.cafe_door()

    # Draw the doorknob of the cafe door
    Lab_03.cafe_doorknob()

    # Draw the two Windows at the points, (x, y)
    # Window 1: (50, 150)
    # Window 2: (450, 150)
    Lab_03.window(50, 150)
    Lab_03.window(450, 150)

    # Draw the chimmney
    Lab_03.chimmney()

    # Draw the smoke from the chimmney
    Lab_03.smoke()

    # Finish Drawing
    Lab_03.arcade.finish_render()

    # Keep the Window open
    Lab_03.arcade.run()

# Call the main function start the program
main()