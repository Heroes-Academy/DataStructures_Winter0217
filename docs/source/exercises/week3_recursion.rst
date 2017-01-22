Week 3 Exercises: Recursion
===========================

Recursion is super fun!

There are two sections: recursive functions to compute things and recursive functions to draw things!


Computing
---------

For each of these problems, define the base case and the recursive case! 
I've done the first one for you.

Find the Minimum of a List
**************************

Use a recursive function to find the mininum of a list. 

.. code-block:: python
    :linenos:
    
    def minimum_of_list(some_list):
        # base case
        if len(some_list) == 1:
            # return that item!
            return some_list[0]
        #recursive case
        else:
            # get the length of the list
            n = len(some_list)
            # find the halfway point
            halfway = n // 2
            # use recursion to find the minimum of the left side
            min_left = minimum_of_list(some_list[:halfway])
            # use recursion to find the minimum of the right side
            min_right = minimum_of_list(some_list[halfway:])
            # return the smallest one
            if min_left < min_right:
                return min_left
            else:
                return min_right
        
    def run():
        assert 1 == minimum_of_list([1,2,3])
        
        assert -10 == minimum_of_list([1,-10,3])
        
        assert 4 == minimum_of_list([10,20,4])
    
Test for a Palindrome
*********************

A palindrome is the same forwards as it is backwards. 
There could be several ways to do this.  One way:

1. Check to see if the ends are the same
   - :code:`some_string[0] == some_string[-1]`
2. Call the function on the string without the ends
   - :code:`new_string = old_string[1:-1]`

- The base case: 
  + The string is empty or of length 1
- The recursive case
  + Check to see if the ends are equal
  + Check to see if the interior is a palindrome
  + return the :code:`and` of the result

.. code-block:: python
    :linenos:
    
    def is_palindrome(some_string):
        if len(some_string) <= 1:
            return True 
        else:
            ### fill in code here
            
    def run():
        assert is_palindrome('bob') == True # do I need to have the == though?
        
        assert is_palindrome('wow') # no!
        
        assert not is_palindrome('potato') 
        
        assert is_palindrome('mirror image|egami rorrim')
        

Hailstone Sequence
******************

A hailstone sequence is a sequence with the following operations:

For each number, if the number is even, the new number is that number divided by 2.
If it is odd, the new number is that number times 3 plus 1.
This is repeated until the new number is 1.

More precisely:

.. code-block:: python
    :linenos:
    
    if n%2 == 0: 
        n = n // 2
    else:
        n = n*3 + 1
    

Write a function which computes the length of the hailstone sequence

.. code-block:: python
    :linenos:
    
    def hailstone_length(n):
        #base case:
        if n == 1:
            return 1
            
    def run():
        assert hailstone_length(1) == 1
        assert hailstone_length(2) == 2
        assert hailstone_length(3) == 8
        assert hailstone_length(4) == 3
        assert hailstone_length(5) == 6
        assert hailstone_length(6) == 9
        assert hailstone_length(7) == 17
        assert hailstone_length(8) == 4
        assert hailstone_length(9) == 20
        
        
Turtles
-------

Recursive turtles are really fun =).

First, though, set up a file and define a function which lets you make turtles really easily:


.. code-block:: python
    :linenos:
    
    import turtle
    
    def getbob():
        bob = turtle.Turtle()
        bob.left(90)
        bob.speed('fastest')
        jump(bob, 0,0)
        return bob



Next, I will show you some of the recursive turtles.  Run them and play with the code.
Try and make your own!



Tree
****

.. code-block:: python
    :linenos:

    def tree(t, length, branch_num, depth, width=90.0, ratio=2/3.):
    
        # make the pen size bigger if near top of the tree
        t.pensize(depth+1)
        # go forward for the trunk
        t.forward(length)
        # if not at the base case
        if depth > 0:
            # turn left half of the width
            t.left(width/2)
            
            # for each branch, make a subtree
            for x in range(branch_num-1):
                
                # the subtree!
                #        new_length             new_depth
                tree(t, length*ratio, branch_num, depth-1, width, ratio)
            
                # turn right to match the number of branches    
                t.right(width/(branch_num-1))
                
            # do one final tree because the pattern was supposed to be
            # left, subtree, right, subtree, right, subtree, left 
            # for 3 branches
            tree(t, length*ratio, branch_num, depth-1, width, ratio)
            
            t.left(width/2)
    
        # back up!
        t.backward(length)
        
    def run_tree():
        bob = get_bob()
        
        length = 200
        branch = 2
        depth = 9
        angle = 140.
        reduc = 0.7
    
        tree(bob, length, branch, depth, angle, reduc)

Sierpinski
**********

Sierpinksi triangles are really cool mathematical patterns!


def sierpinski(t, length, depth, first=True):
    if first:
        t.setheading(0)


    bob.color('black', 'black')
    bob.begin_fill()
    for _ in range(3):
        t.forward(length)
        t.left(120)

        if depth > 0:
            sierpinski(t, length/2, depth-1, False)
    bob.end_fill()
    
    
    
    
Snowflake
*********

def snowflakev2(t, n, d):
    if d == 0:
        return
        t.forward(n)
    else:
        snowflakev2(t, n/3, d-1)
        t.right(120)
        t.forward(n)
        snowflakev2(t, n/3, d-1)
        return
        for _ in range(3):
            t.right(120)
            snowflakev2(t, n/3, d-1)
            t.forward(n / 3)

def snowflake(t, n, d, mod=1):
    if d == 0:
        t.forward(n*mod)
    else:
        snowflake(t, n/3, d-1)
        t.left(60)
        snowflake(t, n/3, d-1)
        t.right(120)
        snowflake(t, n/3, d-1)
        t.left(60)
        snowflake(t, n/3, d-1)
            
def neat(bob):

    bob.setheading(0)
    bob.penup(); bob.setpos(-300,0); bob.pendown()
    bob.begin_fill()
    snowflake(bob, 700, 4)
    bob.setheading(180)
    snowflake(bob, 700, 4, -1)
    bob.end_fill()

    bob.color('black', 'purple')
    bob.setheading(0)
    bob.penup(); bob.setpos(-140,0); bob.pendown()
    bob.begin_fill()
    snowflake(bob, 375, 4)
    bob.setheading(180)
    snowflake(bob, 375, 4, -1)
    bob.end_fill()


    bob.color('black', 'blue')
    bob.setheading(0)
    bob.penup(); bob.setpos(-140*0.4666,0); bob.pendown()
    bob.begin_fill()
    snowflake(bob, 375*0.5357, 4)
    bob.setheading(180)
    snowflake(bob, 375*0.5357, 4, -1)
    bob.end_fill()

            
def carpet(t, l, d):
    for _ in range(4):
        t.forward(l/3)
        t.left(90)
    t.forward(l)

    if d > 0:
        t.penup()
        t.forward(l/4)
        t.left(90)
        t.backward(l/4)
        t.pendown()

        for _ in range(4):
            carpet(t, l/6, d-1)
            t.penup()
            t.forward((l/4 + l)/2)
            t.pendown()
            carpet(t, l/6, d-1)
            t.penup()
            t.forward((l/4 + l)/2)
            t.pendown()
            t.left(90)
            
            
