Linked List Families, 4
=======================


Now that you have a PersonLine that works, let's try a new challenge.

.. code-block:: python
    :linenos:
    
    class PersonLine:
        def __init__(self):
            self.first_person = None
        
        def add_new_person(self, new_person):
            if self.first_person == None:
                self.first_person = new_person
            else:
                self.first_person.set_next_person(new_person)
                
        def add_to_end_of_line(self, new_person):
            print("How could you add someone to the end of the line directly?")
        
        

Take a look at the above code.  Let's say we want to just add people to the back
of the line directly without having to have them go and talk to everyone in the line just to
find the back!


        
        