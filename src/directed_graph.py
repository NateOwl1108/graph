

class Node():
  def __init__(self, index):
    self.children = None
    self.parents = None
    self.previous = None
    self.next = None
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
    self.nodes_depth_first_list = []
  
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

    visited = []
    order_list = [[child for child in node.children] for node in self.nodes]

    for index in range(len(order_list)):
      for node in range(len(order_list[index])):
        if order_list[index][node].index == value:
          visited.append(order_list[index][node])
          del order_list[index][node]
    alternate = False
    minus = 0
    by_root= False
    while len(order_list) > 0 :
      
      if alternate == False:
        for node in order_list[value - minus]:
          if node.index not in [a_value.index for a_value in visited]:
            visited.append(node)
        del order_list[value - minus]
        if by_root == False:
          alternate = True
      else:
        if minus == value -1:
          by_root = True
        minus += 1
        for node in order_list[value - minus]:
          if node.index not in [a_value.index for a_value in visited]:
            visited.append(node)
        del order_list[value - minus]
        order_list_index = int(value - minus)
        if order_list_index >= len(order_list):
          alternate = True
        else:
          alternate = False
     
    return visited

  def find_next(self, index):
    order_list = [[child for child in node.children] for node in self.nodes]
    
    next_nodes = order_list[index.index]

    return next_nodes
      


  def nodes_depth_first(self,index_value):
    depth_queue = []
    depth_list = []
    order_list = [[child for child in node.children] for node in self.nodes]
    for index in range(len(order_list)):
      for node in range(len(order_list[index])):
        if order_list[index][node].index == index_value:
          depth_queue.append(order_list[index][node])
          del order_list[index][node]
    while len(depth_list)< len(order_list) - 1:  
        depth_list.append(depth_queue[0])
        for node in self.find_next(depth_queue[0]):
          if node.index not in [value.index for value in depth_list]:
            depth_queue.insert(1, node)
        del depth_queue[0]
      
    return depth_list
  


  def calc_distance(self, node_1 , node_2):

    children_list = [self.nodes[node_1]]
    iterations = 0
    if node_1 == node_2:
      return 0
    while node_2 not in [node.index for node in children_list]:
        iterations += 1
        new_children = []
        for value in children_list:
          value = self.nodes[value.index]
          if value.children is None:
            continue
          for child in value.children:
            new_children.append(child)
        children_list = new_children 
        if len(children_list) == 0:
          return False
        if iterations == 5:
          break
    return iterations

  def previous(self, node_1, node_2):
    node_list = [self.nodes[node_1]]
    iterations = 0
    children_list = [self.nodes[node_1]]
    if node_1 == node_2:
      return node_list
    while node_2 not in [node.index for node in children_list]:
        iterations += 1
        new_children = []
        for value in children_list:
          value = self.nodes[value.index]
          if value.children is None:
            continue
          for child in value.children:
            child = self.nodes[child.index]
            child.previous = self.nodes[value.index]
            
            node_list.append(child)
            new_children.append(child)
        children_list = new_children 
        if len(children_list) == 0:
          return False
        if iterations == 5:
          break
    return node_list

  def calc_shortest_path(self, node_1, node_2):
    num_children = self.calc_distance(node_1,node_2)
    node_list = self.previous(node_1,node_2)


    if num_children == False:
      return False
    

    current_node = self.nodes[node_2]
    shortest_path = [current_node.index]
    iterations = 0
    while current_node.index != node_1:
      for value in node_list:
        if value.index == current_node.index:
          
          current_node = self.nodes[value.previous.index]
          break
      shortest_path.append(current_node.index)
      iterations += 1
      if iterations == 100:
        break
    
    return shortest_path[::-1]
      

        



    



