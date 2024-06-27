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

class Coin(arcade.Sprite):
    """
    This class represents the coins on our screen. It is a child class of
    the arcade library's "Sprite" class.
    """

    def reset_pos(self):

        # Reset the coin to a random spot above the screen
        self.center_y = random.randrange(SCREEN_HEIGHT + 20,
                                         SCREEN_HEIGHT + 100)
        self.center_x = random.randrange(SCREEN_WIDTH)

    def update(self):
        # Move the coin
        self.center_y -= 1

        # See if the coin has fallen off the bottom of the screen.
        # If so, reset it.
        if self.top < 0:
            self.reset_pos()

class MyGame(arcade.Window):
    """ Our custom Window Class"""

    def __init__(self):
        """ Initializer """
        # Call the parent class initializer
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "Coin Collection")

        self.background_image = arcade.load_texture(":resources:images/backgrounds/abstract_1.jpg")

        # Variables that will hold sprite lists
        self.player_list = None
        self.good_sprite_list = None
        self.bad_sprite_list = None

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


    def setup(self):
        """ Set up the game and initialize the variables. """

        # Sprite lists
        self.player_list = arcade.SpriteList()
        self.good_coin_list = arcade.SpriteList()
        self.bad_coin_list = arcade.SpriteList()

        # Score
        self.score = 0

        # Player_lives
        self.player_lives = 3

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
            coin = Coin("/home/paul/learn-arcade-work/Lab 08 - Sprites/bacon_coin.png",  SPRITE_SCALING_COIN)
            bad_coin = Coin("/home/paul/learn-arcade-work/Lab 08 - Sprites/snout_coin.png", SPRITE_SCALING_COIN)

            # center the coin
            coin.center_x = random.randrange(SCREEN_WIDTH)
            coin.center_y = random.randrange(SCREEN_HEIGHT)

            # center bad coin
            bad_coin.center_x = random.randrange(SCREEN_WIDTH)
            bad_coin.center_y = random.randrange(SCREEN_HEIGHT)

            # Add the coin to the lists
            self.good_coin_list.append(coin)
            self.bad_coin_list.append(bad_coin)

    def on_draw(self):
        """ Draw everything """
        arcade.start_render()

        arcade.draw_lrwh_rectangle_textured(0, 0, SCREEN_WIDTH, SCREEN_HEIGHT, self.background_image)

        self.good_coin_list.draw()
        self.bad_coin_list.draw()
        self.player_list.draw()
        # Put the text on the screen.
        output = f"Score: {self.score}, Lives: {self.player_lives}"
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
        # example though.
        self.good_coin_list.update()
        self.bad_coin_list.update()

        # Generate a list of all sprites that collided with the player.
        coins_hit_list = arcade.check_for_collision_with_list(self.player_sprite,
                                                              self.good_coin_list)
        bad_hit_list = arcade.check_for_collision_with_list(self.player_sprite,
                                                            self.bad_coin_list)
        

        # Loop through each colliding sprite, remove it, and add to the score.
        for coin in coins_hit_list:
            coin.remove_from_sprite_lists()

            coin = Coin("/home/paul/learn-arcade-work/Lab 08 - Sprites/bacon_coin.png",  SPRITE_SCALING_COIN)
            self.good_coin_list.append(coin)
            self.score += 1
            if self.score % 100 == 0 and self.score != 0:
                level_up = arcade.load_sound("/home/paul/learn-arcade-work/Lab 08 - Sprites/level_up.wav")
                arcade.play_sound(level_up)
                self.player_lives += 1

            else:
                good_coin_sound = arcade.load_sound("/home/paul/learn-arcade-work/Lab 08 - Sprites/good_coin.wav")

                arcade.play_sound(good_coin_sound)




        for coin in bad_hit_list:
            bad_coin_sound = arcade.load_sound("/home/paul/learn-arcade-work/Lab 08 - Sprites/bad_coin.wav")
            coin.remove_from_sprite_lists()

            arcade.play_sound(bad_coin_sound)
            self.player_lives -= 1

            bad_coin = Coin("/home/paul/learn-arcade-work/Lab 08 - Sprites/snout_coin.png",  SPRITE_SCALING_COIN)
            self.bad_coin_list.append(bad_coin)
            if self.player_lives <= 0:
                arcade.close_window()
                arcade.open_window(1920, 1015, "Game Over")
                arcade.start_render()
                arcade.draw_text(f"Game over! Your score was {self.score}", 850, 507.5, arcade.color.WHITE, 12, 500, "left")
                arcade.run()
                


                
def main():
    """ Main method """
    window = MyGame()
    window.setup()
    arcade.run()


main()
