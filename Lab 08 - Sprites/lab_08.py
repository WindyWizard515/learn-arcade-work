import random
import arcade
import os
import time

# --- Constants ---
SPRITE_SCALING_PLAYER = .125
SPRITE_SCALING_COIN = 0.2
COIN_COUNT = 50

SCREEN_WIDTH = 1920
SCREEN_HEIGHT = 1015
MOVEMENT_SPEED = 5
SPRITE_SPEED = 1
max_speed = 1

def instructions():
    os.system("clear")
    print("\n\n\n                            Hello, and welcome to the game \"Coin Collection\"")
    print("       The goal of the game is the get the most amount of the big coins while staying away from the small coins")
    print("                      The coins that you want to collect are the big coins that are falling down")
    print("          The bad coins take one of your lives away and they are small and bounce around on the screen edges")
    print("You control the ninja character by using the arrow keys, you start the game in the bottom left corner next to your lives and score")
    print("         You start with 3 lives and if you hit the bad coins they take away lives, every 100 coins you get another life.")
    print("                If you ever want to exit the game just press the escape button and the window will close")
    print("                                  For the first 5 seconds you will be invincible")
    test_for_enter = input("\n                              Once you are ready to start, press any key")
    os.system("clear")


class good_Coin(arcade.Sprite):
    """
    This class represents the coins on our screen. It is a child class of
    the arcade library's "Sprite" class.
    """

    def reset_pos(self):
        # Reset the coin to a random spot above the screen
        self.center_y = random.randrange(SCREEN_HEIGHT + 20, SCREEN_HEIGHT + 100)
        self.center_x = random.randrange(SCREEN_WIDTH)

    def update(self):
        # Move the coin
        self.center_y -= 1

        # See if the coin has fallen off the bottom of the screen.
        # If so, reset it.
        if self.top < 0:
            self.reset_pos()

class bad_Coin(arcade.Sprite):
    def __init__(self, image, scaling):
        super().__init__(image, scaling)
        self.change_x = random.choice([-1, 1])
        self.change_y = random.choice([-1, 1])
        self.acceleration = 0.1
        max_speed = 2

    def update(self):
        # Accelerate the coin
        if abs(self.change_x) < max_speed:
            self.change_x += self.acceleration if self.change_x > 0 else -self.acceleration
        if abs(self.change_y) < max_speed:
            self.change_y += self.acceleration if self.change_y > 0 else -self.acceleration

        # Move the coin
        self.center_x += self.change_x
        self.center_y += self.change_y

        # Bounce off the edges
        if self.left < 0 or self.right > SCREEN_WIDTH:
            self.change_x *= -1
        if self.bottom < 0 or self.top > SCREEN_HEIGHT:
            self.change_y *= -1


