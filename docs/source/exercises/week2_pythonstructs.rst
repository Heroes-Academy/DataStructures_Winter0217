[Exercise] Python's Data Structures
===================================

The complexity of an algorithm depends heavily on the data structure that's being used. 

Python has four main data structures. We're going to go through them in this exercise.
You should take hand-written notes and make a cheat sheet for what they do,
and their speed with respect to different operations.  

You should have already completed the timing exercise.  You should use the timing
code you learned there to time the operations below. 


Four Data Structures
^^^^^^^^^^^^^^^^^^^^

.. code-block:: python
    :linenos:
    
    # [0, 1, 2]
    data0 = list()
    
    # (0, 1, 2)
    data1 = tuple()
    
    # set([0,1,2])
    data2 = set()
    
    # {"a": 0, "b": 1}
    data3 = dict()
    
Operations
^^^^^^^^^^

1. Add to the data
2. Find inside the data
3. Iterate through the data
4. Test for membership inside the data


I will show the operations below.  You have to tell me how fast it is per operation.
In other words, if you add 100 numbers into a list, and it takes 3 seconds, that is 3/100 per operation. 
Divide the time by the number of things you did. 

You should also be timing for the four data structures separately. 

Adding to the data
------------------


.. code-block:: python
    :linenos:
    
    def run0():
        data0 = list()
        for i in range(1000):
            data0.append(i*10)
    
    def run1():
        data1 = tuple()
        for i in range(1000):
            # the comma in the parenthesis makes python think it's a tuple
            temp_tuple = (i,)
            data1 = data1 + temp_tuple
    
    def run2():
        data2 = set()
        for i in range(1000):
            data2.add(i)
        
    def run3():
        data3 = dict()
        for i in range(1000):
            data3[i] = i * 10
            
    
    
Testing for membership
----------------------

The code for testing for membership is below.  After you fill each of the variables
full of numbers, do the same for loop and test for speed.  An example for list is below. 

.. code-block:: python
    :linenos:
    
    def run0():
        total_number = 1000
        data0 = list()
        for i in range(total_number):
            data0.append(i*10)
    
        finds = 0
        for i in range(total_number):
            if i in data0:
            finds += 1
            
            
    