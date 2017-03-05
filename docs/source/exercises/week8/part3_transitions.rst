Part 3: Transitions
===================

Now we have a state (this is what we made in the last part). Given a state,
we want to produce the children.  In problem solving settings like this, the set
of children are not known until you apply some rules or algorithms. 
In other words, the important question is: 
what is the logic to get the possible legal children?   Illegal children
would be things like having 3 people in the boat, etc.

We will break this down into a few parts:

1. What are and how do we represent the possible moves?
2. How can we apply a move to a state to make a new state?
3. When are states illegal and how can you tell?



Possible Moves
--------------

What are a set of possible moves that can be done at every state?

Fill in the code below to return a list of all possible next moves. 
Assuming that we represented the state in Part 2 as a tuple, each move
should also be a tuple which represents the changes in the state.
For example, one move could be to move 1 missionary across the river by themself. 
In that case, the representation part for the missionaries would change 
and so would the side the boat was on.


.. code-block:: python
    :linenos:
    
    class MCState:
        ### MC is missionaries and cannibals
        ### The init function is going to be whatever we decided from the previous part!

        
        def get_possible_moves(self):
            ## get all possible moves
            pass

    root_state = MCState.root_state()
    
    
    print(root_state.get_possible_moves())
    
    
 
Possible States
---------------

Given a function which gives us the possible moves, write a function which
returns the next states. Don't wrory about whether or not it's legal yet. 


.. code-block:: python
    :linenos:
    
    class MCState:
        ### MC is missionaries and cannibals
        
        def __init__(self, state_vars, num_moves=0, parent=None):
            ### The init function is going to be whatever we decided from the previous part!
            
                
        def get_possible_moves(self):
            ## get all possible moves. this should be the code from above!
            pass
            
        def get_next_states(self):
            ## using possible move, get next states
            
            moves = self.get_possible_moves
            all_states = list()
            for move in moves:
                new_state_vars = "what would this be?"
                print("- Applied move: {}")
                print("- Getting state vars: {}".format(new_state_vars)
                
                ## notice the number of moves is increasing by 1
                ## also notice we are passing self to our child. 
                new_state = MCState(new_state_vars, self.num_moves+1, self)
                all_states.append(new_state)
                
            return all_states
        

Legal States
------------

Now that we have a function which can produce all states, we need to be able to tell if it's
legal!

Fill in the function below. Also, notice I have added a line to the :code:`get_next_states`.
This line tests to see if the state is legal **after** it is created but **before**
it is added to the list of states. 
        
.. code-block:: python
    :linenos:
    
    class MCState:
        ### MC is missionaries and cannibals
        
        def __init__(self, state_vars, num_moves=0, parent=None):
            ### The init function is going to be whatever we decided from the previous part!
            
                
        def get_possible_moves(self):
            ## get all possible moves. this should be the code from above!
            pass
        
        def is_legal(self):
            ## for this exercise, fill in this code!!
            return True
            
        def get_next_states(self):
            ## using possible move, get next states
            ## this should be completed from the previous section!
            
            moves = self.get_possible_moves
            all_states = list()
            for move in moves:
                ### vvvvvvvvvvvvv replace with code from last section
                new_state_vars = "what would this be?"
                print("- Applied move: {}")
                print("- Getting state vars: {}".format(new_state_vars)
                ### ^^^^^^^^^^^^^ replace with code from last section 
                
                ## notice the number of moves is increasing by 1
                ## also notice we are passing self to our child. 
                new_state = MCState(new_state_vars, self.num_moves+1, self)
                
                ### THIS IS THE NEW LINE:
                if new_state.is_legal():
                    all_states.append(new_state)
                
            return all_states
            pass
        



Exercise Extension: Better printing of states
---------------------------------------------

Python lets us specify two functions that should return strings. 
These functions are called whenever you print out the variable.
Although there are two functions and they are used in slightly different
situations, we are going to have them return the same thing.

For this extension, add this to your state class so that it makes more sense when you print it out.

For example: 

.. code-block:: python
    :linenos:
    
    class MCState:
        ### MC is missionaries and cannibals
        
        def __init__(self, state_vars, num_moves=0, parent=None):
            ### The init function is going to be whatever we decided from the previous part!
            
        def __str__(self):
            return "MCState; {} moves deep".format(self.num_moves)
        
        def __repr__(self):
            return str(self)
            
Exercise Extension: Using Properties
------------------------------------

Another shortcut in python is the property decorator. It looks like the class method,
but lets you reference functions as variables.  These functions can
never take arguments, so you are restricted to functions that just return stuff. 

For this extension, convert things that can be properties.  For example:

.. code-block:: python
    :linenos:
    
    class MCState:
        ### MC is missionaries and cannibals
        
        def __init__(self, state_vars, num_moves=0, parent=None):
            ### The init function is going to be whatever we decided from the previous part!
            
                
        @property
        def possible_moves(self):
            ## get all possible moves. this should be the code from above!
            ## this is now a property. notice how it is called below
            pass

    root = MCState.root()
    
    print(root.possible_moves)