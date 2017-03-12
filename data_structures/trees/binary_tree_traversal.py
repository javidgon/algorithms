class Node(object):
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

leaf_left = Node(4)
leaf_right = Node(8)

root = Node(3, leaf_left, leaf_right)
        

def in_order_traversal(node):
    if node:
        in_order_traversal(node.left)
        print(node.value)
        in_order_traversal(node.right)

def pre_order_traversal(node):
    if node:
        print(node.value)
        in_order_traversal(node.left)
        in_order_traversal(node.right)

def post_order_traversal(node):
    if node:
        in_order_traversal(node.left)
        in_order_traversal(node.right)
        print(node.value)

print('In-order-traversal')
in_order_traversal(root)
print('Pre-order-traversal')
pre_order_traversal(root)
print('Post-order-traversal')
post_order_traversal(root)