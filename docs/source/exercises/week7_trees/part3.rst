Trees, Part 3
=============

.. code-block:: python
    :linenos:
    
    
    .. code-block:: python
    :linenos:
    
    class Tree:
        def __init__(self, value):
            self.left = None
            self.right = None
            self.value = value
            
        def add_tree(self, child):
            if self.right == None:
                self.right = child
            else:
                self.right.add_tree(child)
        
        def add_value(self, value):
            child = Tree(value)
            self.add_tree(child)
            
        def is_in(self, value):
            if self.value == value:
                return True
            if self.right != None:
                if self.right.is_in(value):
                    return True
            if self.left != None:
                if self.left.is_in(value);
                    return True
                    
    top = Tree("A")
    top.add_value("B")
    top.add_value("C")
    top.add_value("D")
    top.add_value("E")

    
    
    