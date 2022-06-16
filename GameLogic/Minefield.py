
import numpy as np

class Minefield:
    """A minesweeper board - nxn grid of either bomb or no. of neighbouring bombs"""

    BOMB = -1
    EMPTY = 0

    def __init__(self, field_size, no_of_bombs):
        self.minefield = Minefield.create_minefield(field_size, no_of_bombs)
        self.counted = Minefield.count_neighbours(self.minefield)


    def create_minefield(n, b):
        # create 1D array and add bombs
        area = np.zeros(n*n, dtype=int)
        area[:b] = -1

        #randomise the bomb placement
        np.random.seed(1000)
        np.random.shuffle(area)

        # shape into square grid
        area = area.reshape((n,n))
        
        return area

    def count_neighbours(minefield):

        counted = np.copy(minefield)

        x, y = minefield.shape
        for i in range(x):
            for j in range(y):

                i1 = i - 1
                i2 = i + 2
                j1 = j - 1
                j2 = j + 2

                if i == 0:
                    i1 = 0
                elif i == x - 1:
                    i2 = x

                if j == 0:
                    j1 = 0
                elif j == y - 1:
                    j2 = y

                if minefield[i,j] == -1:
                    continue
                else:
                    counted[i,j] = -1 * minefield[i1:i2, j1:j2].sum()
                    
        return counted

                



    def display(self):
        print(self.minefield)
        print()
        print(self.counted)

if __name__ == "__main__":

    area = Minefield(10, 10)
    area.display()