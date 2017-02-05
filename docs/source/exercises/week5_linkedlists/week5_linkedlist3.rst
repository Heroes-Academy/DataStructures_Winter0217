Linked List Families, 3
=======================


Now that we have an idea about how the person line is going to work,
let's write class that takes care of the entire line for us!


.. code-block:: python
    :linenos:
    
    class PersonLine:
        def __init__(self):
            self.first_person = None
        
        def add_new_person(self, new_person):
            print("How do I add this person to the line?")
            

Above is the code for a line.  We want to have a function which lets us
add new people to the line.  To do this, we would have to check and see if there 
is anyone in line.  If there isn't, it's that person's lucky break!  They get to be
first!  

If there is someone in line already, though, they have to get behind that person. 
So, we should just tell the new person to get behind the first person in line.
If you did the last page correctly, the new person will keep going down
the line until they find a spot where they can stand. 

If the function from the last page isn't working though, then the new person is
just to budge and become the second person in line, no matter who is already there!

So, write the function to add the new person.  This should be similar to the function
you wrote on the last page: there is only two possibilities!  

You should test with this code:

.. code-block:: python
    :linenos:
    
    george = Person("George Jetson")
    jane = Person("Jane Jetson")
    judy = Person("Judy Jetson")
    elroy = Person("Elroy Jetson")
    
    line = PersonLine()
    
    line.add_new_person(george)
    line.add_new_person(jane)
    line.add_new_person(judy)
    line.add_new_person(elroy)
    
    person_after_jane = jane.next
    print("{} is behind Jane!".format(person_after_jane.name))
    
    ## this does the same thing as above
    print("{} is behind George!".format(george.next.name))
    
    if elroy.next == None:
        print("Elory is last line... he has no one behind him!")
    else:
        print("{} is behind Elroy".format(elroy.next.name))
    

Once you are done, :doc:`click here <week5_linkedlist4>` to go to the next page!