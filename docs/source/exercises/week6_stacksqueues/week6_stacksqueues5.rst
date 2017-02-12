Stacks and Queues, Part 5
=========================

These parts are bonus if you get this far =)

Stacks and Recursion
--------------------

Stacks are how a computer represents recursion.  Everytime the recursive function
is called, it places the current call onto a virtual stack.  Then, when that 
function is over, the next active call is retrieved by getting the top of the stack. 
Let's look at this with fibonacci. 

Example: Fibonacci Stack
^^^^^^^^^^^^^^^^^^^^^^^^

For a fibonacci stack, let's first remember how the recursive version looked. 

.. code-block:: python
    :linenos:
    
    def recursive_fibonacci(current_n):
        if current_n == 0 or current_n == 1:
            return current_n
        else:
            n_minus_one = recursive_fibonacci(current_n - 1)
            n_minus_two = recursive_fibonacci(current_n - 2)
            return n_minus_one + n_minus_two
            


Everytime the code makes a recursive call, the state of the function is saved
and put onto a stack.  Then, after it finishes (the return statement), that state
is retrieved by popping the stack. 

Let's look at the implementation with a stack.  You will be asked a couple questions
afterward. 

.. code-block:: python
    :linenos:
    
    from collections import deque
    
    def stack_fibonacci(starting_n):
        stack = deque()
        total = 0
        
        stack.append(starting_n)
        
        while len(stack) > 0:    
            next_n = stack.pop()
            if next_n == 0 or next_n == 1:
                total += next_n
            else:
                stack.append(next_n - 1)
                stack.append(next_n - 2)
        return total

As this :code:`while` loop iterates, the stack and the variables :code:`next_n` and :code:`total` 
will have different values. 

Now you will be doing a write-up.  You will trace through the code and write down
the value of the variables at each loop.  The write-up details are as follows:

1. There are 5 function calls which change the :code:`starting_n`.  These are below.
2. At the end of the while loop, the state is the value each of the variables has. 
3. For each function call, write down the state for each time through the while loop. 
4. A stack can be written like a list, where the first item is the deepest part. 
    - So, :code:`[2,3,4]` is a stack with 4 at the top, 3 in the middle, and 2 at the bottom
    - the next :code:`pop` would remove 4 from the stack. 
    - If you were to push 5 onto the stack without popping 4, you would have :code:`[2,3,4,5]`

.. code-block:: python
    :linenos:
    
    for i in range(1, 5):
        print("{}: {}".format(stack_fibonacci(1))
    
    
I will do 6 for you:

.. code-block:: python
    :linenos:
    
    stack_fibonacci(6)
    
Initially::
    stack = empty
    total = 0
    
Then, :code:`starting_n` is pushed onto the stack::
    stack = [6]
    
When you write yours for 1-5, you can start at that point. 

Loop 0::

    next_n = 6
    # remember, add next_n-1 THEN next_n-2
    stack = [5, 4]
    total = 0

Loop 1::

    next_n = 4
    # remember, add next_n-1 THEN next_n-2
    stack = [5, 3, 2] 
    total = 0

Loop 2::

    next_n = 2
    # remember, add next_n-1 THEN next_n-2
    stack = [5, 3, 1, 0] 
    total = 0
    
Loop 3::

    next_n = 0
    # now, it is 0, so add it to total. except adding 0 is a waste! oh well.. 
    # maybe we could have made it faster and checked for 0 BEFORE adding
    stack = [5, 3, 1] 
    total = 0 + 0
    
Loop 4::

    next_n = 1
    # now it is a 1!  So add it to total
    stack = [5, 3] 
    total = 0 + 1 = 1

Loop 5::

    next_n = 3
    # remember, add next_n-1 THEN next_n-2
    stack = [5, 2, 1] 
    total = 1

Loop 6::

    next_n = 1
    # a 1 adds into total
    stack = [5, 2]
    total = 2

Loop 7::

    next_n = 2
    # a 1 adds into total
    stack = [5, 1, 0]
    total = 2

Loop 8::

    next_n = 0
    # a 0 adds into total
    stack = [5, 1]
    total = 2 + 0
    
Loop 9::

    next_n = 1
    # a 1 adds into total
    stack = [5]
    total = 2 + 1
    
Loop 10::

    next_n = 5
    # 5 is removed from the stack and adds 4, 3
    stack = [4, 3]
    total = 3
    
Loop 11::

    next_n = 3
    # 3 is removed from the stack, adds 2, 1
    stack = [4, 2, 1]
    total = 3
    
Loop 12::

    next_n = 1
    # a 1 adds into total
    stack = [4, 2]
    total = 3 + 1 
    
Loop 13::

    next_n = 2
    # a 2 is removed from the stack, adds 1, 0
    stack = [4, 1, 0]
    total = 4
    
Loop 14::

    next_n = 0
    # a 0 adds into total
    stack = [4, 1]
    total = 4

Loop 15::

    next_n = 1
    # a 1 adds into total
    stack = [4]
    total = 4 + 1

Loop 16::

    next_n = 4
    # a 4 is removed from the stack, adds 3, 2
    stack = [3, 2]
    total = 5

Loop 17::

    next_n = 2
    # a 2 is removed from the stack, adds 1, 0
    stack = [3, 1, 0]
    total = 5

Loop 18::

    next_n = 0
    # a 0 is added into total
    stack = [3, 1]
    total = 5 + 0
    
Loop 19::

    next_n = 1
    # a 1 is added into total
    stack = [3]
    total = 5 + 1

Loop 20::

    next_n = 3
    # a 3 is removed from the stack, adds 2, 1
    stack = [2, 1]
    total = 6

Loop 21::

    next_n = 1
    # a 1 is added to the total
    stack = [2]
    total = 6 + 1
    
Loop 22::

    next_n = 2
    # a 2 is removed from the stack, adds 1, 0
    stack = [1,0]
    total = 7

Loop 23::

    next_n = 0
    # a 0 is added to the total
    stack = [1]
    total = 7 + 0
    
Loop 25::

    next_n = 1
    # a 1 is added to the total
    stack = []
    total = 7 + 1 = 8
    
At this point, the while loop ends and :code:`total` is returned, which is 8!
    
    