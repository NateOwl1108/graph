
class Node():
  def __init__(self, game_state):
    self.game_state = game_state
    self.possible_moves = next
    self.turn = 'X'

class Tic_Tac_Toe():

  def __init__(self):
    self.game_start = Node([[None,None,None],[None,None,None],[None,None,None]])


  

  def game(self):
    self.game_start.possible_moves = self.game_recursion(self.game_start)
  
  def valid_possible_moves(self, current_state, turn):
    if current_state[0][0] == current_state[1][1] and current_state[2][2] == current_state[1][1] and current_state[1][1] != None :
          return 'home' 
        #diagnol /
    elif current_state[2][0] == current_state[1][1] and current_state[0][2] == current_state[1][1] and current_state[1][1] != None:
          return 'home' 
        #first row
    elif current_state[0][0] == current_state[0][1] and current_state[0][2] == current_state[0][1] and current_state[0][1] != None:
          return 'home'
        #second row
    elif current_state[1][0] == current_state[1][1] and current_state[1][2] == current_state[1][1] and current_state[1][1] != None:
          return 'home'
        #third row
    elif current_state[2][0] == current_state[2][1] and current_state[2][2] == current_state[2][1] and current_state[2][1] != None:
          return 'home'
        #column 1
    elif current_state[0][0] == current_state[1][0] and current_state[2][0] == current_state[1][0] and current_state[2][0] != None:
          return 'home'
        #column 2
    elif current_state[0][1] == current_state[1][1] and current_state[2][1] == current_state[1][1] and current_state[2][1] != None:
          return 'home'
        #column 3
    elif current_state[0][2] == current_state[1][2] and current_state[2][2] == current_state[1][2] and current_state[2][2] != None:
          return 'home'
    possible_moves = []
    for row in range(3):
      for column in range(3):

        possibility = []
        for rows in current_state:
          possibility.append(list(rows))
        
        if current_state[row][column] == None:
          
          if turn == 'X':
            possibility[row][column] = 'X'
            next_move = Node(possibility)
            next_move.turn = 'O'
            
            possible_moves.append(next_move)
          else:
            possibility[row][column] = 'O'
            next_move = Node(possibility)
            possible_moves.append(next_move)
    return possible_moves

  def game_depth(self, node):
    possible_moves = self.valid_possible_moves(node.game_state, node.turn)
    if len(possible_moves) >0:
      for possible_move in possible_moves:
        next_moves = self.valid_possible_moves(possible_move.game_state, possible_move.turn)
        move_list = []
        for move in next_moves:
          if move != 'home':
            move_list.append(move)
        possible_move.possible_moves = move_list
    return possible_moves
  
  def game_recursion(self,node):
    node_depth = self.game_depth(node)

    for move in node_depth:
      for possibility in move.possible_moves:
        if possibility == 'home':
          continue
        elif self.check_for_win(possibility) == False:
          possibility.possible_moves = self.game_recursion(possibility)

        

  def check_for_win(self, possibility):
    if type(possibility) is str:
      return True
    if (possibility.game_state[0][0] == possibility.game_state[1][1] and possibility.game_state[2][2] == possibility.game_state[1][1] and possibility.game_state[1][1] != None) or(possibility.game_state[2][0] == possibility.game_state[1][1] and possibility.game_state[0][2] == possibility.game_state[1][1] and possibility.game_state[1][1] != None) or(possibility.game_state[0][0] == possibility.game_state[0][1] and possibility.game_state[0][2] == possibility.game_state[0][1] and possibility.game_state[0][1] != None) or(possibility.game_state[1][0] == possibility.game_state[1][1] and possibility.game_state[1][2] == possibility.game_state[1][1] and possibility.game_state[1][1] != None) or (possibility.game_state[2][0] == possibility.game_state[2][1] and possibility.game_state[2][2] == possibility.game_state[2][1] and possibility.game_state[2][1] != None) or(possibility.game_state[0][0] == possibility.game_state[1][0] and possibility.game_state[2][0] == possibility.game_state[1][0] and possibility.game_state[2][0] != None) or (possibility.game_state[0][1] == possibility.game_state[1][1] and possibility.game_state[2][1] == possibility.game_state[1][1] and possibility.game_state[2][1] != None) or (possibility.game_state[0][2] == possibility.game_state[1][2] and possibility.game_state[2][2] == possibility.game_state[1][2] and possibility.game_state[2][2] != None):
      return True
    else:
      return False
         



tic_tac_toe = Tic_Tac_Toe()
tic_tac_toe.game()
print(tic_tac_toe.game_start.possible_moves)
for move in tic_tac_toe.game_start.possible_moves:
  for possibility in move.possible_moves:
    print('')
    print(possibility.game_state[0])
    print(possibility.game_state[1])
    print(possibility.game_state[2])
    print('')



