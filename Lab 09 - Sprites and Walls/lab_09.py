import arcade
import random
import os
SPRITE_SCALING = .05
PLAYER_SCALING = 0.2

SCREEN_WIDTH = 1920
SCREEN_HEIGHT = 1015
SCREEN_TITLE = "Astroid evasion"

MOVEMENT_SPEED = 5

class Coin(arcade.Sprite):
    """
    This class represents the coins on our screen. It is a child class of
    the arcade library's "Sprite" class.
    """

    def reset_pos(self):
        # Reset the above the screen
        self.center_y = SCREEN_HEIGHT + 30
        self.center_x = random.randrange(SCREEN_WIDTH)

    def update(self):
        # Move the coin
        self.center_y -= 1

        # Spin the coin counterclockwise when it moves down
        self.angle += 5
        if self.center_y == -30:
            self.reset_pos()

class MyGame(arcade.Window):
    """ Main application class. """

    def __init__(self, width, height, title):
        """
        Initializer
        """
        super().__init__(width, height, title)

        # Sprite lists
        self.coin_list = None
        self.wall_list = None
        self.player_list = None

        # Set up the player
        self.player_sprite = None
        self.physics_engine = None

        # Track the current key state
        self.up_pressed = False
        self.down_pressed = False
        self.left_pressed = False
        self.right_pressed = False


    def setup(self):
        """ Set up the game and initialize the variables. """

        # Sprite lists
        self.coin_list = arcade.SpriteList()
        self.player_list = arcade.SpriteList()
        self.wall_list = arcade.SpriteList()

        # Coin
        # File coin by LapisDemon on deviantart.com
        self.coin_png = "/home/paul/learn-arcade-work/Lab 09 - Sprites and Walls/astroid.png"

        self.coin = Coin(self.coin_png, 
                    0.1)
                         

        # center coin
        self.coin.center_x = random.randrange(SCREEN_WIDTH)
        self.coin.center_y = SCREEN_HEIGHT + 18
        
        # Add the coin to the lists
        self.coin_list.append(self.coin)

        # Spaceship by SimeonTemplar on deviantart.com
        self.player = "/home/paul/learn-arcade-work/Lab 09 - Sprites and Walls/spaceship.gif"

        # Set up the player
        self.player_sprite = arcade.Sprite(self.player,
                                           PLAYER_SCALING)
        self.player_sprite.center_x = 50
        self.player_sprite.center_y = 64
        self.player_list.append(self.player_sprite)

        

        # -- Set up the walls
        
        wall = arcade.Sprite("/home/paul/learn-arcade-work/Lab 09 - Sprites and Walls/tile.png",
                            SPRITE_SCALING, )
        self.wall_list.append(wall)

        self.physics_engine = arcade.PhysicsEngineSimple(self.player_sprite,
                                                         self.wall_list)

        # Background image by 13CatsAndCounting on deviantart.com
        self.background_image = arcade.load_texture("/home/paul/learn-arcade-work/Lab 09 - Sprites and Walls/background.jpg")

    def on_draw(self):
        """
        Render the screen.
        """

        # This command has to happen before we start drawing
        self.clear()

        # Draw the background
        arcade.draw_lrwh_rectangle_textured(0, 0, SCREEN_WIDTH, SCREEN_HEIGHT, self.background_image)

        # Draw all the sprites.
        self.player_list.draw()
        self.coin_list.draw()
        self.wall_list.draw()

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
        self.player_sprite.center_y -= 1
        if self.player_sprite.center_y < -15:
            exit()
        # Update player position based on the keys pressed
        if self.up_pressed and not self.down_pressed:
            if self.player_sprite.center_y > SCREEN_HEIGHT - 25:
                self.player_sprite.center_y = SCREEN_HEIGHT - 25
            self.player_sprite.change_y = MOVEMENT_SPEED
        elif self.down_pressed and not self.up_pressed:
            if self.player_sprite.center_y < 15:
                self.player_sprite.center_y = SCREEN_HEIGHT - 18
            self.player_sprite.change_y = -MOVEMENT_SPEED
        else:
            self.player_sprite.change_y = 0

        if self.left_pressed and not self.right_pressed:
            if self.player_sprite.center_x < 18:
                self.player_sprite.center_x = SCREEN_WIDTH - 18
            self.player_sprite.change_x = -MOVEMENT_SPEED
        elif self.right_pressed and not self.left_pressed:
            if self.player_sprite.center_x > SCREEN_WIDTH - 18:
                self.player_sprite.center_x = 15
            self.player_sprite.change_x = MOVEMENT_SPEED
        else:
            self.player_sprite.change_x = 0

        self.player_sprite.center_x += self.player_sprite.change_x
        self.player_sprite.center_y += self.player_sprite.change_y

        # Call update on all sprites
        self.coin_list.update()

        # Generate a list of all sprites that collided with the player.
        coins_hit_list = arcade.check_for_collision_with_list(self.player_sprite, self.coin_list)
    def on_update(self, delta_time):
        """ Movement and game logic """

        # Call update on all sprites (The sprites don't do much in this
        # example though.)
        self.physics_engine.update()


def main():
    """ Main function """
    os.system("clear")
    window = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()