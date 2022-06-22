
from GameLogic.Minefield import Minefield

class Game:
    """A minesweeper game with a board and turns"""

    GAME_ONGOING = 0
    GAME_OVER = 1
    GAME_WON = 2

    def __init__(self, mode):

        # set difficulty mode
        difficulty_modes = [(10,10), (20,20), (40,50)]
        difficulty = difficulty_modes[mode]

        # minefield for the game with difficulty selected
        self.minefield = Minefield(*difficulty)

        # variable for whether game has been won, lost or is ongoing
        self.game_status = self.GAME_ONGOING


    def turn(self):
        self.minefield.display()

        x = int(input("x: "))
        y = int(input("y: "))
        
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
            print("Woohoo you a winnnnernnnnnrer")        
        elif self.game_status == 0:
            print("Error this shouldn't happen - it's 0")
        else:
            print("Error this shouldn't happen - it's something else")