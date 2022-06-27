
from GameLogic.Minefield import Minefield

class Game:
    """A minesweeper game with a board and turns"""

    GAME_ONGOING = 0
    GAME_OVER = 1
    GAME_WON = 2

    def __init__(self):

        self.set_difficulty()

        # minefield for the game with difficulty selected
        self.minefield = Minefield(*self.difficulty)

        # variable for whether game has been won, lost or is ongoing
        self.game_status = self.GAME_ONGOING

    def set_difficulty(self):
        """Set the games difficulty mode"""

        # Modes by (field_size, no_of_mines)
        difficulty_modes = [(10,10), (14,40), (18,50)]

        # Get input for the mode
        # Change this to be from minecraft window
        mode = 2
        #mode = int(input("Difficulty mode: "))
        self.difficulty = difficulty_modes[mode]
        

    def turn(self, x, y):
        # run selection and set game_status
        game_over = self.minefield.select(x, y)
        if game_over:
            self.game_status = self.GAME_OVER

        elif self.minefield.check_cleared():
            self.game_status = self.GAME_WON

    def game_ending(self):
        if self.game_status == 1:
            print("YOU LOOOOOOSE!")
        elif self.game_status == 2:
            print("Woohoo you a winnnnennnnnrer")        
        elif self.game_status == 0:
            print("Error this shouldn't happen - it's 0")
        else:
            print("Error this shouldn't happen - it's something else")