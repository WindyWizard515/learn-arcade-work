import arcade
import random
import os
import time

SPRITE_SCALING = 0.05
PLAYER_SCALING = 0.2

SCREEN_WIDTH = 1920
SCREEN_HEIGHT = 1015
SCREEN_TITLE = "Astroid Evasion"

MOVEMENT_SPEED = 5
max_speed = 2
last_speed_increase_score = 1

class Laser(arcade.Sprite):
    def update(self):
        # Move the laser
        self.center_y += 15

        if self.center_y >= SCREEN_HEIGHT + 15:
            self.kill()

class Coin(arcade.Sprite):

    def __init__(self, image, scaling):
        super().__init__(image, scaling)
        self.acceleration = 0.1

    def reset_pos(self):
        # Reset above the screen
        self.center_y = random.randrange(SCREEN_HEIGHT, SCREEN_HEIGHT + 100)
        self.center_x = random.randrange(SCREEN_WIDTH)

    def update(self):
        # Accelerate the coin
        if abs(self.change_y) < max_speed:
            self.change_y += self.acceleration if self.change_y > 0 else -self.acceleration

        self.center_y += self.change_y

        # Spin the coin counterclockwise when it moves down
        self.angle += 5

class Pack(arcade.Sprite):
    
    def update(self):
        self.center_y -= 1

