Week 8: Sorting
===============


Summary
-------

Today we covered the major sorting algorithms.  We discussed how each sorting algorithm and how it navigates the list of items. Specifically, we went over how bubble sort will check each item as it moves up the list, while sorts like selection sort will assume the list before it is sorted.  We also discussed the divide and conquer sorts like mergesort and quicksort.  To finish off, we went over heaps and how heapsort and its operations work. 


Homework
--------

There are two options for homeworks:

Option 1
^^^^^^^^

Take two of the sort algorithms from the slides and benchmark them.  You should aim for benchmarking with a randomized, a sorted, and a reversely sorted list. The following code will help with this:

.. code:: python 

  import random
  test_numbers = list(range(1,10**10)
  # this shuffles in place; it does not return a copy of test_numbers 
  random.shuffle(test_numbers)
  
  import time
  start_time = time.time()
  sort_function(test_numbers)
  total_time = time.time() - start_time
  
  print("The algorithm took {} seconds".format(total_time))
    
    
Option 2
^^^^^^^^

Implement the heap data structure.  There are resources below, and information in the slides.  It should be a max-heap.  It should turn a new array into a heap.  It should then allow for inserts and pops. 
    

Extra Resources
---------------

Lecture Slides
--------------

.. raw:: html

    <iframe src="https://docs.google.com/presentation/d/1bVHPG03GDrDHsbHv8JDIcpV5G1sx5tjS-VfuT-bWpaM/embed?start=false&loop=false&delayms=60000" frameborder="0" width="480" height="299" allowfullscreen="true" mozallowfullscreen="true" webkitallowfullscreen="true"></iframe>
