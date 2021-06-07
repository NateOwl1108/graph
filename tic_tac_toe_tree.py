

class Node():
  def __init__(self, game_state):
    self.game_state = game_state
    self.possible_moves = next
    self.turn = 'X'

class Tic_Tac_Toe():

  def __init__(self):
    self.game_start = Node([[None,None,None],[None,None,None],[None,None,None]])

  

  def game(self):
    self.game_start.possible_moves = self.next_possible_moves(self.game_start.game_state, 'X', 0)

  def next_possible_moves(self, current_state, turn, level):
    print('Level ', level)
    possible_moves = []
    for row in range(3):
      for column in range(3):
        possibility = list(current_state)
        print('row', row)
        print('column', column)
        print('turn', turn)
        print(possibility[0])
        print(possibility[1])
        print(possibility[2])
        print('')
        #diagnol \
        
        if current_state[row][column] == None:
          
          if turn == 'X':
            
            possibility[row][column] = 'X'
            print('Good Move ')
            print(possibility[0])
            print(possibility[1])
            print(possibility[2])
            possibility = Node(possibility)
            possibility.turn = 'O'
            if possibility.game_state[0][0] == possibility.game_state[1][1] and possibility.game_state[2][2] == possibility.game_state[1][1] and possibility.game_state[1][1] != None :
              possible_moves.append(possibility)
              continue 
            #diagnol /
            elif possibility.game_state[2][0] == possibility.game_state[1][1] and possibility.game_state[0][2] == possibility.game_state[1][1] and possibility.game_state[1][1] != None:
              possible_moves.append(possibility)
              continue 
            #first row
            elif possibility.game_state[0][0] == possibility.game_state[0][1] and possibility.game_state[0][2] == possibility.game_state[0][1] and possibility.game_state[0][1] != None:
              possible_moves.append(possibility)
              continue
            #second row
            elif possibility.game_state[1][0] == possibility.game_state[1][1] and possibility.game_state[1][2] == possibility.game_state[1][1] and possibility.game_state[1][1] != None:
              possible_moves.append(possibility)
              continue
            #third row
            elif possibility.game_state[2][0] == possibility.game_state[2][1] and possibility.game_state[2][2] == possibility.game_state[2][1] and possibility.game_state[2][1] != None:
              possible_moves.append(possibility)
              continue
            #column 1
            elif possibility.game_state[0][0] == possibility.game_state[1][0] and possibility.game_state[2][0] == possibility.game_state[1][0] and possibility.game_state[2][0] != None:
              possible_moves.append(possibility)
              continue
            #column 2
            elif possibility.game_state[0][1] == possibility.game_state[1][1] and possibility.game_state[2][1] == possibility.game_state[1][1] and possibility.game_state[2][1] != None:
              possible_moves.append(possibility)
              continue
            #column 3
            elif possibility.game_state[0][2] == possibility.game_state[1][2] and possibility.game_state[2][2] == possibility.game_state[1][2] and possibility.game_state[2][2] != None:
              possible_moves.append(possibility)
              continue
            possibility.possible_moves = self.next_possible_moves(possibility.game_state, 'O', level + 1)
            possible_moves.append(possibility)
          else:
            possibility[row][column] = 'O'
            print('Good Move ')
            print(possibility[0])
            print(possibility[1])
            print(possibility[2])
            possibility = Node(possibility)
            possibility.turn = 'X'
            if possibility.game_state[0][0] == possibility.game_state[1][1] and possibility.game_state[2][2] == possibility.game_state[1][1] and possibility.game_state[1][1] != None :
              possible_moves.append(possibility)
              continue 
            #diagnol /
            elif possibility.game_state[2][0] == possibility.game_state[1][1] and possibility.game_state[0][2] == possibility.game_state[1][1] and possibility.game_state[1][1] != None:
              possible_moves.append(possibility)
              continue 
            #first row
            elif possibility.game_state[0][0] == possibility.game_state[0][1] and possibility.game_state[0][2] == possibility.game_state[0][1] and possibility.game_state[0][1] != None:
              possible_moves.append(possibility)
              continue
            #second row
            elif possibility.game_state[1][0] == possibility.game_state[1][1] and possibility.game_state[1][2] == possibility.game_state[1][1] and possibility.game_state[1][1] != None:
              possible_moves.append(possibility)
              continue
            #third row
            elif possibility.game_state[2][0] == possibility.game_state[2][1] and possibility.game_state[2][2] == possibility.game_state[2][1] and possibility.game_state[2][1] != None:
              possible_moves.append(possibility)
              continue
            #column 1
            elif possibility.game_state[0][0] == possibility.game_state[1][0] and possibility.game_state[2][0] == possibility.game_state[1][0] and possibility.game_state[2][0] != None:
              possible_moves.append(possibility)
              continue
            #column 2
            elif possibility.game_state[0][1] == possibility.game_state[1][1] and possibility.game_state[2][1] == possibility.game_state[1][1] and possibility.game_state[2][1] != None:
              possible_moves.append(possibility)
              continue
            #column 3
            elif possibility.game_state[0][2] == possibility.game_state[1][2] and possibility.game_state[2][2] == possibility.game_state[1][2] and possibility.game_state[2][2] != None:
              possible_moves.append(possibility)
              continue
            possibility.possible_moves = self.next_possible_moves(possibility.game_state, 'X', level +1)
            possible_moves.append(possibility)
          print(possibility.game_state)
    return possible_moves

tic_tac_toe = Tic_Tac_Toe()
tic_tac_toe.game()

print('over',tic_tac_toe.game_start.possible_moves )
for move in tic_tac_toe.game_start.possible_moves:
  print(move.game_state)



