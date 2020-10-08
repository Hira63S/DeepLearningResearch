"""
Doubly Linked List class
"""

class List:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None
class DoublyLinkedList:
    def __init__(self):
        self.head = None
    
    def append_to_front(self, data):
        new_node = Node(data)
        if self.head == None:
            self.head = new_node
            new_node.prev = None
        else:
            current = self.head
            while current:
                current = current.next
            current.next = new_node
            new_node.prev = current
            new_node.next = None
            
            
dllist = DoublyLinkedList()
dllist.append_to_front(1)
dllist.append_to_front(29)
print(dllist)
