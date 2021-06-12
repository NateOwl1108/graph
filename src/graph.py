

class Node():
  def __init__(self, current_node):
    self.neighbors = None
    self.index = current_node
    self.d = None
    self.previous = None


class Graph():
  def __init__(self, edges):
    self.edges = edges
    self.max_index = self.get_max_index()
    self.node_list = [_ for _ in range(self.max_index+1)]
    
    

  def get_neighbors(self, current_node):
    neighbor_list = []
    for neighbors in self.edges:
      if neighbors[0] == current_node.index:
        neighbor_list.append(self.node_list[neighbors[1]])
      elif neighbors[1] == current_node.index:
        neighbor_list.append(self.node_list[neighbors[0]])
    return neighbor_list

  def get_max_index(self):
    max_index = 0
    for edge in self.edges:
      if edge[0]> max_index:
        max_index = edge[0]
      elif edge[1] > max_index:
        max_index = edge[1]
    return max_index



  def build_from_edges(self):
    for index in range(len(self.node_list)):
      current_node = Node(index)

      self.node_list[index] = current_node
    for node in self.node_list:
      self.node_list[node.index].neighbors = self.get_neighbors(node)



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
    self.build_from_edges()
    self.node_list[starting_node_index].distance = 0
    queue = [self.node_list[starting_node_index]]
    visited = []
    while queue != []:
      visiting = queue[0]
      current_dist = visiting.distance
      queue = queue[1:]
      visited.append(visiting)
      neighbors = visiting.neighbors
      for neighbor in neighbors:
        if neighbor not in queue and neighbor not in visited:
          neighbor.distance = current_dist + 1
          neighbor.previous = visiting

      queue = queue + [neighbor 
                       for neighbor in neighbors 
                       if neighbor not in queue and neighbor not in visited]


  def calc_shortest_path(self, starting_node_index, ending_node_index):
    self.set_breadth_first_distance_and_previous(starting_node_index)
    
    current_node = self.node_list[ending_node_index]
    path_list = [ending_node_index]
    while current_node.index != starting_node_index:
      current_node = current_node.previous
      path_list.append(current_node.index)
    return path_list[::-1]