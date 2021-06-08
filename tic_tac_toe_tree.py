
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
    if current_state[0][0] == current_state[1][1] and current_state[2][2] == current_state[1][1] and current_state[1][1] != None :
          return None 
        #diagnol /
    elif current_state[2][0] == current_state[1][1] and current_state[0][2] == current_state[1][1] and current_state[1][1] != None:
          return None 
        #first row
    elif current_state[0][0] == current_state[0][1] and current_state[0][2] == current_state[0][1] and current_state[0][1] != None:
          return None
        #second row
    elif current_state[1][0] == current_state[1][1] and current_state[1][2] == current_state[1][1] and current_state[1][1] != None:
          return None
        #third row
    elif current_state[2][0] == current_state[2][1] and current_state[2][2] == current_state[2][1] and current_state[2][1] != None:
          return None
        #column 1
    elif current_state[0][0] == current_state[1][0] and current_state[2][0] == current_state[1][0] and current_state[2][0] != None:
          return None
        #column 2
    elif current_state[0][1] == current_state[1][1] and current_state[2][1] == current_state[1][1] and current_state[2][1] != None:
          return None
        #column 3
    elif current_state[0][2] == current_state[1][2] and current_state[2][2] == current_state[1][2] and current_state[2][2] != None:
          return None
    print('Level ', level)
    possible_moves = []
    for row in range(3):
      for column in range(3):
        print('current_state')
        print(current_state[0])
        print(current_state[1])
        print(current_state[2])
        possibility = list(current_state)
        print('row', row)
        print('column', column)
        print('turn', turn)
        print(possibility[0])
        print(possibility[1])
        print(possibility[2])
        print('')

        if possibility[0][0] == possibility[1][1] and possibility[2][2] == possibility[1][1] and possibility[1][1] != None :
          continue 
        #diagnol /
        elif possibility[2][0] == possibility[1][1] and possibility[0][2] == possibility[1][1] and possibility[1][1] != None:
          continue 
        #first row
        elif possibility[0][0] == possibility[0][1] and possibility[0][2] == possibility[0][1] and possibility[0][1] != None:
          continue
        #second row
        elif possibility[1][0] == possibility[1][1] and possibility[1][2] == possibility[1][1] and possibility[1][1] != None:
          continue
        #third row
        elif possibility[2][0] == possibility[2][1] and possibility[2][2] == possibility[2][1] and possibility[2][1] != None:
          continue
        #column 1
        elif possibility[0][0] == possibility[1][0] and possibility[2][0] == possibility[1][0] and possibility[2][0] != None:
          continue
        #column 2
        elif possibility[0][1] == possibility[1][1] and possibility[2][1] == possibility[1][1] and possibility[2][1] != None:
          continue
        #column 3
        elif possibility[0][2] == possibility[1][2] and possibility[2][2] == possibility[1][2] and possibility[2][2] != None:
          continue
        
        if current_state[row][column] == None:
          
          if turn == 'X':
            no_more = False
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
              no_more = True
              print('diagnol /')
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
            if no_more == True:
              print('no more')
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



