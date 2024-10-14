import arcade
import os
os.system("clear")

# Variables that stay the same
SCREEN_WIDTH = 1920
SCREEN_HIGHT = 1080
SCREEN_TITLE = "Dune Raiders"

# Used to change the size of the sprites
CHARACTER_SCALING = 1
TILE_SCALING = 0.5
COIN_SCALING = 0.75

# Pixles per frame
PLAYER_MOVEMENT_SPEED = 5

GRAVITY = 1
PLAYER_JUMP_SPEED = 20


class MyGame(arcade.Window):
    """ The class for the Window """

    def __init__(self):
        """ The initializer function """
        
        # Set up the window speifics
        super().__init__(SCREEN_WIDTH, SCREEN_HIGHT, SCREEN_TITLE)

        # Set up the scene
        self.scene = None

        # Set up the Physics Engine
        self.physics_engine = None

        # Camera for scrolling
        self.camera = None

        # Set the background color to a saddle brown
        arcade.set_background_color(arcade.csscolor.SADDLE_BROWN)

    def setup(self):
        """ Sets up some Sprites/The Game """

        # Setup the camera scrolling
        self.camera = arcade.Camera(self.width, self.height)        
        
        # Load sounds
        self.collect_coin_sound = arcade.load_sound(":resources:sounds/coin1.wav")
        self.jump_sound = arcade.load_sound(":resources:sounds/jump1.wav")

        # Start up the scene
        self.scene = arcade.Scene()

        # Create the sprite lists in the scene
        self.scene.add_sprite_list("Player")
        self.scene.add_sprite_list("Walls", use_spatial_hash=True)
        self.scene.add_sprite_list("Coins", use_spatial_hash=True)

        """ Image From https://opengameart.org/forumtopic/i-need-a-scifispacespacesuit-for-my-2d-scifi-platform-shooter """

        # Set up the Player Sprites
        self.player_right_face = "Lab 12 - Final Lab/player(R).png"
        self.player_left_face = "Lab 12 - Final Lab/player(L).png"
        self.player_sprite = arcade.Sprite(self.player_right_face, CHARACTER_SCALING)

        self.player_sprite.center_x = 55
        self.player_sprite.center_y = 150

        self.scene.add_sprite("Player", self.player_sprite)

        # Create the ground
        for x in range(0, SCREEN_WIDTH+1, 64):
            ground = arcade.Sprite(":resources:images/tiles/grassMid.png", TILE_SCALING)

            ground.center_x = x
            ground.center_y = 64
            self.scene.add_sprite("Walls", ground)

        # Create the crates/blocks
        coordinate_list = [[512, 128], [256, 128], [768, 128]]

        for coordinate in coordinate_list:
            wall = arcade.Sprite(":resources:images/tiles/boxCrate_double.png", TILE_SCALING)
            wall.position = coordinate

            self.scene.add_sprite("Walls", wall)

        # Create the spaceship
        self.spaceship_source = "Lab 12 - Final Lab/spaceship.gif"
        self.spaceship_sprite = arcade.Sprite(self.spaceship_source, TILE_SCALING)

        self.spaceship_sprite.center_x = 50
        self.spaceship_sprite.center_y = 135

        self.scene.add_sprite("Walls", self.spaceship_sprite)

        # Create the coins
        for x in range(128, 1250, 256):
            coin = arcade.Sprite("Lab 12 - Final Lab/wrench.png", COIN_SCALING)

            coin.center_x = x
            coin.center_y = 125
            self.scene.add_sprite("Coins", coin)

        # Create the Physics engine variable
        self.physics_engine = arcade.PhysicsEnginePlatformer(self.player_sprite, gravity_constant=GRAVITY, walls=self.scene.get_sprite_list("Walls"))

    def on_draw(self):
        """Render the screen."""

        # Clear the screen so you can draw the objects
        self.clear()

        # Activate the Camera
        self.camera.use()

        # Draw our Scene
        self.scene.draw()

    def on_key_press(self, key, modifiers):
        """Called whenever a key is pressed."""

        if key == arcade.key.UP or key == arcade.key.W:
            if self.physics_engine.can_jump():
                self.player_sprite.change_y = PLAYER_JUMP_SPEED
                arcade.play_sound(self.jump_sound)
        elif key == arcade.key.DOWN or key == arcade.key.S:
            self.player_sprite.change_y = -PLAYER_MOVEMENT_SPEED
        elif key == arcade.key.LEFT or key == arcade.key.A:
            self.player_sprite.change_x = -PLAYER_MOVEMENT_SPEED
            self.player_sprite.texture = arcade.load_texture(self.player_left_face)
        elif key == arcade.key.RIGHT or key == arcade.key.D:
            self.player_sprite.change_x = PLAYER_MOVEMENT_SPEED
            self.player_sprite.texture = arcade.load_texture(self.player_right_face)

        elif key == arcade.key.ESCAPE:
            exit()

    def on_key_release(self, key, modifiers):
        """Called when the user releases a key."""

        if key == arcade.key.UP or key == arcade.key.W:
            self.player_sprite.change_y = 0
        elif key == arcade.key.DOWN or key == arcade.key.S:
            self.player_sprite.change_y = 0
        elif key == arcade.key.LEFT or key == arcade.key.A:
            self.player_sprite.change_x = 0
        elif key == arcade.key.RIGHT or key == arcade.key.D:
            self.player_sprite.change_x = 0

    def center_camera_to_player(self):
        screen_center_x = self.player_sprite.center_x - (self.camera.viewport_width / 2)
        screen_center_y = self.player_sprite.center_y - (
            self.camera.viewport_height / 2
        )

        # Don't let camera travel past 0
        if screen_center_x < 0:
            screen_center_x = 0
        if screen_center_y < 0:
            screen_center_y = 0
        player_centered = screen_center_x, screen_center_y

        self.camera.move_to(player_centered)

    def on_update(self, delta_time):
        """Movement and game logic"""

        # Move the player with the physics engine
        self.physics_engine.update()

        self.center_camera_to_player()

                # See if we hit any coins
        coin_hit_list = arcade.check_for_collision_with_list(
            self.player_sprite, self.scene["Coins"]
        )

        # Loop through each coin you hit and remove it
        for coin in coin_hit_list:
            coin.remove_from_sprite_lists()
            arcade.play_sound(self.collect_coin_sound)

        if self.player_sprite.center_y < 0:
            exit()


def main():
    """Main function"""
    window = MyGame()
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()