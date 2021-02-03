
def remove_parenthesis(edges):
  edges_list = []
  for index in range(len(edges)):
    edge = []
    for char in edges[index]:
      if char != '(' or char != ')':
        edge.append(char)
    edges_list.append(edge)
  return edges_list

def get_children(value, edges_list):#gets children of value from list of edges
  edges_list = list(remove_parenthesis(edges_list))
  edges = []
  for index in range(len(edges_list)):
    if edges_list[index][0] == value:
      edges.append(edges_list[index][1])
  return(edges)


def get_parents(value, edges): 
  edges_list = list(remove_parenthesis(edges))
  edges = []
  for index in range(len(edges_list)):
    if edges_list[index][1] == value:
      edges.append(edges_list[index][0])
  return(edges)

def get_root(edges):
  edges_list = list(remove_parenthesis(edges))
  parents = []
  for index in range(len(edges_list)):
    parents.append(edges_list[index][0])
  for char in parents:
    if get_parents(char, edges) == []:
      return char

class Node():
  def __init__(self, value):
    self.value = value
    self.children = next
    self.index = None

class Tree():

  def __init__(self, edges, node_values):
    self.edges = edges
    self.root = Node(get_root(self.edges))
    self.root.index = node_values.index(self.root.value)
    self.node_values = node_values

  def  build_from_edges(self):
    node_array = [self.root]
    while len(node_array) > 0:
      children_array = []
      for parent in range(len(node_array)):
        node_array[parent].children = get_children(node_array[parent].value, self.edges)
        for index in range(len(node_array[parent].children)):
          node_array[parent].children[index] = Node(node_array[parent].children[index])
          node_array[parent].children[index].index = self.node_values.index(node_array[parent].children[index].value)
          children_array.append(node_array[parent].children[index])
      node_array = children_array
  
  def nodes_breadth_first(self):
    queue = [self.root.value]
    visited = []
    while len(queue) > 0 :
      node = Node(queue[0])
      visited.append(node)
      node.children = get_children(node.value, self.edges)
      for child in node.children:
        queue.append(child)
      queue.remove(node.value)
    return visited

  def nodes_depth_first(self):
    queue = [self.root.value]
    visited = []
    while len(queue) > 0 :
      node = Node(queue[0])
      visited.append(node)
      node.children = get_children(node.value, self.edges)
      for child in node.children:
        queue.insert(0,child)
      queue.remove(node.value)
    return visited


