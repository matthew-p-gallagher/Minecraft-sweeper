
import numpy as np

class Minefield:
    """A minesweeper board - nxn grid of either bomb or no. of neighbouring bombs"""

    BOMB = -1
    EMPTY = 0

    def __init__(self, field_size, no_of_bombs):
        self.area = Minefield.area_init(field_size, no_of_bombs)


    def area_init(n, b):
        # create 1D array and add bombs
        area = np.zeros(n*n, dtype=int)
        area[:b] = -1

        #randomise the bomb placement
        np.random.shuffle(area)

        # shape into square grid
        area = area.reshape((n,n))
        
        return area

    def count_neighbours():
        pass


    def display(self):
        print(self.area)

if __name__ == "__main__":

    area = Minefield(10, 10)
    area.display()