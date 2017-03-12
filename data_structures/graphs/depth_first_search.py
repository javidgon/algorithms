class Graph(object):
    nodes = None

class Node(object):
    def __init__(self, name, children):
        self.name = name
        self.children = children
        self.visited = False

a = Node('A', [])
e = Node('E', [a])
c = Node('C', [a, e])
d = Node('D', [e, c])
b = Node('B', [a])

def depth_first_search(node):
    if not node:
        return
    print(node.name)
    node.visited = True
    for child in node.children:
        if not child.visited:
            depth_first_search(child)

depth_first_search(d)
