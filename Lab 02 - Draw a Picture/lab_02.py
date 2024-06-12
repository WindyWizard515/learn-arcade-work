# Import The "arcade" library

import arcade
import arcade.csscolor
import arcade.csscolor
import arcade.csscolor
import arcade.csscolor
import arcade.csscolor
import arcade.csscolor
import arcade.csscolor
import arcade.csscolor
import arcade.csscolor

# Open the window
arcade.open_window(600, 600, "Cat Cafe")

# Set the background color
arcade.set_background_color((100, 50, 0))

# Get ready to draw
arcade.start_render()

# Draw a rectangle
arcade.draw_lrtb_rectangle_filled(0, 599, 599, 500, arcade.csscolor.SKY_BLUE)

# Draw a Sun
arcade.draw_circle_filled(599, 599, 40, arcade.color.YELLOW)

# Draw the rays of the Sun
arcade.draw_line(599, 599, 555, 555, arcade.color.YELLOW, 4)
arcade.draw_line(599, 599, 577, 550, arcade.color.YELLOW, 4)
arcade.draw_line(599, 599, 550, 577, arcade.color.YELLOW, 4)
arcade.draw_line(599, 599, 535, 590, arcade.color.YELLOW, 4)
arcade.draw_line(599, 599, 590, 540, arcade.color.YELLOW, 4)

# Draw the Outline of Cafe
arcade.draw_lrtb_rectangle_filled(0, 599, 500, 490, arcade.csscolor.SANDY_BROWN)
arcade.draw_lrtb_rectangle_filled(0, 10, 500, 0, arcade.csscolor.SANDY_BROWN)
arcade.draw_lrtb_rectangle_filled(590, 600, 500, 0, arcade.csscolor.SANDY_BROWN)

# Draw the Cafe door
arcade.draw_lrtb_rectangle_filled(200, 210, 300, 0, arcade.csscolor.SANDY_BROWN)
arcade.draw_lrtb_rectangle_filled(200, 400, 300, 290, arcade.csscolor.SANDY_BROWN)
arcade.draw_lrtb_rectangle_filled(400, 410, 300, 0, arcade.csscolor.SANDY_BROWN)

# Draw the doorknob
arcade.draw_ellipse_filled(360, 130, 25, 15, arcade.csscolor.SANDY_BROWN, 90)

# Draw the windows
arcade.draw_lrtb_rectangle_filled(350, 450, 505, 500, arcade.csscolor.BLACK)

# Finish Drawing
arcade.finish_render()

# Keep the Window open
arcade.run()