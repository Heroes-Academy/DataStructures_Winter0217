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
        
