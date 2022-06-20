
from GameLogic.Minefield import Minefield

class Game:
    """A minesweeper game with a board and turns"""

    def __init__(self, d):

        difficulty = [(10,10), (20,20), (40,50)]

        # minefield for the game with difficulty selected
        self.minefield = Minefield(*difficulty[d])

        game_over = False

        while not game_over:

            self.minefield.display()

            x = int(input("x: "))
            y = int(input("y: "))

            game_over = self.minefield.select(x, y)

            if(game_over):
                print("game_over")