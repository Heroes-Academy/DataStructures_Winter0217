[Week 4 Exercises] Linked Lists, part 1

You should have completed the introduction portion already. If not, go back and do that!

Your First Linked List
----------------------

We will be writing a linked list class.  
The class is going to represent the box you were drawing.
However, we are going to call the boxes "nodes". This is a common computer science term. 

.. code-block:: python
    :linenos:
    
    class Node:
        def __init__(self, content):
            self.content = content
            self.next = None
        
        def set_next(self, next_node):
            self.next = next_node
            
Using this code, write a test which will create the linked list you made on paper. 

You can test the code by doing the following:

.. code-block:: python
    :linenos:
    
    if __name__ == "__main__":
        ### create your linked list using nodes here
        ### i'm going to call the first item as "top_node"
        
        assert top_node.content == "the thing you expect it to be"
        
        top_node = top_node.next
        assert top_node.content == "the thing you expect the second thing to be"
        
        ## and so on until the last one, when there is no more, should be None 
        ## this is because we set the `next` variable to be None in the __init__ of Node
        
        top_node = top_node.next
        assert top_node.content == None
        
        
        