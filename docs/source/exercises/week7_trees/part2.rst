Trees, Part 2
=============

.. code-block:: python
    :linenos:
    
    
    .. code-block:: python
    :linenos:
    
    class Tree:
        def __init__(self, value, children=None):
            if children == None:
                children = []
            self.children = children
            self.value = value
            
        def add_tree(self, child):
            self.children.append(child)
        
        def add_value(self, value):
            child = Tree(value)
            self.children.append(child)
            
        def is_in(self, value):
            if self.value == value:
                return True
            for child in self.children:
                if child.is_in(value):
                    return True
            return False

    
    top = Tree("A")
    top.add_value("B")
    top.add_value("C")
    top.add_value("D")
    top.add_value("E")

    
    
    