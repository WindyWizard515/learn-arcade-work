import arcade
import os

WIDTH = 20
HIGHT = 20
MARGIN = 5

ROW_COUNT = 10
COLUMN_COUNT = 10

SCREEN_WIDTH =  ROW_COUNT * WIDTH + (MARGIN * 11)
SCREEN_HEIGHT = COLUMN_COUNT * HIGHT + (MARGIN * 11)

class MyGame(arcade.Window):
    """
    Main application class.
    """

    def __init__(self, width, height):
        super().__init__(width, height)

        arcade.set_background_color(arcade.color.BLACK)
        self.grid = []
        for row in range(ROW_COUNT):
            self.grid.append([])
            for column in range(COLUMN_COUNT):
                self.grid[row].append(0)
                
        self.grid[1][5] = 1

    def on_draw(self):
        """
        Render the screen.
        """

        arcade.start_render()
        for column in range(COLUMN_COUNT):
            for row in range(ROW_COUNT):
                if self.grid[row][column] == 1:
                    self.color = arcade.color.GREEN
                else:
                    self.color = arcade.color.WHITE
                center_x = (MARGIN + WIDTH) * column + MARGIN + (WIDTH // 2)
                center_y = (MARGIN + HIGHT) * row + MARGIN + (HIGHT // 2)
                arcade.draw_rectangle_filled(center_x, center_y, WIDTH, HIGHT, self.color)

    def on_mouse_press(self, x, y, button, key_modifiers):
        """
        Called when the user presses a mouse button.
        """
        
        column = x // (WIDTH + MARGIN)
        row = y // (HIGHT + MARGIN)
        
        print(f"Click coordinates: ({x}, {y}). Grid coordinates: ({row}, {column})")
        
        if row < ROW_COUNT and column < COLUMN_COUNT:

            # Flip the location between 1 and 0.
            if self.grid[row][column] == 0:
                self.grid[row][column] = 1
            else:
                self.grid[row][column] = 0


def main():

    MyGame(SCREEN_WIDTH, SCREEN_HEIGHT)
    arcade.run()


if __name__ == "__main__":
    os.system("clear")
    main()