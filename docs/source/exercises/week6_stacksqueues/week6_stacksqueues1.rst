Stacks and Queues, Part 1
=========================

Today we will be talking about stacks and queues!
They are the two most common data structures.

Since you have looked at linked lists and how to add things to the front
and to the back, you mostly know how this works!


collections.deque
-----------------

Today, instead of writing our own class to do the basic operations,
we are going to work with python's stack and queue data structure, :code:`deque`.

.. code-block:: python
    :linenos:

    from collections import deque
    
:code:`deque` is just like our :code:`PersonLine` from last week in that it
lets us add new things at the front or the next of the line.

Historically, there are special names for adding and removing from lines: **push**
and **pop**.  In Python, they still call it **pop**, but pushing is called **append**.

Let's look at some examples. In these examples, there are two main functions:
:code:`append` which adds to the right side of the line and
:code:`pop` which removes the person from the right and returns that value.
There are also versions of these two functions for the **left** side:
:code:`appendleft` and :code:`popleft`

.. code-block:: python
    :linenos:

    from collections import deque
    
    line = deque()
    
    line.append("Bob")
    line.append("Sally")
    line.append("Larry")
    line.append("Julia")
    
    ## who is at the front of the line?
    ## who will get removed if I call line.pop()?
    ## what if I call line.popleft()?
    
    person1 = line.pop()
    print("From line.pop(): {}".format(person1))
    
    person2 = line.popleft()
    print("From line.popleft(): {}".format(person2))
    
    

:doc:`Click here for the next page. <week6_stacksqueues2>`
Don't go on until you have guessed the answer!