class MyGame(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)

        # Sprite lists
        self.coin_list = None
        self.pack_list = None
        self.player_list = None
        self.laser_list = None

        # Set up the playerw
        self.player_sprite = None

        # Track the current key state
        self.up_pressed = False
        self.down_pressed = False
        self.left_pressed = False
        self.right_pressed = False
        self.space_pressed = False

        self.player_lives = 3
        self.score = 0

        self.laser_amount = 5

        # Track the start time
        self.start_time = time.time()

        # Countdown timer for game start delay
        self.countdown_time = 2

        self.player_speed = 1

    def setup(self):
        # Sprite lists
        self.coin_list = arcade.SpriteList()
        self.pack_list = arcade.SpriteList()
        self.player_list = arcade.SpriteList()
        self.laser_list = arcade.SpriteList()

        # Coin
        for coin in range(200):
            self.coin_png = "/home/paul/learn-arcade-work/Lab 09 - Sprites and Walls/astroid.png"
            self.coin = Coin(self.coin_png, 0.07)
            self.coin.center_x = random.randrange(SCREEN_WIDTH)
            self.coin.center_y = random.randrange(SCREEN_HEIGHT + 30, SCREEN_HEIGHT + 50000)
            self.coin_list.append(self.coin)
            
        # Player
        self.player = "/home/paul/learn-arcade-work/Lab 09 - Sprites and Walls/spaceship.gif"
        self.player_sprite = arcade.Sprite(self.player, PLAYER_SCALING)
        self.player_sprite.center_x = 960
        self.player_sprite.center_y = 507.5
        self.player_list.append(self.player_sprite)

        # Background image
        self.background_image = arcade.load_texture("/home/paul/learn-arcade-work/Lab 09 - Sprites and Walls/background.jpg")

    def on_draw(self):
        self.clear()
        arcade.draw_lrwh_rectangle_textured(0, 0, SCREEN_WIDTH, SCREEN_HEIGHT, self.background_image)
        self.player_list.draw()
        self.coin_list.draw()
        self.laser_list.draw()
        self.pack_list.draw()

        output = f"Score: {self.score}, System Health: {self.player_lives}, Laser Shots: {self.laser_amount}"
        arcade.draw_text(output, 10, 20, arcade.color.WHITE, 14)

    def on_mouse_press(self, x, y, button, key_modifiers):
        """ Called when the user presses a mouse button. """
        self.handle_space_bar()

    def on_mouse_release(self, x: float, y: float, button: int, modifiers: int):
        """ Called when the user releases a mouse button. """
        pass

    def on_mouse_motion(self, x: float, y: float, dx: float, dy: float):
        """ Called when the user moves the mouse. """
        pass

    def on_key_press(self, key, modifiers):
        if key == arcade.key.UP or key == arcade.key.W:
            self.up_pressed = True
        elif key == arcade.key.DOWN or key == arcade.key.S:
            self.down_pressed = True
        elif key == arcade.key.LEFT or key == arcade.key.A:
            self.player_sprite.angle += 15
            self.left_pressed = True
        elif key == arcade.key.RIGHT or key == arcade.key.D:
            self.player_sprite.angle -= 15
            self.right_pressed = True
        elif key == arcade.key.ESCAPE:
            print(f"\n\n\n                              Your score was {self.score}\n\n\n")
            exit()
        if key == arcade.key.SPACE and not self.space_pressed:
            self.space_pressed = True
            self.handle_space_bar()

    def on_key_release(self, key, modifiers):
        if key == arcade.key.UP or key == arcade.key.W:
            self.up_pressed = False
        elif key == arcade.key.DOWN or key == arcade.key.S:
            self.down_pressed = False
        elif key == arcade.key.LEFT or key == arcade.key.A:
            self.player_sprite.angle -= 15
            self.left_pressed = False
        elif key == arcade.key.RIGHT or key == arcade.key.D:
            self.player_sprite.angle += 15 
            self.right_pressed = False
        if key == arcade.key.SPACE:
            self.space_pressed = False

    def handle_space_bar(self):
        if self.laser_amount > 0 and time.time() - self.start_time >= self.countdown_time:
            self.laser_png = ":resources:images/space_shooter/laserRed01.png"
            self.laser_sprite = Laser(self.laser_png, 1)
            self.laser_sprite.center_x = self.player_sprite.center_x
            self.laser_sprite.center_y = self.player_sprite.center_y + 40
            self.laser_list.append(self.laser_sprite)
            
            self.laser_amount -= 1

    def update(self, delta_time):
        global max_speed
        global last_speed_increase_score
        if time.time() - self.start_time < self.countdown_time:
            return
        
        if self.score % 25 == 0 and self.score != 0 and self.score != last_speed_increase_score:
            max_speed += 1
            if self.score % 50 == 0 and self.score != 0 and self.score != last_speed_increase_score:
                self.player_speed += 1
                last_speed_increase_score = self.score
            last_speed_increase_score = self.score


        
        if time.time() - self.start_time - self.countdown_time >= 5:
            self.pack_png = ":resources:images/items/gemRed.png"
            self.pack = Pack(self.pack_png, .5)
            self.pack.center_x = random.randrange(SCREEN_WIDTH)
            self.pack.center_y = SCREEN_HEIGHT - 10
            self.pack_list.append(self.pack)
            self.start_time = time.time() - self.countdown_time

        self.coin_list.update()
        self.pack_list.update()
        self.laser_list.update()

        if self.up_pressed and not self.down_pressed:
            if self.player_sprite.center_y > SCREEN_HEIGHT - 25:
                self.player_sprite.center_y = SCREEN_HEIGHT - 25
            self.player_sprite.change_y = MOVEMENT_SPEED
        elif self.down_pressed and not self.up_pressed:
            if self.player_sprite.center_y < -15:
                print(f"\n\n\n                              Your score was {self.score}\n\n\n")
                exit()
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
        self.player_sprite.center_y += self.player_sprite.change_y - int(self.player_speed)

        self.coin_list.update()
        self.pack_list.update()
        self.laser_list.update()

        coins_hit_list = arcade.check_for_collision_with_list(self.player_sprite, self.coin_list)

        for laser in self.laser_list:
            coin_hit_laser = arcade.check_for_collision_with_list(laser, self.coin_list)
            for coin in coin_hit_laser:
                coin.remove_from_sprite_lists()
                laser.remove_from_sprite_lists()
                self.coin_png = "/home/paul/learn-arcade-work/Lab 09 - Sprites and Walls/astroid.png"
                self.coin = Coin(self.coin_png, 0.07)
                self.coin.center_x = random.randrange(SCREEN_WIDTH)
                self.coin.center_y = random.randrange(SCREEN_HEIGHT + 30, SCREEN_HEIGHT + 5000)
                self.coin_list.append(self.coin)

                self.score += 1

        for coin in coins_hit_list:
            coin.remove_from_sprite_lists()
            self.coin_png = "/home/paul/learn-arcade-work/Lab 09 - Sprites and Walls/astroid.png"
            self.coin = Coin(self.coin_png, 0.07)
            self.coin.center_x = random.randrange(SCREEN_WIDTH)
            self.coin.center_y = random.randrange(SCREEN_HEIGHT + 30, SCREEN_HEIGHT + 5000)
            self.coin_list.append(self.coin)
            self.player_lives -= 1

            if self.player_lives <= 0:
                print(f"\n\n\n                              Your score was {self.score}\n\n\n")
                exit()

        pack_hit = arcade.check_for_collision_with_list(self.player_sprite, self.pack_list)

        for pack in pack_hit:
            pack.remove_from_sprite_lists()
            self.laser_amount += 1

        
        if self.player_sprite.center_y < -15:
            print(f"\n\n\n                              Your score was {self.score}\n\n\n")
            exit()


def main():
    os.system("clear")
    window = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    window.setup()
    arcade.run()

if __name__ == "__main__":
    main()
