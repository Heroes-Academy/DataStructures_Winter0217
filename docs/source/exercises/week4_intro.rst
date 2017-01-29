[Week 4 Exercises] Test-Driven Code, Introductions, and Refreshers
==================================================================

In this initial set of exercises, we will look at three topics:

1. What is test-driven code?
2. How do lists and classes work again?
3. What is a linked list?


Test Driven Coding
------------------

Test Driven Coding means always thinking about how you can prove that your code works.
The best way to prove your code works is to try things that could break it. 

Right now, I will just introduce how you can put tests inside your files. 

Use the following code:

.. code-block:: python
    :linenos:
    
    def square(x):
        return x ** 2
        
    if __name__ == "__main__":
        print("Testing the square function")
        assert square(2) == 4
        

The important thing about this is the :code:`if` statement. This code will only run
when the file is being directly run. Later, when we import code from other files, it won't run
this code.  

For now, we will put our tests in this section of files. 


Lists and Classes
-----------------

Lists are really useful data structure that Python provides. They provide the following functions:

.. code-block:: python
    :linenos:
    
    # two ways of creating
    groceries = list()
    groceries = [] 
    
    # add new items to it
    groceries.append("apples")
    groceries.append("potatoes")
    
    # remove items from it by specifying the exact location
    del groceries[0]
    

Classes let you define the structure of information and then use it in different ways. 

.. code-block:: python
    :linenos:
    
    class Student:
    
        def __init__(self, name):
            self.name = name
        
    
    bob = Student("Robert")
    
    print(bob.name)
    
They have internal variables.  From the outside, you access them through dot notation
on the variable name that is being used for them. 

From the inside, you access them using :code:`self` variables, which Python has
make a feature of every internal function.  

.. code-block:: python
    :linenos:
    
    class Student:
    
        def __init__(self, name):
            self.name = name
            self.points = 0
            
        def add_points(self, new_points):
            self.points = self.points + 10 #what's the shortcut for this command?
        
    
    bob = Student("Robert")
    
    print(bob.name)
    print(bob.points)
    
    bob.add_points(100)
    print(bob.points)
    

What is a linked list?
----------------------

A linked list is a classic data structure.  It is conceptually like parts of Python's list.
Specifically, the :code:`append` function is a function linked lists have!

But, linked lists are actually just individual items that can see only two things:

1. Their content
2. Their next door neighbor

You can think of this as people in a line who don't know who's in front of them,
but they can point at who's behind them!

Then, there is a single manager who knows the first item.  This is what starts the line.

Linked Lists with Cards
***********************

Get a deck of cards and two sheets of paper. Do the following:

1. Put down the numbers 1 through 10 on your paper, spread far across. There will be 1 card per number.
2. Deal out 10 cards, one to each number.

- You can think of what you just did as how a computer stores information. 
- The numbers 1 through 10 represent the memory adddresses of a computer.
- The cards represent the content of the variables there!

- Now, on the other sheet of paper you will be drawing a linked list.  
    + A linked list can be drawn as a rectangle with a line dividing it into two halves.  
- The first half should always have the content written in (so, the card number and suit). 
    + Let's call that the "Content Side".
- The second half is going to be "pointing" at its next door neighbor!  
    + For us, that "pointing" is going to be the memory address.  
    + So, it is the number on the paper for the specific card!
    + Let's call this half the "Memory Side".

1. Draw a linked list that starts with the smallest card.  This is a single box with two halves.
2. Write the card number and the card suit in the Content Side. 
3. Next, find the second smallest card. It is second in the list. 
4. Make a new box and put its card number and card suit in the Content Side.
5. Write the address of the second box into the Memory side of the first box.
6. You now have a two-item linked list!
7. Do this for the rest of the cards, smallest to biggest. 
8. You decide for tie breaks (if there are any).
