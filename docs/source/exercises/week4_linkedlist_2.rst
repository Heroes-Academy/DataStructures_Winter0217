[Week 4 Exercises] Linked Lists, part 2

You should have completed the intro and part 1 portions before this one. 

You have now written a linked list using the :code:`Node` class.
Also, you have written tests to make sure it works. 

Now, we will look at how to write the managing class for the linked list.

Break into pairs to do this part. 

The Linked List Class
----------------------

.. code-block:: python
    :linenos:

    class LinkedList:
        def __init__(self):
            self.top_node = None
        
        def add(self, content):
            new_node = Node(content)
            if self.top_node == None:
                ### place holder
            else:
                ### place holder
                

    groceries = LinkedList()
    
    groceries.add('potatoes')
    groceries.add('strawberries')
    
    
This linked list class needs to be adding items into it.  What should it be doing in the
add function?  

1. First, solve what happens in the :code:`if`.
2. Then, think about how you would solve the :code:`else` portion. 

**We will wait until all groups have come to here.**

If you finish it early, though, think about how you would do the following functions:

.. code-block:: python
    :linenos:

    class LinkedList:
        def __init__(self):
            self.top_node = None
        
        def delete(self, content):
            ''' delete any node that has this content '''
        
        def search(self, content):
            ''' return any node or nodes that match this content 
                we can sometimes assume all contents are unique, so if you find it once,
                you can stop searching
            '''            
            
        def max(self):
            ''' return the max item '''
            
        def min(self):
            ''' return the min item '''
        
        def insert_sorted(self, content):
            ''' if you wanted to keep the list sorted, how would you add this in? '''
            