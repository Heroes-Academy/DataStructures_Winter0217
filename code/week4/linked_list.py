"""
Use the classes below to make a Linked List

I've provided the skeleton, you have to fill in the details

You can use the slide and ask me questions.

You can also use the internet, but I would warn against just copying code.
You won't learn much that way.
"""

class LinkedList:
    """Basic Linked List class

    Functions:
        insert: add an value onto the list
        delete: delete a value from the list
        search: return the value if it's in the list
    """
    def __init__(self):
        self.root = None

    def insert(self, value):
        """ inserts value into the list

        Args:
            value: any variable type

        Procedure:
            Use the value to create a new node.
            If root is None, set root to equal the new node
            If root is not None, have root insert it into its child
        """
        new_node = Node(value)
        if self.root is None:
            self.root = new_node
        else:
            self.root.insert(new_node)

    def delete(self, value):
        """Handles the delete function for the linked list

        Args:
            value: a value which should be deleted

        Procedure:
            check if the root node is equal to the value
            if it is, remove it and set its next to be the new root
            if it isn't, call the delete function from root
        """
        pass

    def search(self, value):
        """searches for the value in the list

        Args:
            value: a value which should equal a node in the list

        Procedure:
            call the root's search procedure
            return whatever it returns
        """
        pass


class Node:
    """Basic Node class

    Functions:
        __init__ constructor: when created, a Node wraps a value
        insert: add new node to next or pass it on
    """
    def __init__(self, value):
        self.next = None
        self.value = value

    def insert(self, new_node):
        """inserts the new node into the list

        Args:
            new_node: a Node instance

        Procedure:
            if the node's next is None, set None to new_node
            else, call insert on the next node
        """
        pass

    def delete(self, value):
        """deletes a Node from the linked list

        Args:
            value: a value which should equal a value in the list

        Procedure:
            Check if next's value is equal to this value
            If it is, then bypass it by setting this next to the next's next
            If it isn't, then call next's delete
        """
        pass

    def search(self, value):
        """searches for the value in the list

        Args:
            value: a value which should equal a value in the list

        Procedure:
            Check if the value is equal to the node's value
            If it is, return True
            If it isn't, called the child and return its result
        """
        pass

def test():
    mylist = LinkedList()
    mylist.insert(5)
    mylist.insert("potato")
    mylist.insert("bunnies")
    assert mylist.search("potato") == True

    mylist.delete(5)
    assert mylist.search(5) == False
    assert mylist.search("bunnies") == False



if __name__ == "__main__":
    test()
