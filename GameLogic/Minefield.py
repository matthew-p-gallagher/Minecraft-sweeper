import numpy as np


class Minefield:
    """A minesweeper board - n x n grid of either mine or no. of neighbouring mines"""

    def __init__(self, field_size, no_of_mines):

        # create a minefield - an array of -1 for mine and 0 for empty
        self.minefield = Minefield._create_minefield(field_size, no_of_mines)

        # for empty squares count neighbouring mines
        self.counted = Minefield._count_neighbours(self.minefield)

    def _create_minefield(n, b):

        # create 1D array and add mines
        area = np.zeros(n * n, dtype=int)
        area[:b] = -1

        # randomise the mine placement
        # TODO remove seed
        np.random.seed(1000)
        np.random.shuffle(area)

        # shape into square grid
        area = area.reshape((n, n))

        return area

    def _count_neighbours(minefield):

        # create a new array rather than calculate in place
        counted = np.copy(minefield)

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
                    counted[i, j] = -1 * minefield[i1:i2, j1:j2].sum()

        return counted

    def display(self):
        print(self.minefield)
        print()
        print(self.counted)


if __name__ == "__main__":

    area = Minefield(10, 10)
    area.display()
