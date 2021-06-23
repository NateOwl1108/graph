from random import random
import math

class RandomPlayer():
    def __init__(self):
        self.player = None

    def set_player(self, n):
        self.player = n

    def choose_choice(self, choices):
        random_idx = math.floor(len(choices) * random())
        return choices[random_idx]
