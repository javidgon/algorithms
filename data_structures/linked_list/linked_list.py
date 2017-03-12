class LinkedList(object):
    head = None
    
    def __init__(self, head=None):
        self.head = head
    
    def append(self, d):
        if not self.head:
            self.head = Node(d)
        else:
            self.head.append(d)
    
    def length(self):
        node = self.head
        i = 0
        while True:
            if not node:
                return i
            else:
                node = node.next
                i += 1

class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None
    
    def append(self, d):
        if not self.next:
            self.next = Node(d)
        else:
            self.next.append(d)


ll = LinkedList()
ll.append(2)
ll.append(3)
ll.append(4)
ll.append(5)
ll.append(5)

print(ll.length())
        
    