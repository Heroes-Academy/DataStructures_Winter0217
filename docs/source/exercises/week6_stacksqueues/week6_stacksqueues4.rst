Stacks and Queues, Part 4
=========================

Checking Validity
-----------------

We can also use a stack to check the validity of a math expression. 
For this, we want to know: are the parenthesis balanced.
For example, is :code:`(5+5`  balanced?  What about :code:`3 / (4 * (2+4))`

These are easy to check with a stack.  The procedure is as follows:

1. Start a :code:`for` loop over the input string
2. Every time you see a left parentheses, '(', push it onto the stack.
3. Every time you see a right parentheses, ')', pop it from the stack.
4. If the loop ends and there are items left on the stack, that means it's not valid! (there are too many left parentheses)
5. If you see a right parentheses and the stack is empty, it means it's not valid! (there are too many right parentheses)

Finish the function below to accomplish this.  We will use indexing again. 

.. code-block:: python
    :linenos:
    
    from collections import deque

    def validity_checking(in_string):
        
        stack = queue()
        
        num_characters = len(in_string)
        
        for index in range(num_characters):
            current_character = in_string[index]
        

    assert validity_checking("(x)") == True
    assert validity_checking("((y)") == False
    assert validity_checking("(z))") == False
    
    assert validity_checking("((a))") == True
    assert validity_checking("((a+b)))") == False
    assert validity_checking("(((42)") == False

    

When you have finished with this, go on to :doc:`Part 5 <week6_stacksqueues5>`.