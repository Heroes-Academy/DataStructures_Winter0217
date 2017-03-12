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

Be careful if you run this. Currently, it will run forever! This is because
we are not searching for duplicates, and we are not testing for success!


Testing for existence
---------------------

We want a uniqueness test that lets us see if something has been visited before.
This is the primary reason why we want to use tuples are our state variable. 
By doing this, we can :code:`hash` them and use them in :code:`sets`.

.. code-block:: python
    :linenos:
    
        
    from collections import deque
    
    def search(exit_on_solution=False):
    
        root = MCState.root()
        
        to_search = deque()
        seen_states = set()
        solutions = list()
        
        to_search.append(root)
        
        while len(to_search) > 0:
            current_state = to_search.pop()
            if current_state.is_solution():
                ## this is a successful state!
                ## the state vars should be (0,0,0)
                if exit_on_solution:
                    ## we just return the state
                    return current_state
                else:
                    ## we are just saving it this time
                    solutions.append(current_state)
            
            next_states = current_state.get_next_states()
            
            for possible_next_state in next_states:
                possible_state_vars = possible_next_state.state_vars
                if possible_state_vars not in seen_states:
                    # the state variables haven't been seen yet
                    # so we add the state itself into the to_search deque
                    to_search.append(possible_next_state)

                    # now that we have "seen" the state, we add the state vars
                    # to the set!
                    seen_states.add(possible_state_vars)

        print("Found {} solutions".format(len(solutions)))
        return solutions

Testing for Success
------------------

The search above uses a function :code:`current_state.is_solution()`.  Write this
function inside the :code:`MCState` class so that it returns True **only** if the
state vars are :code:`(0,0,0)`.


Thinking Exercise
-----------------

Think about how the search is currently moving. 

In the current implementation, what is the order of states that will be searched?

The way to answer that is to think about what :code:`to_search` is doing. 
It is taking the right most item (with the :code:`pop` function) and searching
its children.  It is putting the children onto the right as well (with :code:`extend`).

You should try drawing out a tree on paper where each node is one of the states. 
This is really helpful in visualizing this. 