Linked List Families, 2
=======================


So, did you answer that Elroy would cut in front of Jane and that
Jane would no longer be connected?

Let's look at why:

.. code-block:: python
    :linenos:
    
    class Person:
        def __init__(self, name):
            self.name = name
            self.next = None
            
        def set_next_person(self, next_person):
            self.next = next_person
    
    george = Person("George Jetson")
    jane = Person("Jane Jetson")
    judy = Person("Judy Jetson")
    
    george.set_next_person(jane)
    jane.set_next_person(judy)
    
    elroy = Person("Elroy Jetson")
    jane.set_next_person(elroy)

You can see that :code:`self.next` is equal to whichever :code:`Person` 
is given to Jane's function :code:`set_next_person`.  So, that makes Elroy
the next person because he was the last one to do it!

What would we have to do to make it so that Elroy couldn't cut in line?
The best way is to have Jane's the :code:`set_next_person` check to see if there's a person
behind them yet.  If there isn't, then the new person gets to stand behind Jane!

IF there is a person standing behind Jane (like Judy), then Jane should make the
new person stand behind the person already there!

To say it more like a computer scientist: inside the :code:`set_next_person` function, 
if the :code:`self.next` variable is empty (equal to None), then you can set :code:`self.next`
as the new person.  But, if it isn't None, that means you have to have :code:`next_person`
go to the back of the line.  You can do this by calling the :code:`set_next_person` on
the :code:`self.next`!

You should code this.  Hint:  It is an if statement.  There are two possibilities, described in the last
paragraph.  You should test for these possibilites and do the correct action!

Once you have done that, :doc:`click here <week5_linkedlist3>` to go to the next page!

