class DoubleLinkedList:
    def __init__(self, root=None):
        self.root = root
    
    def insert(self, value):
        if self.root is None:
            self.root = Node(value)
        else:
            new_node = Node(value)
            self.root.insert(new_node)
    
    def delete(self):
        pass
    
    def search(self):
        pass
    
    def sort(self):
        pass
    
class Node:
    """Basic Node class

    Functions:
        __init__ constructor: when created, a Node wraps a value
        insert: add new node to next or pass it on
    """
    def __init__(self, value, parent=None):
        self.next = None
        self.value = value
        self.parent = parent

    def insert(self, new_node):
        if self.next is None:
            new_node.parent = self
            self.next = new_node
        else:
            self.next.insert(new_node)
            
    def delete(self, value):
        if self.next is None:
            return
        elif self.next.value == value:
            self.next = self.next.next
            self.next.parent = self
        else:
            self.next.delete(value)

    def search(self, value):
        if self.value == value:
            return True
        elif self.next:
            return self.next.search(value)
        else:
            return False