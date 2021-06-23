import random 
import math
from Logger_class import Logger

class Game:
    def __init__(self, players):
        self.player_X = players[0]
 
        
        self.player_O = players[1]


        logger = Logger()
        self.logger = logger
        self.logger.clear_log()

        self.state = {
            'turn': 1,
            'player turn' : 'X',
            'board':[[None, None, None],
                     [None, None, None],
                     [None, None, None]],
            'winner': None
        }

    #find possible moves
    def find_choices(self):
      choices = []
      for row in range(len(self.state['board'])):
        for column in range(len(self.state['board'])):
          if self.state['board'][row][column] == None:
            choices.append([row,column])
      return choices
    
    #check for winner if so update winner
    def check_winner(self):
      #check rows
      for row in self.state['board']:
        if row[0] == row[1] and row[1] == row[2] and row[1] != None:
          self.state['winner'] = self.state['player turn']
      board = self.state['board']
      #check columns
      for col in range(3):
        if board[0][col] == board[1][col] and board[1][col] == board[2][col] and board[1][col] !=None:
          self.state['winner'] = self.state['player turn']
      #check \ diagnol
      if board[0][0] == board[1][1] and board[1][1] == board[2][2] and board[1][1]!= None:
        self.state['winner'] = self.state['player turn']

      #check / diagnol
      if board[2][0] == board[1][1] and board[1][1] == board[0][2] and board[1][1]!= None:
        self.state['winner'] = self.state['player turn']

    def check_if_full(self):
      #go through all values to check if any empty
      full = True
      for row in self.state['board']:
        for value in row:
          if value == None:
            full = False
      if full == True and self.state['winner'] == None:
        self.state['winner'] = 'Tie'

    #complet turn for x or o
    def complete_turn(self):
      #increase turn number
      self.state['turn'] += 1
      choices = self.find_choices()
      
      if self.state['player turn'] == 'X':
        choice = self.player_X.choose_choice(choices)
        self.state['board'][choice[0]][choice[1]] = 'X'
        self.check_winner()
        self.state['player turn'] = 'O'
      else:
        choice = self.player_O.choose_choice(choices)
        choice = self.player_X.choose_choice(choices)
        self.state['board'][choice[0]][choice[1]] = 'O'
        self.check_winner()
        self.state['player turn'] = 'X'
      
    #run until board is full or there is a winner
    def run_to_completion(self):
      while self.state['winner'] == None:
        self.complete_turn()
        self.check_if_full()
          



