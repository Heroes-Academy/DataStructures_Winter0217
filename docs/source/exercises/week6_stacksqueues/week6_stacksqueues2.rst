Stacks and Queues, Part 2
=========================

Example from last page
----------------------

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
    ## This will print "From line.pop(): Julia"
    
    person2 = line.popleft()
    print("From line.popleft(): {}".format(person2))
    ## This will print "From line.popleft(): Bob"
    
    
    
Wrappers
--------

What is a wrapper?

A wrapper is a class which provides functions that you want and accomplishes those
functions by using something else.  For example, we could rewrite our
:code:`PersonLine` class which used the :code:`deque` to manage the line!

In fact, we will!

.. code-block:: python
    :linenos:
    
    from collections import deque
    
    class Person:
        def __init__(self, name):
            self.name = name
    
    class PersonLine:
        def __init__(self):
            self.line = deque()
        
        def add_new_person(self, new_person):
            self.line.append(new_person)
        
        def get_first_person(self):
            print("what should go here?")
            
        
    #### tests
    
    george = Person("George Jetson")
    jane = Person("Jane Jetson")
    judy = Person("Judy Jetson")
        
    line = PersonLine()
    line.add_new_person(george)
    line.add_new_person(jane)
    line.add_new_person(judy)
    
    first_in_line = line.get_first_person()
    
    print("{} is first in line!".format(first_in_line.name))
        
Now we have a :code:`PersonLine` which lets us add people to the back of the line
and get people from the front of the line!  

But what code goes in the function :code:`get_first_person`?  Hint: it should
return a value and it should get that value from the :code:`self.line`!

When you have finished this function, you can go onto :doc:`Part 3 <week6_stacksqueues3>`.

