import numpy as np


class Minefield:
    """A minefield board for minesweeper game

    - n x n grid of either mine or no. of neighbouring mines
    - added layer for hidden/revealed
    """

    def __init__(self, field_size, no_of_mines):

        # create a minefield - an array of -1 for mine and 0 for empty
        self.mines_only = Minefield._create_minefield(field_size, no_of_mines)

        # for empty squares count neighbouring mines
        self.count_neighbours()

        # create an overlay for hidden/revealed squares
        # 1's for hidden, 0's for revealed
        self.combined = np.stack((np.ones( self.counted.shape, dtype=int ), self.counted))

    def _create_minefield(n, b):

        # create 1D array and add mines
        minefield = np.zeros(n * n, dtype=int)
        minefield[:b] = -1

        # randomise the mine placement
        # TODO remove seed
        np.random.seed(1000)
        np.random.shuffle(minefield)

        # shape into square grid
        minefield = minefield.reshape((n, n))

        return minefield

    def count_neighbours(self):

        minefield = self.mines_only

        # create a new array easier than calculating in place
        self.counted = np.copy(minefield)

        # iterate through all squares in the minefield
        x, y = minefield.shape
        for i in range(x):
            for j in range(y):

                # coords for a 3 x 3 slice around square
                i1 = i - 1
                i2 = i + 2
                j1 = j - 1
                j2 = j + 2
                
                # change the slice of square is at the edge
                if i == 0:
                    i1 = 0
                elif i == x - 1:
                    i2 = x

                if j == 0:
                    j1 = 0
                elif j == y - 1:
                    j2 = y

                # if sqaure is a mine then move on
                # otherwise get sum of neighbouring mines
                if minefield[i, j] == -1:
                    continue
                else:
                    self.counted[i, j] = -1 * minefield[i1:i2, j1:j2].sum()


    def select(self, x, y):
        """Selecting a square - clear squares or game over"""

        # variable to determine if the game has been lost on selection
        game_over = False

        selection = self.combined[1, x, y]

        # if empty, clear neighbouring empties
        if selection == 0:
            self.clear_empties(x, y)

        # if number, clear number only
        elif selection > 0:
            self.combined[0, x, y] = 0
            

        # if mine, game over
        elif selection == -1:
            self.combined[0, x, y] = 0
            game_over = True

        return game_over


    def clear_empties(self, x, y):

        # create a queue of squares to clear with starting square
        queue = [(x,y)]

        # while there are still squares to clear in queue
        while queue != []:

            # take the current coords
            x, y = queue.pop()

            # clear the overlay at current x, y
            self.combined[0, x, y] = 0

            # cycle through neighbours
            for i in range(x-1, x+2):

                # account for boundary i cases
                if i < 0 or i > self.mines_only.shape[0]-1:
                    continue

                for j in range(y-1, y+2):

                    # account for boundary j cases
                    if j < 0 or j > self.mines_only.shape[0]-1:
                        continue

                    found = self.combined[1, i, j]

                    # bombs should not be found here so will throw error
                    if found == -1:
                        print("Bomb found clearing empties")
                        exit(1)

                    # numbers will clear overlay only
                    if found > 0:
                        self.combined[0, i, j] = 0

                    # empties will be added to the continue to go again
                    # extra check that overlay is not 0 avoids repitition
                    if found == 0:
                        if self.combined[0, i, j] != 0:
                            queue.append((i,j))


    def display(self):
        print(self.combined)
        print()


if __name__ == "__main__":

    area = Minefield(10, 10)
    area.display()
