[Week 9]: Projects
========================


Summary
-------

We will start class by reviewing what we've covered these last 9 weeks.
Then, you will work on your projects!  If you didn't get a working
prototype over the week, the goal is to get one by the end of the class time. 
See below for the project prototype requirements.


Project Prototype
-----------------

The project is to implement a search for a problem of your choosing. 
Last week we did Missionaries and Cannibals in class and I provided links
to some other options.  These included tic-tac-toe, nim, and some others. 

The important parts of the search are:

1. The search state representation
    - this should be some set of variables which represent the state of the game
    - You should define both your start and your goal states. 
    - In the missionaries and cannibals, it was a tuple with three things:
        1. "how many missionaries on the right side"
        2. "how many cannibals on the right side"
        3. "how many boats on the right side"
    - The start state was :code:`(3, 3, 1)`
    - The goal state was :code:`(0,0,0)`
    - In general, representing with tuples is a good easy first solution. 
2. The set of possible actions
    - Given the way you represented the state, what are all the ways the state can change?
    - This is usually determined by the rules of the game
    - For example, in Missionaries and Cannibals, the rules were the you can only
    have two people in a boat at one time.  
    - So, we could do the following actions in one boat trip:
        1. 2 Missionaries, 0 Cannibals
        2. 1 Missiionary, 0 Cannibals
        3. 1 Missionary, 1 Cannibal
        4. 0 Missionaries, 1 Cannibal
        5. 0 Missionaries, 2 Cannibals
    - We don't mention the boat because it just changes sides to whichever side it wasn't on
    - To represent this as changes to our state, we can say each of these three moves is a tuple:
        1. :code:`(2,0)`
        2. :code:`(1,0)`
        3. :code:`(1,1)`
        4. :code:`(0,1)`
        5. :code:`(0,2)`
3. A rule for applying the actions to the state that results in a new state
    - Given that you have your state and set of actions, there should be a rule
    that you can turn into a function that determines the new state. 
    - For example, in missionaries and cannibals:
        - If the boat is on the left side, then the action is to bring the specified people to the right
        - If the boat is on the right side, then the action is to bring the specified people to the left
        - So if the state is :code:`(3,3,1)`, the boat is on the right, and any actions will bring people to the left
        - To bring people to the left, we subtract our move numbers
        - So, the move :code:`(1,1)`, which is 1 missionary and 1 cannibal, will result in the state :code:`(2,2,0)`
        - If the boat were on the left side, we **add** our move numbers to the state because we are bringing people to the right
        and the state represents the number of people on the right
4. A test for illegal actions
    - When are actions illegal?  
    - You might have to apply the actions to your state a couple of time to notice the possible illegal states
    - It usually comes from possibilities that are outside of realistic situations
    - For example, in Missionaries and Cannibals:
        - if we were in the state :code:`(2,2,0)`, we still have the full set of actions available
        - So we could pick the action :code:`(2,0)` which means "2 missionaries use the boat"
        - Since the boat is on the left side, we would add the number to our state
        - This results in state :code:`(4,2,1)`. 
        - This state is clearly impossible!
    - Given this example, you should just have a rule that tells you when things are impossible
5. A test for losing states
    - when is the state a losing state?  
    - In Missionaries and Cannibals, the state is a losing state when:
        - there are more cannibals than missionaries on either side. 
6. A test for the winning state
    - when is the state a winning state?
    - In missionaries and cannibals, the winning state is :code:`(0,0,0)`
    

So, to sum that up, you need:

1. State Representation
2. Action Representation
3. Rule for applying actions to states
4. Test for illegal actions
5. Test for losing states
6. Test for winning states

Given these things, the search is fairly simple. 
Below is the example code from Missionaries and Cannibals. 
When you implement your state code, this search code should also work for you.
It is the following steps:

1. Create the initial root state
2. Create the python data structures that are useful (:code:`to_search, seen-states, solutions`)
3. Loop until the :code:`to_search` stack/queue is empty
4. Get the next state
5. Check to see if it's a solution
6. If it's not a solution, look at the states that can follow it
7. Add in any states we haven't seen yet 
    - an example of a state that could repeat is just bringing 1 person back
    and forth forever.


.. code-block:: python
    :linenos:
    
    
    ### this is the stack/queue that we used before
    from collections import deque
    
    ### create the root state
    root = MCState.root()
        
        
    ### we use the stack/queue for keeping track of where to search next
    to_search = deque()
    
    ### use a set to keep track fo where we've been
    seen_states = set()
    
    ### use a list to keep track of the solutions that have been seen
    solutions = list()
    
    ### start the search with the root
    to_search.append(root)
    
    
    ### while the stack/queue still has items
    while len(to_search) > 0:
    
        ### get the next item
        current_state = to_search.pop()
        
        ### Test for Winning State
        if current_state.is_solution():
            ## this is a successful state!
            ## the state vars should be (0,0,0)
            
            ## Save it into our solutions list 
            solutions.append(current_state)
            
            ## we don't really want to go through the rest of this loop
            ## continue will skip the rest of the loop and start at the top again
            continue
        
        ## look at the current state's children 
        ## this uses the rule for actions and moves to create next states
        ## it is also removing all illegal states
        next_states = current_state.get_next_states()
        
        ## next_states is a list, so iterate through it
        for possible_next_state in next_states:
            
            ## to see if we've been here before, we look at the state variables
            possible_state_vars = possible_next_state.state_vars
            
            ## we use the set and the "not in" boolean comparison 
            if possible_state_vars not in seen_states:
            
                # the state variables haven't been seen yet
                # so we add the state itself into the searching stack/queue
                
                #### IMPORTANT
                ## which side we append on changes how the search works
                ## why is this?
                to_search.append(possible_next_state)

                # now that we have "seen" the state, we add the state vars to the set.
                # this means next time when we do the "not in", that will return False
                # because it IS in
                seen_states.add(possible_state_vars)

    ## finally, we reach this line when the stack/queue is empty (len(to_searching==))
    print("Found {} solutions".format(len(solutions)))



Examples of Missionaries and Cannibals in iPython Notebooks
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. raw:: html
    <script src="https://gist.github.com/braingineer/6c1bf90be76b5dbe01ef857ececbbb63.js"></script>

.. raw:: html
    <script src="https://gist.github.com/braingineer/9ce5c8dcc6d4ac8bc8978c15414a269c.js"></script>

Presentation Template
---------------------

You will give a presentation to your parents when we meet next week. 
You will have time at the beginning of class to finish things up, but your presentation
is due to me that Friday. 

Here is the presentation template:

.. raw:: html

    <iframe src="https://docs.google.com/presentation/d/1BhVcGhiUifG9GgATvY1EfhM-_MC87_2DALh5AysicZw/embed?start=false&loop=false&delayms=60000" frameborder="0" width="960" height="569" allowfullscreen="true" mozallowfullscreen="true" webkitallowfullscreen="true"></iframe>