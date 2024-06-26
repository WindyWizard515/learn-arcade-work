""" Sprite Sample Program """

import random
import arcade

# --- Constants ---
SPRITE_SCALING_PLAYER = .125
SPRITE_SCALING_COIN = 0.2
COIN_COUNT = 50

SCREEN_WIDTH = 1920
SCREEN_HEIGHT = 1015
MOVEMENT_SPEED = 5


class MyGame(arcade.Window):
    """ Our custom Window Class"""

    def __init__(self):
        """ Initializer """
        # Call the parent class initializer
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "Sprite Example")

        # Variables that will hold sprite lists
        self.player_list = None
        self.coin_list = None

        # Set up the player info
        self.player_sprite = None
        self.score = 0

        # Don't show the mouse cursor
        self.set_mouse_visible(False)

        # Track the current key state
        self.up_pressed = False
        self.down_pressed = False
        self.left_pressed = False
        self.right_pressed = False

        arcade.set_background_color(arcade.color.MAGENTA_HAZE)

    def setup(self):
        """ Set up the game and initialize the variables. """

        # Sprite lists
        self.player_list = arcade.SpriteList()
        self.coin_list = arcade.SpriteList()

        # Score
        self.score = 0

        self.ninja_right = "/home/paul/learn-arcade-work/Lab 08 - Sprites/ninja_right.png"
        self.ninja_left = "/home/paul/learn-arcade-work/Lab 08 - Sprites/ninja_left.png"
        self.ninja_up = "/home/paul/learn-arcade-work/Lab 08 - Sprites/ninja_up.png"
        self.ninja_down = "/home/paul/learn-arcade-work/Lab 08 - Sprites/ninja_down.png"

        # Set up the player
        # Character image from kenney.nl
        self.player_sprite = arcade.Sprite(self.ninja_right, SPRITE_SCALING_PLAYER)
        self.player_sprite.center_x = 50
        self.player_sprite.center_y = 50
        self.player_list.append(self.player_sprite)

        # Create the coins
        for i in range(COIN_COUNT):

            # Create the coin instance
            # Coin image from kenney.nl
            coin = arcade.Sprite("/home/paul/learn-arcade-work/Lab 08 - Sprites/bacon_coin.gif", SPRITE_SCALING_COIN)

            # center the coin
            coin.center_x = random.randrange(SCREEN_WIDTH)
            coin.center_y = random.randrange(SCREEN_HEIGHT)

            # Add the coin to the lists
            self.coin_list.append(coin)

    def on_draw(self):
        """ Draw everything """
        arcade.start_render()
        self.coin_list.draw()
        self.player_list.draw()

        # Put the text on the screen.
        output = f"Score: {self.score}"
        arcade.draw_text(output, 10, 20, arcade.color.WHITE, 14)

    def on_key_press(self, key, modifiers):
        """Called whenever a key is pressed. """
        if key == arcade.key.UP:
            self.up_pressed = True
        elif key == arcade.key.DOWN:
            self.down_pressed = True
        elif key == arcade.key.LEFT:
            self.left_pressed = True
        elif key == arcade.key.RIGHT:
            self.right_pressed = True

    def on_key_release(self, key, modifiers):
        """Called whenever a key is released. """
        if key == arcade.key.UP:
            self.up_pressed = False
        elif key == arcade.key.DOWN:
            self.down_pressed = False
        elif key == arcade.key.LEFT:
            self.left_pressed = False
        elif key == arcade.key.RIGHT:
            self.right_pressed = False

    def update(self, delta_time):
        """ Movement and game logic """

        # Update player postion based on the keys pressed
        if self.up_pressed and not self.down_pressed:
            self.player_sprite.texture = arcade.load_texture(self.ninja_up)
            if self.player_sprite.center_y > SCREEN_HEIGHT - 18:
                self.player_sprite.center_y = SCREEN_HEIGHT - 18
            self.player_sprite.change_y = MOVEMENT_SPEED
        elif self.down_pressed and not self.up_pressed:
            self.player_sprite.texture = arcade.load_texture(self.ninja_down)
            if self.player_sprite.center_y < 18:
                self.player_sprite.center_y = 18
            self.player_sprite.change_y = -MOVEMENT_SPEED
        else:
            self.player_sprite.change_y = 0

        if self.left_pressed and not self.right_pressed:
            self.player_sprite.texture = arcade.load_texture(self.ninja_left)
            if self.player_sprite.center_x < 18:
                self.player_sprite.center_x = 18
            self.player_sprite.change_x = -MOVEMENT_SPEED
        elif self.right_pressed and not self.left_pressed:
            self.player_sprite.texture = arcade.load_texture(self.ninja_right)
            if self.player_sprite.center_x > SCREEN_WIDTH - 18:
                self.player_sprite.center_x = SCREEN_WIDTH - 18
            self.player_sprite.change_x = MOVEMENT_SPEED
        else:
            self.player_sprite.change_x = 0

        self.player_sprite.center_x += self.player_sprite.change_x
        self.player_sprite.center_y += self.player_sprite.change_y

        # Call update on all sprites (The sprites don't do much in this
        # example though.)
        self.coin_list.update()

        # Generate a list of all sprites that collided with the player.
        coins_hit_list = arcade.check_for_collision_with_list(self.player_sprite,
                                                              self.coin_list)

        # Loop through each colliding sprite, remove it, and add to the score.
        for coin in coins_hit_list:
            coin.remove_from_sprite_lists()
            self.score += 1


def main():
    """ Main method """
    window = MyGame()
    window.setup()
    arcade.run()


main()
