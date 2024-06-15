# Import arcade and all of the functions
# Folder for functions is in learn-arcade-work
from .Cat_Cafe import *

def main():
    
    # Open the window
    arcade.open_window(600, 600, "Cat Cafe")

    # Set the background color
    arcade.set_background_color((100, 50, 0))

    # Get ready to draw
    arcade.start_render()

    # Draw the background wall of the cafe
    draw_cafe_background()

    # Draw the body of the Sun
    draw_sun()

    # Draw the rays of the Sun
    draw_sun_rays()

    # Draw the outline of the cafe along the edges of the screen
    outline_cafe()

    # Draw the cafe door ihe midde of the screen
    cafe_door()

    # Draw the doorknob of the cafe door
    cafe_doorknob()

    # Draw the two Windows at the points, (x, y)
    # Window 1: (50, 150)
    # Window 2: (450, 150)
    window(50, 150)
    window(450, 150)

    # Draw the chimmney
    chimmney()

    # Draw the smoke from the chimmney
    smoke()

    # Finish Drawing
    arcade.finish_render()

    # Keep the Window open
    arcade.run()

# Call the main function start the program
main()