class MyGame(arcade.Window):
    global score
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

        # Track the start time
        self.start_time = time.time()

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
        self.player_sprite = arcade.Sprite(self.ninja_right, SPRITE_SCALING_PLAYER)
        self.player_sprite.center_x = 50
        self.player_sprite.center_y = 50
        self.player_list.append(self.player_sprite)

        # Create the coins
        for i in range(COIN_COUNT):
            # Create the coin instance
            coin = good_Coin("/home/paul/learn-arcade-work/Lab 08 - Sprites/bacon_coin.png", SPRITE_SCALING_COIN)
            bad_coin = bad_Coin("/home/paul/learn-arcade-work/Lab 08 - Sprites/snout_coin.png", SPRITE_SCALING_COIN)

            # center the coin
            coin.center_x = random.randrange(SCREEN_WIDTH)
            coin.center_y = random.randrange(SCREEN_HEIGHT)
            coin.change_x = random.randrange(-3, 4)
            coin.change_y = random.randrange(-3, 4)

            # center bad coin
            bad_coin.center_x = random.randrange(SCREEN_WIDTH)
            bad_coin.center_y = random.randrange(SCREEN_HEIGHT)

            # Add the coin to the lists
            self.good_coin_list.append(coin)
            self.bad_coin_list.append(bad_coin)

    def on_draw(self):
        """ Draw everything """
        arcade.start_render()
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
        elif key == arcade.key.ESCAPE:
            exit()

    def on_key_release(self, key, modifiers):
        """Called whenever a key is released. """
        if key == arcade.key.UP:
            self.up_pressed = False
        if key == arcade.key.DOWN:
            self.down_pressed = False
        if key == arcade.key.LEFT:
            self.left_pressed = False
        if key == arcade.key.RIGHT:
            self.right_pressed = False

    def update(self, delta_time):
        """ Movement and game logic """
        global MOVEMENT_SPEED
        # Update player position based on the keys pressed
        if self.up_pressed and not self.down_pressed:
            self.player_sprite.texture = arcade.load_texture(self.ninja_up)
            if self.player_sprite.center_y > SCREEN_HEIGHT + 18:
                self.player_sprite.center_y = 18
            self.player_sprite.change_y = MOVEMENT_SPEED
        elif self.down_pressed and not self.up_pressed:
            self.player_sprite.texture = arcade.load_texture(self.ninja_down)
            if self.player_sprite.center_y < 15:
                self.player_sprite.center_y = SCREEN_HEIGHT - 18
            self.player_sprite.change_y = -MOVEMENT_SPEED
        else:
            self.player_sprite.change_y = 0

        if self.left_pressed and not self.right_pressed:
            self.player_sprite.texture = arcade.load_texture(self.ninja_left)
            if self.player_sprite.center_x < 18:
                self.player_sprite.center_x = SCREEN_WIDTH - 18
            self.player_sprite.change_x = -MOVEMENT_SPEED
        elif self.right_pressed and not self.left_pressed:
            self.player_sprite.texture = arcade.load_texture(self.ninja_right)
            if self.player_sprite.center_x > SCREEN_WIDTH - 18:
                self.player_sprite.center_x = 15
            self.player_sprite.change_x = MOVEMENT_SPEED
        else:
            self.player_sprite.change_x = 0

        self.player_sprite.center_x += self.player_sprite.change_x
        self.player_sprite.center_y += self.player_sprite.change_y

        # Call update on all sprites
        self.good_coin_list.update()
        self.bad_coin_list.update()

        # Generate a list of all sprites that collided with the player.
        coins_hit_list = arcade.check_for_collision_with_list(self.player_sprite, self.good_coin_list)

        # Check if the player is still invincible
        if time.time() - self.start_time > 5:
            bad_hit_list = arcade.check_for_collision_with_list(self.player_sprite, self.bad_coin_list)
        else:
            bad_hit_list = []

        # Loop through each colliding sprite, remove it, and add to the score.
        for coin in coins_hit_list:
            global max_speed
            coin.remove_from_sprite_lists()
            coin = good_Coin("/home/paul/learn-arcade-work/Lab 08 - Sprites/bacon_coin.png", SPRITE_SCALING_COIN)
            self.good_coin_list.append(coin)
            self.score += 1
            if self.score % 100 == 0 and self.score != 0:
                level_up = arcade.load_sound("/home/paul/learn-arcade-work/Lab 08 - Sprites/level_up.wav")
                arcade.play_sound(level_up)
                self.player_lives += 1
            elif self.score % 50 == 0 and self.score != 0:
                max_speed += 1
                speed_up = arcade.load_sound("/home/paul/learn-arcade-work/Lab 08 - Sprites/speed_up.wav")
                arcade.play_sound(speed_up)
            else:
                good_coin_sound = arcade.load_sound("/home/paul/learn-arcade-work/Lab 08 - Sprites/good_coin.wav")
                arcade.play_sound(good_coin_sound)

        for coin in bad_hit_list:
            bad_coin_sound = arcade.load_sound("/home/paul/learn-arcade-work/Lab 08 - Sprites/bad_coin.wav")
            coin.remove_from_sprite_lists()
            arcade.play_sound(bad_coin_sound)
            self.player_lives -= 1
            bad_coin = bad_Coin("/home/paul/learn-arcade-work/Lab 08 - Sprites/snout_coin.png", SPRITE_SCALING_COIN)
            self.bad_coin_list.append(bad_coin)
            if self.player_lives <= 0:
                arcade.close_window()
                arcade.open_window(1920, 1015, "Game Over")
                arcade.set_background_color(arcade.csscolor.BLUE)
                arcade.start_render()
                arcade.draw_text(f"Game over! Your score was {self.score}", 500, 507.5, arcade.color.GREEN, 50, 500, "left")
                arcade.run()

def main():
    """ Main method """
    instructions()
    window = MyGame()
    window.setup()
    arcade.run()

main()
