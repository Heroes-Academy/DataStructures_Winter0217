Stacks and Queues, Part 3
=========================

A Queue
-------

The :code:`PersonLine` that we have been talking about this whole time is a **queue**.

We should have discussed this in the slides, but to recover the material:

A Queue is a sequence of items (like the :code:`PersonLine`) where new items
can join the back of the line, and old items are taken off the front of the line.
This makes a Queue as **First In, First Out (FIFO)** data structure. FIFO is extremely important
to remember!  I will ask you about it many times =).


A Stack
-------

A **stack** is very similar to a **queue**, but instead of adding to the back of the line,
it adds to the front of the line!  This is very useful in many different
features of computers.  One you use every day is your browser history!  When
you the back-button, you are actually going to the last thing that was pushed onto the stack!

Because Stacks remove from and add to the front, they are called **Last In, First Out (LIFO)**
data structures.  Some other things that are LIFO: when you make edits and hit the 
undo-button, when you put cups into a cupboard (you use the front ones first!), or
when you take a plate off of a stack of plates (the bottom one was the first to be 
put down!).


Reversing Strings
-----------------

Let's look at how we use a stack to reverse a string (or any list in python).

.. code-block:: python
    :linenos:

    from collections import deque
    

    def reverse(in_string):
        stack = deque()
        
        ### let's use integer indexing to get each character
        
        num_letters = len(in_string)
        
        for index in range(num_letters):
            current_letter = in_string[index]
            # <here>
            ### remove the previous line and put code there that
            ### puts the current_letter onto the top of the stack
            
        
        print("Stack after pushing all letters onto it: {}".format(stack))
        
        ### create a blank string to collect the reverse letters
        out_string = ""
        
        ### the while loop will end when there is nothing left to pop
        while len(stack) > 0:
            ### get the top item off the stack
            ### finish this line:
            next_letter = 
            out_string += next_letter
        
        print("Our reversed string: {}".format(out_string))
        
    reverse("supercalifragilisticexpialidocious")
    
    
When you have finished with this, go on to :doc:`Part 4 <week6_stacksqueues4>`.