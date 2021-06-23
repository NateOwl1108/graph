from tic_tac_toe_game_class import Game
from player_classes import RandomPlayer

players = [RandomPlayer(), RandomPlayer()]
game = Game(players)


game.complete_turn()
print(game.state)
print('')
game.run_to_completion()
print(game.state)
