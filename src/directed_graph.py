

class Node():
  def __init__(self, index):
    self.children = None
    self.parents = None
    self.index = index

class DirectedGraph():
  def __init__(self, edges):
    self.edges = edges
    self.root = Node(0)
    max_index = 0
    for index in edges:
      for value in index:
        if value > max_index:
          max_index = value
    self.nodes = [_ for _ in range(max_index+1)]
  
  def get_parents(self, index_value): 
    parents = []
    for index in range(len(self.edges)):
      if self.edges[index][1] == index_value:
        parents.append(self.edges[index][0])
    return parents

  def get_children(self, index_value):#gets children of index from list of edges
    children = []
    for index in range(len(self.edges)):

      if self.edges[index][0] == index_value:
        children.append(self.edges[index][1])
    return children

  def build_from_edges(self):
    node_array = [self.root]
    for index in range(len(self.nodes)):
      index_value = int(index)
      self.nodes[index] = Node(index_value)
      index_node_children = self.get_children(index)
      self.nodes[index].children = []
      for child in index_node_children:
        child = Node(child)
        self.nodes[index].children.append(child)
      self.nodes[index].parents = [Node(index) for index in self.get_parents(index)]
  
  def nodes_breadth_first(self,value):
    queue = [self.root.index]
    visited = []
    while len(queue) > 0 :
      node = Node(queue[0])
      visited.append(node)
      node.children = get_children(node.index, self.edges)
      for child in node.children:
        queue.append(child)
      queue.remove(node.index)
    return visited

  def nodes_depth_first(self):
    queue = [self.root.index]
    visited = []
    while len(queue) > 0 :
      node = Node(queue[0])
      visited.append(node)
      node.children = get_children(node.index, self.edges)
      for child in node.children:
        queue.insert(0,child)
      queue.remove(node.index)
    return visited


