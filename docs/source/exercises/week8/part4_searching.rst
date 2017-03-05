Part 4: Searching
=================

Given that we have a class which can represent the state of missionaries and
cannibals, and we have a function which can generate the next possible states,
we need a way of organizing those states so that we can search for a solution!

There are 2 primary methods that we will explore:

1. Depth First Search
2. Breadth First Search


Searching with Queues and Stacks
--------------------------------

First, let's write a function which maintains the search:

.. code-block:: python
    :linenos:
    
    from collections import deque
    
    def search():
    
        root = MCState.root()
        
        to_search = deque()
        
        to_search.append(root)
        
        while len(to_search) > 0:
            current_state = to_search.pop()
            
            next_states = current_state.get_next_states()
            
            to_search.extend(next_states)
            

What's missing from this?  

1. A test for completion
2. A test for duplicates


Testing for existance
---------------------

We want a uniqueness test that lets us see if something has been visited before.
This is the primary reason why we want to use tuples are our state variable. 
By doing this, we can :code:`hash` them and use them in :code:`sets`.

.. code-block:: python
    :linenos:
    
    state_var = (0,0,0)
    
    seen_states = set()
    
    if state_var not in seen_states:
        print("not seen yet")
        seen_states.add(state_var)
        
    if state_var in seen_states:
        print("already saw this!")
        
We need to do this with our states. But we should keep it ouside of our class~
Instead, the :code:`seen_states` set should go inside the search function above. 

Do the following when the function creates the new states:

    - loop over them and check to see if they are in the set yet
        + if they are, do not add them into :code:`to_search`
        + if they aren't, add them to :code:`to_search` AND to the set :code:`seen_states`


Task 1
^^^^^^

Add a function to the class to test for it being completed.  Test for this on each
of the states in the search loop.  If something is completed, return it. 


Depth vs Breadth First Search as Stacks and Queues
--------------------------------------------------

In the current implementation, what is the order of states that will be searched?

The way to answer that is to think about what :code:`to_search` is doing. 
It is taking the right most item (with the :code:`pop` function) and searching
its children.  It is putting the children onto the right as well (with :code:`extend`).





            
        