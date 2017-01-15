[Exercise]  Timing
==================

Knowing the runtime of an algorithm can be analyzed through math.  An easy way to
test and verify this math is to simulate a bunch of operations and record the time it takes.

For this, we need the :code:`time` module.  


.. code-block:: python
    :linenos:
    
    import time
    
    def run():
        start = time.time()
        
        ### do some stuff
        
        end = time.time()
        
        total = end - start
        
        print("Start time: {}".format(start))
        print("End time: {}".format(end))
        print("Total time: {}".format(total))
    
    run()
    

Fill in the code above and time the following operations


Looping with squaring:

.. code-block:: python
    :linenos:
    
    def run():
        
        x = 0
        for i in range(1000):
            x += i ** 2
        
    run()

Looping with list appending and lookup

.. code-block:: python
    :linenos:
    
    def run():
    
        unique_list = list()
        repeated_list = list()
        
        for i in range(1000):
            if i in unique_list:
                repeated_list.append(i)
            else:
                unique_list.append(i)
                unique_list.append(i**2+i)
                unique_list.append(i**2+2*i)
    
    run()
    
    

Advanced
--------

You can write a function which takes the :code:`run` and times it. 

.. code-block:: python
    :linenos:
    
    import time
    
    
    def time_it(func):
            
        start = time.time()
        
        func()
        
        end = time.time()
        
        total = end - start
        
        print("Start time: {}".format(start))
        print("End time: {}".format(end))
        print("Total time: {}".format(total))
        
    
    def run0():
        x = 0
        for i in range(1000):
            x += i ** 2
    
    def run1():
    
        unique_list = list()
        repeated_list = list()
        
        for i in range(1000):
            if i in unique_list:
                repeated_list.append(i)
            else:
                unique_list.append(i)
                unique_list.append(i**2+i)
                unique_list.append(i**2+2*i)
    
    
    def run_all():
        print("going to run v0 now")
        
        time_it(run0)
        
        print("going to run v1 now")
        
        time_it(run1)
    
    run_all()