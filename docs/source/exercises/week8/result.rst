Missionaries and Cannibals, partial solution
============================================

Here is some code for a partial solution to the exercises.  There were
two files. They are labeled below. 

.. code-block:: python
    :linenos:
        
    ''' mclib.py '''
    class MCState:
        ### MC is missionaries and cannibals
        def __init__(self, state_vars, num_moves=0, parent=None):
            self.state_vars = state_vars
            self.num_moves = num_moves
            self.parent = parent
    
        ### decorator
        @classmethod
        def root(cls):
            return cls((3,3,1))
    
        def get_possible_moves(self):
            ''' return all possible moves in the game as tuples
            possible moves:
                1 or 2 mis
                1 or 2 cannibals
                1 mis, 1 can
            '''
    
            moves = [(1, 0), (2, 0), (0, 1), (0, 2), (1, 1)]
            return moves
    
        def get_next_states(self):
            ## using possible move, get next states
    
            moves = self.get_possible_moves()
            all_states = list()
            print("inside state with {} state variables".format(self.state_vars))
            mis_right, can_right, raft_right = self.state_vars
            ## if raft is on right, subtract move from these numbers
            ## if raft is on left, add these move numbers to these numbers
            for move in moves:
                change_mis, change_can = move
                if raft_right == 1:  ## mis_right = 3; can_right = 3, raft_right = 1
                    new_state_vars = (mis_right-change_mis, can_right-change_can, 0)
                else:
                    new_state_vars = (mis_right+change_mis, can_right+change_can, 1)
                print("- Applied move: {}".format(move))
                print("- Getting state vars: {}".format(new_state_vars))
    
                ## notice the number of moves is increasing by 1
                ## also notice we are passing self to our child.
                new_state = MCState(new_state_vars, self.num_moves+1, self)
                all_states.append(new_state)
    
            return all_states
    
        def __str__(self):
            return "MCState; {} moves deep".format(self.num_moves)
    
        def __repr__(self):
            return str(self)
            
            
            
            
    ''' second file: mcrun.py '''
    from mclib import MCState
    ### number missionaries, number cannibals, raft side
    ### for each, number on right side of river
    ### everything is trying to move left
    ### (3, 3, 1)
    
    root = MCState.root()
    
    print(root.get_possible_moves())
    
    next_states = root.get_next_states()
    state = next_states[0]
    print(state)
    state.get_next_states()