# Import The "arcade" library

import arcade
import arcade.csscolor

# Open the window
arcade.open_window(600, 600, "Cat Cafe")

# Set the background color
arcade.set_background_color((100, 50, 0))

# Get ready to draw
arcade.start_render()

# Draw a rectangle
arcade.draw_lrtb_rectangle_filled(0, 600, 600, 500, arcade.csscolor.SKY_BLUE)

# Draw a Sun
arcade.draw_circle_filled(600, 600, 40, arcade.color.YELLOW)

# Draw the rays of the Sun
arcade.draw_line(600, 600, 555, 555, arcade.color.YELLOW, 4)
arcade.draw_line(600, 600, 577, 550, arcade.color.YELLOW, 4)
arcade.draw_line(600, 600, 550, 577, arcade.color.YELLOW, 4)
arcade.draw_line(600, 600, 535, 590, arcade.color.YELLOW, 4)
arcade.draw_line(600, 600, 590, 540, arcade.color.YELLOW, 4)

# Draw the Outline of Cafe
arcade.draw_lrtb_rectangle_filled(0, 600, 500, 490, arcade.csscolor.SANDY_BROWN)
arcade.draw_lrtb_rectangle_filled(0, 10, 500, 0, arcade.csscolor.SANDY_BROWN)
arcade.draw_lrtb_rectangle_filled(590, 600, 500, 0, arcade.csscolor.SANDY_BROWN)

# Draw the Cafe door
arcade.draw_lrtb_rectangle_outline(200, 400, 300, 0, arcade.csscolor.SANDY_BROWN, 10)

# Draw the doorknob
arcade.draw_ellipse_filled(360, 130, 25, 15, arcade.csscolor.SANDY_BROWN, 90)

# Making the inside of the window1 arcade.csscolor.SKY_BLUE
arcade.draw_lrtb_rectangle_filled(450, 550, 300, 200, arcade.csscolor.SKY_BLUE)

# Draw the window1 outline
arcade.draw_lrtb_rectangle_outline(450, 550, 300, 200, arcade.csscolor.BLACK, 5)

# Making the inside of the window1
arcade.draw_line(500, 200, 500, 300, arcade.csscolor.BLACK, 5)
arcade.draw_line(450, 252.5, 550, 252.5, arcade.csscolor.BLACK, 5 )

# Making the inside of window2, arcade.csscolor.SKY_BLUE
arcade.draw_lrtb_rectangle_filled(50, 150, 300, 200, arcade.csscolor.SKY_BLUE)

# Draw the window2 outline
arcade.draw_lrtb_rectangle_outline(50, 150, 300, 200, arcade.csscolor.BLACK, 5)

# Draw the window2 inside
arcade.draw_line(50, 250, 150, 250, arcade.csscolor.BLACK, 5 )
arcade.draw_line(100, 200, 100, 300, arcade.csscolor.BLACK, 5)

# Drawing the Chimmney
arcade.draw_lrtb_rectangle_filled(450, 475, 550, 500, arcade.csscolor.BLACK)

# Draw the Smoke
arcade.draw_polygon_filled([[460, 560], [470, 565], [475, 570], [480, 565], [470, 560]], arcade.csscolor.GRAY)

# Finish Drawing
arcade.finish_render()

# Keep the Window open
arcade.run()