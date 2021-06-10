
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
class Node():
  def __init__(self, current_node):
    self.neighbors = None
    self.index = current_node
    self.distance = None
    self.previous = None
=======
=======
>>>>>>> origin/master
=======
>>>>>>> origin/master

def get_neighbors(value, edges_list):
  copy_list = list(edges_list)
  neighbor_list = []
  for neighbors in copy_list:
    if value in neighbors:
      for point in neighbors:
        if point!= value:
          neighbor_list.append(point)
  return neighbor_list

class Node():
  def __init__(self, value):
    self.neighbors = None
    self.index = value
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> origin/master
=======
>>>>>>> origin/master
=======
>>>>>>> origin/master

class Graph():
  def __init__(self, edges):
    self.edges = edges
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
    self.node_list = [_ for _ in range(len(self.edges))]

  def get_neighbors(self, current_node):
    copy_list = list(self.edges)
    neighbor_list = []
    for neighbors in copy_list:
      if current_node in neighbors:
        for point in neighbors:
          if point!= current_node:
            neighbor_list.append(point)
    return neighbor_list

  def build_from_edges(self):
    for index in range(len(self.edges)):
      index_current_node = Node(index)
      index_current_node.neighbors = self.get_neighbors(index_current_node.index)
      self.node_list[index] = index_current_node
=======
=======
>>>>>>> origin/master
=======
>>>>>>> origin/master
    self.list = [_ for _ in range(len(self.edges))]

  def build_from_edges(self):
    for index in range(len(self.edges)):
      index_value = Node(index)
      index_value.neighbors = get_neighbors(index_value.index, self.edges)
      self.list[index] = index_value


  def get_nodes_breadth_first(self, root):
    queue = [root]
    visited = []
    while len(queue)>0:
      value = self.list[queue[0]]
      visited.append(value)
      queue.pop(0)
      for neighbor in value.neighbors:
        if neighbor not in [node.index for node in visited] and neighbor not in queue:
          queue.append(neighbor)
    return visited

  def get_nodes_depth_first(self, root):
    queue = [root]
    visited = []
    while len(queue)>0:
      value = self.list[queue[0]]
      visited.append(value)
      queue.pop(0)
      for neighbor in value.neighbors:
        if neighbor not in [node.index for node in visited] and neighbor not in queue:
          queue.insert(0,neighbor)
    return visited

<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> origin/master
=======
>>>>>>> origin/master
=======
>>>>>>> origin/master
      
  def get_nodes_breadth_first(self, root):
    queue = [root]
    visited = []
    while len(queue)>0:
      current_node = self.node_list[queue[0]]
      visited.append(current_node)
      queue.pop(0)
      for neighbor in current_node.neighbors:
        if neighbor not in [node.index for node in visited] and neighbor not in queue:
          queue.append(neighbor)
    return visited
  
  def get_nodes_depth_first(self, root):
    queue = [root]
    visited = []
    while len(queue)>0:
      current_node = self.node_list[queue[0]]
      visited.append(current_node)
      queue.pop(0)
      for neighbor in current_node.neighbors:
        if neighbor not in [node.index for node in visited] and neighbor not in queue:
          queue.insert(0,neighbor)
    return visited
  
  def set_breadth_first_distance_and_previous(self, starting_node_index):
    first_node = Node(starting_node_index)
    first_node.distance = 0
    queue = [first_node]
    visited = []
    distance = 0
    while len(queue)>0:
      current_node = self.node_list[queue[0].index]
      current_node.distance = queue[0].distance
      current_node.previous = queue[0].previous
      visited.append(current_node)
      queue.pop(0)
      for neighbor in current_node.neighbors:
        if neighbor not in [node.index for node in visited] and neighbor not in queue and neighbor not in [node.index for node in queue]:
          neighbor = Node(neighbor)
          neighbor.distance = current_node.distance +1
          neighbor.previous = current_node
          queue.append(neighbor)
    return visited
    
  def calc_distance(self, starting_node_index, ending_node_index):
      node_list = self.set_breadth_first_distance_and_previous(starting_node_index)
      for node_index in range(len(node_list)):
        if node_list[node_index].index == ending_node_index:
          return node_list[node_index].distance


  def calc_shortest_path(self, starting_node_index, ending_node_index):
    node_list = self.set_breadth_first_distance_and_previous(starting_node_index)
    node_index_list = [node.index for node in node_list]
    index = node_index_list.index(ending_node_index)
    previous_list = [node_list[index].index]
    while previous_list[0] != starting_node_index:
      index = node_index_list.index(previous_list[0])
      previous_list.insert(0, node_list[index].previous.index)
    return previous_list