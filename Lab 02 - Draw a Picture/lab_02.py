# Import The "arcade" library

import arcade

def draw_cafe_background():
    """ Draw the Background of the cafe """
    arcade.draw_lrtb_rectangle_filled(0, 600, 600, 500, arcade.csscolor.SKY_BLUE)
    
def draw_sun():
    """ Draw the Sun """
    arcade.draw_circle_filled(600, 600, 40, arcade.color.YELLOW)

def draw_sun_rays():
    arcade.draw_line(600, 600, 555, 555, arcade.color.YELLOW, 4)
    arcade.draw_line(600, 600, 577, 550, arcade.color.YELLOW, 4)
    arcade.draw_line(600, 600, 550, 577, arcade.color.YELLOW, 4)
    arcade.draw_line(600, 600, 535, 590, arcade.color.YELLOW, 4)
    arcade.draw_line(600, 600, 590, 540, arcade.color.YELLOW, 4)

def outline_cafe():
    """ Draw the outline of the Cafe """
    arcade.draw_lrtb_rectangle_outline(0, 600, 500, 0, arcade.csscolor.SANDY_BROWN, 10)

def cafe_door():
    """ Draw the Cafe door """
    arcade.draw_lrtb_rectangle_outline(200, 410, 300, 0, arcade.csscolor.SANDY_BROWN, 5)

def cafe_doorknob():
    """ Draw the doorknob of the Cafe door """
    arcade.draw_ellipse_filled(360, 130, 25, 15, arcade.csscolor.SANDY_BROWN, 90)

def window():
    """ Draw a Window """
    # Make the insid of the window sky blue
    arcade.draw_lrtb_rectangle_filled(50, 150, 300, 200, arcade.csscolor.SKY_BLUE)

    # Draw the outline of the window
    arcade.draw_lrtb_rectangle_outline(50, 150, 300, 200, arcade.csscolor.BLACK, 5)

    # Draw the lines inside of the window
    arcade.draw_line(50, 250, 150, 250, arcade.csscolor.BLACK, 5 )
    arcade.draw_line(100, 200, 100, 300, arcade.csscolor.BLACK, 5)

def chimmney():
    """ Draw the Chimmney"""
    arcade.draw_lrtb_rectangle_filled(450, 475, 550, 500, arcade.csscolor.BLACK)

def smoke():
    """ Draw a wisp of smoke """
    arcade.draw_polygon_filled([[460, 560], [470, 565], [475, 570], [480, 565], [470, 560]], arcade.csscolor.GRAY)

def main():
    
    # Open the window
    arcade.open_window(600, 600, "Cat Cafe")

    # Set the background color
    arcade.set_background_color((100, 50, 0))

    # Get ready to draw
    arcade.start_render()

    draw_cafe_background()

    draw_sun()

    draw_sun_rays()

    outline_cafe()

    cafe_door()

    cafe_doorknob()

    # Making the inside of the window1 arcade.csscolor.SKY_BLUE
    arcade.draw_lrtb_rectangle_filled(450, 555, 300, 200, arcade.csscolor.SKY_BLUE)

    # Draw the window1 outline
    arcade.draw_lrtb_rectangle_filled(450, 550, 205, 200, arcade.csscolor.BLACK)
    arcade.draw_lrtb_rectangle_filled(450, 550, 305, 300, arcade.csscolor.BLACK)
    arcade.draw_lrtb_rectangle_filled(450, 455, 305, 200, arcade.csscolor.BLACK)
    arcade.draw_lrtb_rectangle_filled(550, 555, 305, 200, arcade.csscolor.BLACK)

    # Making the inside of the window1
    arcade.draw_line(502.5, 200, 500, 305, arcade.csscolor.BLACK, 5)
    arcade.draw_line(450, 252.5, 550, 252.5, arcade.csscolor.BLACK, 5 )

    window()

    chimmney()

    smoke()

    # Finish Drawing
    arcade.finish_render()

    # Keep the Window open
    arcade.run()

# Call the main function start the program
main()