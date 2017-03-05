Trees, Part 1
==============

Today, we are going to be covering trees.

Let's look at a basic tree:

.. code-block:: python
    :linenos:
    
    class Tree:
        def __init__(self, value, left=None, right=None):
            self.left = left
            self.right = right
            self.value = value
        
    carl = Tree("Carl")
    jane = Tree("Jane")
    delip = Tree("Delip")
    
    carl.left = jane
    carl.right = delip


We can picture this as a family tree. Delip and Jane are Carl's parents. 

We can also picture this as how we think about information:

.. code-block:: python
    :linenos:
    
    class Tree:
        def __init__(self, value, left=None, right=None):
            self.left = left
            self.right = right
            self.value = value
        
    main_task = Tree("get a new computer")
    subtask1 = Tree("get a job")
    subtask2 = Tree("pick a good computer")
    main_task.left = subtask1
    main_task.right = subtask2
    