from GameLogic.Minefield import Minefield
from GameLogic.Game import Game

game = Game(0)

while(True):
    # play a selection
    # this could change game status
    game.turn()
    # check game status for win/loss
    if game.game_status > 0:
        break

game.game_ending()
