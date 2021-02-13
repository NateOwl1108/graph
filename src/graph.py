
class Node():
  def __init__(self, value):
    self.index = value
    self.neighbors = None
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
      self.node_list[index] = Node(index)
      self.node_list[index].index = index
      self.node_list[index].neighbors = self.get_neighbors(index)
    print([node.neighbors for node in self.node_list])

  def get_nodes_breadth_first(self, root):
    queue = [root]
    visited = []
    runs = 0 
    while len(queue) > 0 :
      runs += 1
      if runs == 30:
        return 0
      else:
        node = self.node_list[queue[0]]
        visited.append(node)
        neighbors = self.node_list[node.index].neighbors
        queue.pop(0)
        for neighbor in neighbors:
         if neighbor not in [node.index for node in visited]:
            queue.append(neighbor)
        
      return visited
      
  def get_nodes_depth_first(self, root):
    queue = [root]
    visited = []
    runs = 0 
    while len(queue) > 0 :
      runs += 1
      if runs == 30:
        return 0
      else:
        node = self.node_list[queue[0]]
        visited.append(node)
        neighbors = self.node_list[node.index].neighbors
        queue.pop(0)
        for neighbor in neighbors:
         if neighbor not in [node.index for node in visited]:
            queue.insert(0,neighbor)
        
      return visited
      
    
      
    