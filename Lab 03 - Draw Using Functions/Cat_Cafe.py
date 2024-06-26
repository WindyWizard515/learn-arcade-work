# Import The "arcade" library
import arcade

# All of the functions for Lab_03
def draw_cafe_background():
    """ Draw the Background of the cafe """
    arcade.draw_lrtb_rectangle_filled(0, 600, 600, 500, arcade.csscolor.SKY_BLUE)
    
def draw_sun():
    """ Draw the Sun """
    arcade.draw_circle_filled(600, 600, 40, arcade.color.YELLOW)

def draw_sun_rays():
    """ Rays of the Sun """
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

def window(x, y):
    """ Draw a Window """
    # Make the inside of the window sky blue
    arcade.draw_lrtb_rectangle_filled(x, x + 100, y + 100, y, arcade.csscolor.SKY_BLUE)

    # Draw the outline of the window
    arcade.draw_lrtb_rectangle_outline(x, x + 100, y + 100, y, arcade.csscolor.BLACK, 5)

    # Draw the lines inside of the window
    arcade.draw_line(x, y + 50, x + 100, y + 50, arcade.csscolor.BLACK, 5 )
    arcade.draw_line(x + 50, y, x + 50, y + 100, arcade.csscolor.BLACK, 5)

def chimmney():
    """ Draw the Chimmney"""
    arcade.draw_lrtb_rectangle_filled(450, 475, 550, 500, arcade.csscolor.BLACK)

def smoke():
    """ Draw a wisp of smoke """
    arcade.draw_polygon_filled([[460, 560], [470, 565], [475, 570], [480, 565], [470, 560]], arcade.csscolor.GRAY)