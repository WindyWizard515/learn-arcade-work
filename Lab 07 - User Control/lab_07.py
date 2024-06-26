""" Lab 7 - User Control """

import arcade
from time import sleep

# --- Constants ---
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 1000
MOVEMENT_SPEED = 5
DEAD_ZONE = 0.02

class Ball:
    def __init__(self, position_x, position_y, change_x, change_y, radius, color):
        self.position_x = position_x
        self.position_y = position_y
        self.change_x = change_x
        self.change_y = change_y
        self.radius = radius
        self.color = color

        # Variables that track wall collisions
        self.hit_left_wall = False
        self.hit_right_wall = False
        self.hit_top_wall = False
        self.hit_bottom_wall = False

        # Wall sound
        self.wall_sound = arcade.load_sound("/home/paul/learn-arcade-work/Lab 07 - User Control/wall.wav")
        self.wall_sound_player = None

    def draw(self):
        """ Draw the balls with the instance variables we have. """
        arcade.draw_circle_filled(self.position_x,
                                  self.position_y,
                                  self.radius,
                                  self.color)

    def update(self):
        # Move the ball
        self.position_y += self.change_y
        self.position_x += self.change_x

        # See if the ball hit the edge of the screen.
        if self.position_x < self.radius:
            if not self.hit_left_wall:
                arcade.play_sound(self.wall_sound)
                self.hit_left_wall = True
            self.position_x = self.radius
        else:
            self.hit_left_wall = False

        if self.position_x > SCREEN_WIDTH - self.radius:
            if not self.hit_right_wall:
                arcade.play_sound(self.wall_sound)
                self.hit_right_wall = True
            self.position_x = SCREEN_WIDTH - self.radius
        else:
            self.hit_right_wall = False

        if self.position_y < self.radius:
            if not self.hit_bottom_wall:
                arcade.play_sound(self.wall_sound)
                self.hit_bottom_wall = True
            self.position_y = self.radius
        else:
            self.hit_bottom_wall = False

        if self.position_y > SCREEN_HEIGHT - self.radius:
            if not self.hit_top_wall:
                arcade.play_sound(self.wall_sound)
                self.hit_top_wall = True
            self.position_y = SCREEN_HEIGHT - self.radius
        else:
            self.hit_top_wall = False



class MyGame(arcade.Window):
    """ Our Custom Window Class"""

    def __init__(self):
        """ Initializer """
        # Call the parent class initializer
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "Alien Attack")   

        # Laser Sound
        self.mouse_sound = arcade.load_sound("/home/paul/learn-arcade-work/Lab 07 - User Control/laser.wav")

        self.set_mouse_visible(False)

        self.ball_mouse = Ball(50, 50, 0, 0, 15, arcade.color.GREEN)
        self.ball_control = Ball(50, 50, 0, 0, 15, arcade.color.RED)
        
        joysticks = arcade.get_joysticks()

        if joysticks:
            self.joystick = joysticks[0]
            self.joystick.open()
        else:
            print("There are no joysticks.")
            self.joystick = None


    def on_draw(self):
        """ Start Drawing """
        arcade.start_render()
        self.ball_mouse.draw()
        self.ball_control.draw()

        # Create the background
        arcade.set_background_color(arcade.color.BLUE)

    def on_mouse_motion(self, x, y, dx, dy):
        """ Called to update our objects.
        Happens approximately 60 times per second."""
        self.ball_mouse.position_x = x
        self.ball_mouse.position_y = y
    
    def on_mouse_press(self, x, y, button, modifiers):
        """ Called when the user presses a mouse button. """

        if button == arcade.MOUSE_BUTTON_LEFT:
            self.mouse_sound_player = arcade.play_sound(self.mouse_sound)
    
    def update(self, delta_time):

        if self.joystick:

            # Set a "dead zone" to prevent drive from a centered joystick
            if abs(self.joystick.x) < DEAD_ZONE:
                self.ball_control.change_x = 0
            else:
                self.ball_control.change_x = self.joystick.x * MOVEMENT_SPEED

            # Set a "dead zone" to prevent drive from a centered joystick
            if abs(self.joystick.y) < DEAD_ZONE:
                self.ball_control.change_y = 0
            else:
                self.ball_control.change_y = -self.joystick.y * MOVEMENT_SPEED

        self.ball_control.update()
            

def main():
    window = MyGame()
    arcade.run()


main()