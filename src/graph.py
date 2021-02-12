

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
    self.value = value
    self.neighbors = None
    self.index = None

class Graph():
  def __init__(self, edges):
    self.edges = edges
    self.list = [_ for _ in range(len(self.edges))]

  def build_from_edges(self):
    for index in range(len(self.edges)):
      index_value = Node(index)
      index_value.neighbors = get_neighbors(index_value.value, self.edges)
      self.list[index] = index_value


  def get_nodes_breadth_first(self, root):
    queue = [root]
    visited = []
    while len(queue)>0:
      value = self.list[queue[0]]
      visited.append(value)
      queue.pop(0)
      for neighbor in value.neighbors:
        if neighbor not in [node.value for node in visited] and neighbor not in queue:
          queue.append(neighbor)
    return visited

      
    