
Take Home Exercises
-------------------

Read through the lecture in the slides below.  Recursive functions are functions which
have two cases: a base case and the recursive case.  Consider the following:

.. code-block:: python
   :linenos:

    def recursive_add(x):
        if x == 1:
            return 1
        else:
            return 1 + recursive_add(x-1)


This is a simple and silly example, but it illustrates the point.

Your homework is to write a function like this for the fibonacci series and for factorials:
  - Recall that each fibonacci is the sum of the two before it.  It starts out as 0, 1, 1, 2, 3, 5, etc.  Write a function for recursively computing the nth fibonacci.  Fo
  - Recall that a factorial (written n!) is n * (n-1) * (n-2) * ... * 1.  Write a recursive function that computes this. Hint: it is similar to the adding.

For a bonus, there is a `recursion section at hackerrank under the Functional Programming section <https://www.hackerrank.com/domains/fp/recursion>`_.

