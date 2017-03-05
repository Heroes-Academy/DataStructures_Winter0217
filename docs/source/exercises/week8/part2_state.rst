State
=====

The choices that go into representing a state should cover the possible 
the possible variables that change. 

Note: we are going to use classes in our representations. It makes things
easier to think about and is easy to read.

Below is a class for representing the state. 
It is also going to be a node in a tree, where each child is
the next possible move and each parent is the previous move. 

.. code-block:: python
    :linenos:
    
    class MCState:
        ### MC is missionaries and cannibals
        def __init__(self, state_vars, num_moves=0, parent=None):
            self.state_vars = state_vars
            self.num_moves = num_moves
            self.parent = parent

    root_state = MCState("what should go here")
    
    
What is a set of variables that could go there?  What do we need to pay attention
to? What is important information?



Using Class Methods
-------------------

In python's classes, it's useful to have functions which produce systematically
expected states. For example, in this case, we want a root state! 
Below is functionally the exact same as above, but instead the logic
for constructing the root state now belongs **inside** the state. 

.. code-block:: python
    :linenos:
    
    class MCState:
        ### MC is missionaries and cannibals
        def __init__(self, state_vars, num_moves=0, parent=None):
            self.state_vars = state_vars
            self.num_moves = num_moves
            self.parent = parent
            
        @classmethod
        def root(cls):
            cls("what should go here")

    root_state = MCState.root()