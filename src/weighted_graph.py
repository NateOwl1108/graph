

class Node():
  def __init__(self, index):
    self.index = index
    self.value = None
    self.neighbors = []
    self.previous = None
    self.d= 99999999

class WeightedGraph():
  def __init__(self, weights, vertex_values):
    self.weights = weights
    self.edges = [edge for edge in self.weights]
    self.vertex_values = vertex_values
    self.max_index = self.get_max_index()
    self.nodes = [Node(i) for i in range(self.max_index+1)]

    self.build_from_edges()

  
  def get_neighbors(self, index):
    neighbors = []
    for edge in self.edges:
      if edge[0] == index:
        neighbors.append(edge[1])
      elif edge[1] == index:
        neighbors.append(edge[0])
    return neighbors

  def get_max_index(self):
    max = self.edges[0][0]
    for edge in self.edges:
      if edge[0] > max:
        max = edge[0]
      elif edge[1] > max:
        max = edge[1]
    return max

  def build_from_edges(self):
    for node in self.nodes:
      neighbors = [self.nodes[i] for i in self.get_neighbors(node.index)]
      node.neighbors = neighbors
      for neighbor in neighbors:
        if node not in neighbor.neighbors:
          neighbor.neighbors.append(node)
     

  def get_nodes_breadth_first(self, initial_node):
    queue = [self.nodes[initial_node]]
    visited = []
    while queue != []:
      current = queue[0]
      queue = queue.pop(0)
      visited.append(current)
      neighbors = current.neighbors
      for neighbor in neighbors:
         if neighbor not in queue and neighbor not in visited:
           queue.append(neighbor)

  def get_nodes_depth_first(self, initial_node):
    queue = [self.nodes[initial_node]]
    visited = []
    while queue != []:
      current = queue[0]
      queue =  queue.pop(0)
      visited.append(current)
      neighbors = current.neighbors
      new_values = []
      for neighbor in neighbors:
         if neighbor not in queue and neighbor not in visited:
           new_values.append(neighbor)
      queue = [new_values] + queue
    return visited


  def set_breadth_first_distance_and_previous(self, starting_node_index): 
    self.build_from_edges()
    self.nodes[starting_node_index].d = 0
    queue = [self.nodes[starting_node_index]]
    visited = []
    while len(queue) != 0:
      current = queue[0]
      current_dist = current.d
      for node in queue:
        if node.d < current_dist:
          current = node
          current_dist = node.d
      queue = [node for node in queue if node != current]
      visited.append(current)
      neighbors = current.neighbors
      for neighbor in neighbors:
        edge = (current.index, neighbor.index) if (current.index, neighbor.index) in self.edges else (neighbor.index, current.index)
        weight = self.weights[edge]
        if neighbor not in visited and current_dist + weight < neighbor.d:
          neighbor.d = current_dist + weight

      for neighbor in neighbors:
         if neighbor not in queue and neighbor not in visited:
            queue.append(neighbor)
    
  def calc_distance(self, starting_node_index, ending_node_index):
    self.set_breadth_first_distance_and_previous(starting_node_index)
    return self.nodes[ending_node_index].d
    

  #def calc_shortest_path(self, starting_node_index, ending_node_index):
     