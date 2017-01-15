[Exercise] Finding Prime Numbers
================================

Finding prime numbers is really important to many things in computer science.
Specifically, cryptography and encryption rely heavily on them to secretly encode messages!

Let's look at how to find primes and their run times.

Naive Solution
--------------

The easiest way is to use a double loop and check for "primeness"

.. code-block:: python
    :linenos:
    
    def run(max_number):
        # create list for saving the primes
        found_primes = []
        # loop over the numbers
        for first_number in range(2, max_number+1):
            # create a boolean to save the result
            is_prime = False
            # now go over all numbers smaller than it
            for second_number in range(2, first_number):
                if first_number % second_number == 0:
                    is_prime = False
                else:
                    is_prime = True
            if is_prime:
                found_primes.append(first_number)

What is slow about this solution?  What could be fixed? What can be taken out?

Exercise
^^^^^^^^

Turn the most inner loop into a second function:

.. code-block:: python
    :linenos:
    
    def check_primeness(some_number):
        # write this part; for now just defaulting to false
        return False
    
    def run(max_number):
        # create list for saving the primes
        found_primes = []
        # loop over the numbers
        for first_number in range(2, max_number+1):
        
            is_prime = check_primeness(first_number)
            if is_prime:
                found_primes.append(first_number)


Sieve of Eratosthenes
---------------------

The Sieve of Eratosthenes is an ancient way of finding prime numbers. 

The description is fairly simple:

1. Start with a list of all numbers between 2 and the max number. 
2. Loop through the numbers, starting with 2.
    - With each number, "mark" all of its multiples (for 2, it'd be 4, 6, 8, etc)
    - Continue the loop with the next largest number **not** marked. 

.. code-block:: python
    :linenos:
    
    def run(max_number):
        # create list of all numbers
        numbers = []
        for i in range(2, max_number):
            numbers.append(i)
        
        while current_number < max_number:
            
            # go through and mark 2*current_number, 3*current_number, etc
            for multiple in range(2, max_number):
                        
                new_number = current_number * multiple
                if new_number < max_number:
                    numbers[new_number] = -1
            
            # find the next "current_number"
            finding_next = True
            while finding_next:
                current_number += 1
                if numbers[current_number] != -1:
                    finding_next = False
            
        
        for i in range(2, max_number):
            if numbers[i] != -1:
                print("{} is a prime number!".format(i))
                
                
                
What parts of this are slow?  What parts are doing extra work that doesn't need to be done? 


Exercise
^^^^^^^^

I have moved the code into separate functions.  Use the fact that you can
return early to make the functions faster. 

Hint: :code:`mark_multiples` and :code:`get_next_number` can both be made faster.

Hint: Determine when the function should be over, exit at that point.


.. code-block:: python
    :linenos:

    def mark_multiples(current_number, max_number, numbers):            
        # go through and mark 2*current_number, 3*current_number, etc
        for multiple in range(2, max_number):
                    
            new_number = current_number * multiple
            if new_number < max_number:
                numbers[new_number] = -1
        

    def get_next_number(current_number, numbers): 
        # find the next "current_number"
        finding_next = True
        while finding_next:
            current_number += 1
            if numbers[current_number] != -1:
                finding_next = False

        return current_number

    def print_prime_list(numbers):
        for i in range(2, max_number):
            if numbers[i] != -1:
                print("{} is a prime number!".format(i))
        
    def run(max_number):
        # create list of all numbers
        numbers = list(range(2, max_number))
        
        while current_number < max_number:
            
            mark_multiples(current_number, max_number, numbers)

            get_next_number(current_number, numbers)
            
        print_prime_list(numbers)