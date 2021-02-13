
class Node():
  def __init__(self, value):
    self.neighbors = None
    self.index = value

class Graph():
  def __init__(self, edges):
    self.edges = edges
    self.node_list = [_ for _ in range(len(self.edges))]

  def get_neighbors(self, value):
    copy_list = list(self.edges)
    neighbor_list = []
    for neighbors in copy_list:
      if value in neighbors:
        for point in neighbors:
          if point!= value:
            neighbor_list.append(point)
    return neighbor_list

  def build_from_edges(self):
    for index in range(len(self.edges)):
      index_value = Node(index)
      index_value.neighbors = self.get_neighbors(index_value.index)
      self.node_list[index] = index_value
      
  def get_nodes_breadth_first(self, root):
    queue = [root]
    visited = []
    while len(queue)>0:
      value = self.node_list[queue[0]]
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
      value = self.node_list[queue[0]]
      visited.append(value)
      queue.pop(0)
      for neighbor in value.neighbors:
        if neighbor not in [node.index for node in visited] and neighbor not in queue:
          queue.insert(0,neighbor)
    return visited

      
    