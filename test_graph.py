import sys
sys.path.append('src')
from graph import Graph
edges = [(0,1),(1,2),(1,3),(3,4),(1,4),(4,5)]
graph = Graph(edges)
graph.build_from_edges()
print(graph.list[0].neighbors)

bf = graph.get_nodes_breadth_first(2)
print([node.value for node in bf])
[2, 1, 0, 3, 4, 5]