import arcade

# Variables that stay the same
SCREEN_WIDTH = 1920
SCREEN_HIGHT = 1080
SCREEN_TITLE = "Dune Raiders"

# Used to change the size of the sprites
CHARACTER_SCALING = 1
TILE_SCALING = 0.5

# Pixles per frame
PLAYER_MOVEMENT_SPEED = 5


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

        # Set the background color to a saddle brown
        arcade.set_background_color(arcade.csscolor.SADDLE_BROWN)

    def setup(self):
        """ Sets up some Sprites/The Game """

        # Start up the scene
        self.scene = arcade.Scene()

        # Create the sprite lists in the scene
        self.scene.add_sprite_list("Player")
        self.scene.add_sprite_list("Walls", use_spatial_hash=True)

        """ Image From https://opengameart.org/forumtopic/i-need-a-scifispacespacesuit-for-my-2d-scifi-platform-shooter """
        # Set up the Player Sprites
        image_source = "Lab 12 - Final Lab/player(R).png"
        self.player_sprite = arcade.Sprite(image_source, CHARACTER_SCALING)

        self.player_sprite.center_x = 64
        self.player_sprite.center_y = 135

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

        # Create the Physics engine variable
        self.physics_engine = arcade.PhysicsEngineSimple(self.player_sprite, self.scene.get_sprite_list("Walls"))

    def on_key_press(self, key, modifiers):
        """Called whenever a key is pressed."""

        if key == arcade.key.UP or key == arcade.key.W:
            self.player_sprite.change_y = PLAYER_MOVEMENT_SPEED
        elif key == arcade.key.DOWN or key == arcade.key.S:
            self.player_sprite.change_y = -PLAYER_MOVEMENT_SPEED
        elif key == arcade.key.LEFT or key == arcade.key.A:
            self.player_sprite.change_x = -PLAYER_MOVEMENT_SPEED
        elif key == arcade.key.RIGHT or key == arcade.key.D:
            self.player_sprite.change_x = PLAYER_MOVEMENT_SPEED

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

    def on_draw(self):
        """Render the screen."""

        # Clear the screen so you can draw the objects
        self.clear()

        # Draw our Scene
        self.scene.draw()
    
    def on_update(self, delta_time):
        """Movement and game logic"""

        # Move the player with the physics engine
        self.physics_engine.update()


def main():
    """Main function"""
    window = MyGame()
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()