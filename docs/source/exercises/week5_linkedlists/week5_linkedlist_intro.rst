Linked List Families!
=====================

What is a node again? Let's see!


.. code-block:: python
    :linenos:
    
    class Node:
        def __init__(self, content):
            self.content = content
            self.next = None
        
        def set_next(self, next_node):
            self.next = next_node
            
        def get_next(self):
            return self.next
            
            
Your first job is to rewrite this class using different names!

1. The class should be renamed to "Person"
2. the internal variable :code:`content` should be renamed to 
:code:`name`
3. rename :code:`set_next` to be :code:`set_next_person`.
4. inside :code:`set_next`, the variable :code:`next_node` should be renamed to
:code:`next_person`

We are going to use this class to represent the Jetsons standing in line!
It should pass the following test:


.. code-block:: python
    :linenos:
    
    george = Person("George Jetson")
    jane = Person("Jane Jetson")
    judy = Person("Judy Jetson")
    
    george.set_next_person(jane)
    jane.set_next_person(judy)
    
What would happen if we did the following?

.. code-block:: python
    :linenos:
    
    elroy = Person("Elroy Jetson")
    jane.set_next_person(elroy)
    
    
When you have finished the code above and can answer this question, 
:doc:`click here <week5_linkedlist2>` to go to the next page.  The answer is there, so don't peak!
    

    
