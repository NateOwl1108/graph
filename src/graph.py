
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
  def get_nodes_breadth_first(self, root):
      root = Node(root)
      root.index = 0
      index = 0
      node_array = [root]
      neighbors_array = []
      visited = []
      non_repeating = True
      while non_repeating == True:
        non_repeating = False
        for point in node_array:
          print('point')
          print(point)
          if point not in [node.value for node in visited] :
            non_repeating = True
            node_array_index = node_array.index(point)
            node_array[index].neighbors = get_neighbors(point.value, self.edges)
            for neighbor in range(len(node_array[index].neighbors)):
              node_array[index].neighbors[index] = Node(node_array[index].neighbors[index])

              node_array[index].neighbors[index].index = index
              node_array.append(node_array[index].neighbors[index])
          visited.append(node_array[index])
        node_array = neighbors_array
      
    