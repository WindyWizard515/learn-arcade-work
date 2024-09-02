import arcade
import os
os.system("clear")

# Set how many columns and columns we will have
ROW_COUNT = 10
COLUMN_COUNT = 10

# This sets the WIDTH and HEIGHT of each grid location
WIDTH = 20
HEIGHT = 20

# This sets the margin between each cell
# and on the edges of the screen.
MARGIN = 5

# Do the math to figure out our screen dimensions
SCREEN_WIDTH = (WIDTH + MARGIN) * COLUMN_COUNT + MARGIN
SCREEN_HEIGHT = (HEIGHT + MARGIN) * ROW_COUNT + MARGIN



class MyGame(arcade.Window):
    """
    Main application class.
    """

    def __init__(self, width, height):
        """
        Set up the application.
        """
        super().__init__(width, height)
        self.cells_selected = 0
        
        self.row_1_cells = 0
        self.row_2_cells = 0
        self.row_3_cells = 0
        self.row_4_cells = 0
        self.row_5_cells = 0
        self.row_6_cells = 0
        self.row_7_cells = 0
        self.row_8_cells = 0
        self.row_9_cells = 0
        self.row_10_cells = 0
        
        self.column_1_cells = 0
        self.column_2_cells = 0
        self.column_3_cells = 0
        self.column_4_cells = 0
        self.column_5_cells = 0
        self.column_6_cells = 0
        self.column_7_cells = 0
        self.column_8_cells = 0
        self.column_9_cells = 0
        self.column_10_cells = 0
        
        self.continuous_count = 0
        self.max_continuous_found = 0
 
        # Create a 2 dimensional array. A two dimensional
        # array is simply a list of lists.
        self.grid = []
        for row in range(ROW_COUNT):
            # Add an empty array that will hold each cell
            # in this row
            self.grid.append([])
            for column in range(COLUMN_COUNT):
                self.grid[row].append(0)  # Append a cell
        

        arcade.set_background_color(arcade.color.BLACK)

    def on_draw(self):
        """
        Render the screen.
        """

        # This command has to happen before we start drawing
        arcade.start_render()

        # Draw the grid
        for row in range(ROW_COUNT):
            for column in range(COLUMN_COUNT):
                # Figure out what color to draw the box
                if self.grid[row][column] == 1:
                    color = arcade.color.GREEN
                else:
                    color = arcade.color.WHITE

                # Do the math to figure out where the box is
                x = (MARGIN + WIDTH) * column + MARGIN + WIDTH // 2
                y = (MARGIN + HEIGHT) * row + MARGIN + HEIGHT // 2

                # Draw the box
                arcade.draw_rectangle_filled(x, y, WIDTH, HEIGHT, color)

    def on_mouse_press(self, x, y, button, modifiers):
        """
        Called when the user presses a mouse button.
        """

        # Change the x/y screen coordinates to grid coordinates
        column = x // (WIDTH + MARGIN)
        row = y // (HEIGHT + MARGIN)

        # Make sure we are on-grid. It is possible to click in the upper right
        # corner in the margin and go to a grid location that doesn't exist
        if row < ROW_COUNT and column < COLUMN_COUNT:

            # Flip the location between 1 and 0.
            if self.grid[row][column] == 0:
                self.grid[row][column] = 1
                self.cells_selected += 1
            else:
                self.grid[row][column] = 0
                self.cells_selected -= 1
                
            if row == 0:
                if self.grid[row][column] == 0:
                    self.row_1_cells -= 1
                else:
                    self.row_1_cells += 1
            if row == 1:
                if self.grid[row][column] == 0:
                    self.row_2_cells -= 1
                else:
                    self.row_2_cells += 1
            if row == 2:
                if self.grid[row][column] == 0:
                    self.row_3_cells -= 1
                else:
                    self.row_3_cells += 1
            if row == 3:
                if self.grid[row][column] == 0:
                    self.row_4_cells -= 1
                else:
                    self.row_4_cells += 1
            if row == 4:
                if self.grid[row][column] == 0:
                    self.row_5_cells -= 1
                else:
                    self.row_5_cells += 1
            if row == 5:
                if self.grid[row][column] == 0:
                    self.row_6_cells -= 1
                else:
                    self.row_6_cells += 1
            if row == 6:
                if self.grid[row][column] == 0:
                    self.row_7_cells -= 1
                else:
                    self.row_7_cells += 1
            if row == 7:
                if self.grid[row][column] == 0:
                    self.row_8_cells -= 1
                else:
                    self.row_8_cells += 1
            if row == 8:
                if self.grid[row][column] == 0:
                    self.row_9_cells -= 1
                else:
                    self.row_9_cells += 1
            if row == 9:
                if self.grid[row][column] == 0:
                    self.row_10_cells -= 1
                else:
                    self.row_10_cells += 1
                    
            if column == 0:
                if self.grid[row][column] == 0:
                    self.column_1_cells -= 1
                else:
                    self.column_1_cells += 1
            if column == 1:
                if self.grid[row][column] == 0:
                    self.column_2_cells -= 1
                else:
                    self.column_2_cells += 1
            if column == 2:
                if self.grid[row][column] == 0:
                    self.column_3_cells -= 1
                else:
                    self.column_3_cells += 1
            if column == 3:
                if self.grid[row][column] == 0:
                    self.column_4_cells -= 1
                else:
                    self.column_4_cells += 1
            if column == 4:
                if self.grid[row][column] == 0:
                    self.column_5_cells -= 1
                else:
                    self.column_5_cells += 1
            if column == 5:
                if self.grid[row][column] == 0:
                    self.column_6_cells -= 1
                else:
                    self.column_6_cells += 1
            if column == 6:
                if self.grid[row][column] == 0:
                    self.column_7_cells -= 1
                else:
                    self.column_7_cells += 1
            if column == 7:
                if self.grid[row][column] == 0:
                    self.column_8_cells -= 1
                else:
                    self.column_8_cells += 1
            if column == 8:
                if self.grid[row][column] == 0:
                    self.column_9_cells -= 1
                else:
                    self.column_9_cells += 1
            if column == 9:
                if self.grid[row][column] == 0:
                    self.column_10_cells -= 1
                else:
                    self.column_10_cells += 1
                
        def continuous_count_math_row(row_number):
            self.continuous_count = 0
            self.max_continuous_found = 0
            for i in range(ROW_COUNT):
                if self.grid[row_number][i] == 1:
                    self.continuous_count += 1
                else:
                    if self.continuous_count > self.max_continuous_found:
                        self.max_continuous_found = self.continuous_count
                    self.continuous_count = 0
                
            if self.max_continuous_found > 1:
                print(f"There are {self.max_continuous_found} continuous blocks selected on row {row_number + 1}")
                
        def continuous_count_math_column(column_number):
            self.continuous_count = 0
            self.max_continuous_found = 0
            for i in range(ROW_COUNT):
                if self.grid[i][column_number] == 1:
                    self.continuous_count += 1
                else:
                    if self.continuous_count > self.max_continuous_found:
                        self.max_continuous_found = self.continuous_count
                    self.continuous_count = 0
                
            if self.max_continuous_found > 1:
                print(f"There are {self.max_continuous_found} continuous blocks selected on column {column_number + 1}")
                
        print(f"Total of {self.cells_selected} cells are selected.")
        continuous_count_math_row(0)
        print(f"Row 1 has {self.row_1_cells} cells selected.")
        continuous_count_math_row(1)
        print(f"Row 2 has {self.row_2_cells} cells selected.")
        continuous_count_math_row(2)
        print(f"Row 3 has {self.row_3_cells} cells selected.")
        continuous_count_math_row(3)
        print(f"Row 4 has {self.row_4_cells} cells selected.")
        continuous_count_math_row(4)
        print(f"Row 5 has {self.row_5_cells} cells selected.")
        continuous_count_math_row(5)
        print(f"Row 6 has {self.row_6_cells} cells selected.")
        continuous_count_math_row(6)
        print(f"Row 7 has {self.row_7_cells} cells selected.")
        continuous_count_math_row(7)
        print(f"Row 8 has {self.row_8_cells} cells selected.")
        continuous_count_math_row(8)
        print(f"Row 9 has {self.row_9_cells} cells selected.")
        continuous_count_math_row(9)
        print(f"Row 10 has {self.row_10_cells} cells selected.")
        continuous_count_math_column(0)
        print(f"Column 1 has {self.column_1_cells} cells selected.")
        continuous_count_math_column(1)
        print(f"Column 2 has {self.column_2_cells} cells selected.")
        continuous_count_math_column(2)
        print(f"Column 3 has {self.column_3_cells} cells selected.")
        continuous_count_math_column(3)
        print(f"Column 4 has {self.column_4_cells} cells selected.")
        continuous_count_math_column(4)
        print(f"Column 5 has {self.column_5_cells} cells selected.")
        continuous_count_math_column(5)
        print(f"Column 6 has {self.column_6_cells} cells selected.")
        continuous_count_math_column(6)
        print(f"Column 7 has {self.column_7_cells} cells selected.")
        continuous_count_math_column(7)
        print(f"Column 8 has {self.column_8_cells} cells selected.")
        continuous_count_math_column(8)
        print(f"Column 9 has {self.column_9_cells} cells selected.")
        continuous_count_math_column(9)
        print(f"Column 10 has {self.column_10_cells} cells selected.")


def main():

    MyGame(SCREEN_WIDTH, SCREEN_HEIGHT)
    arcade.run()


if __name__ == "__main__":
    main()
    os.system("clear")