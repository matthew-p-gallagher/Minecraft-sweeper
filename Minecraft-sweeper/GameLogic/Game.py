
from GameLogic.Minefield import Minefield

class Game:
    """A minesweeper game with a board and turns"""

    GAME_ONGOING = 0
    GAME_OVER = 1
    GAME_WON = 2

    def __init__(self, mode):

        self.set_difficulty(mode)

        # minefield for the game with difficulty selected
        self.minefield = Minefield(*self.difficulty)

        # variable for whether game has been won, lost or is ongoing
        self.game_status = self.GAME_ONGOING

    def set_difficulty(self, mode):
        """Set the games difficulty mode"""

        # Modes by (field_size, no_of_mines)
        difficulty_modes = [(4,3), (10,10), (14,40), (18,50), (80, 800)]

        #mode = int(input("Difficulty mode: "))
        self.difficulty = difficulty_modes[mode]
        

    def turn(self, x, y):
        # run selection and set game_status
        game_over = self.minefield.select(x, y)
        if game_over:
            self.game_status = self.GAME_OVER

        elif self.minefield.check_cleared():
            self.game_status = self.GAME_WON