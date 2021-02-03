import sys
sys.path.append('src')
from tree import Tree

#basic tree class
'''
edges = [('a','c'), ('e','g'), ('e','i'), ('e','a'), ('g','b'), ('a','d'), ('d','f'), ('f','h'), ('d','j'), ('c','k')]
tree = Tree(edges)
tree.build_from_edges()

assert tree.root.value == 'e'

assert [node.value for node in tree.root.children] == ['g', 'i', 'a']

assert [node.value for node in tree.root.children[0].children] == ['b']


assert [node.value for node in tree.root.children[1].children] == []

assert [node.value for node in tree.root.children[2].children] == ['c', 'd']

assert [node.value for node in tree.root.children[2].children[0].children] == ['k']

assert [node.value for node in tree.root.children[2].children[1].children] == ['f', 'j']

assert [node.value for node in tree.root.children[0].children[0].children] == []

assert [node.value for node in tree.root.children[2].children[0].children[0].children] == []

assert [node.value for node in tree.root.children[2].children[1].children[1].children] == []

assert [node.value for node in tree.root.children[2].children[1].children[0].children] == ['h']

assert [node.value for node in tree.root.children[2].children[1].children[0].children[0].children] == []


edges = [('a','c'), ('e','g'), ('e','i'), ('e','a'), ('d','b'), ('a','d'), ('d','f'), ('f','h'), ('d','j'), ('d','k')]
tree = Tree(edges)
tree.build_from_edges()

nodes = tree.nodes_breadth_first()
print([node.value for node in nodes])

nodes = tree.nodes_depth_first()
print([node.value for node in nodes])
'''

node_values = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k']

edges = [('a','c'), ('e','g'), ('e','i'), ('e','a'), ('d','b'), ('a','d'), ('d','f'), ('f','h'), ('d','j'), ('d','k')]

tree = Tree(edges, node_values)
tree.build_from_edges()

assert tree.root.value == 'e'
assert tree.root.index == 4


children = set(tree.root.children)
grandchildren = set([])
for child in children:
        grandchildren = grandchildren.union(set(child.children))

great_grandchildren = set([])
for grandchild in grandchildren:
        great_grandchildren = great_grandchildren.union(set(grandchild.children))

great_great_grandchildren = set([])
for great_grandchild in great_grandchildren:
        great_great_grandchildren = great_great_grandchildren.union(set(great_grandchild.children))

assert {node.index for node in children} == {0, 8, 6}

assert {node.value for node in children} == {'a', 'i', 'g'}

assert {node.index for node in grandchildren} == {2, 3}

assert {node.value for node in grandchildren} == {'c', 'd'}

assert {node.index for node in great_grandchildren} == {1, 9, 5, 10}

assert {node.value for node in great_grandchildren} == {'b', 'j', 'f', 'k'}

assert {node.index for node in great_great_grandchildren} == {7}

assert {node.value for node in great_great_grandchildren} == {'h'}