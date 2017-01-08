Week 3: Recursion
=================

Summary
^^^^^^^

We had a snow day!  We were going to start learning about recursion, but we will push it into next week's lecture.  It would be good if you did the homework (listed below) before then.  Also, you should play with the turtle below and make your own recursive turtle.

Homework
^^^^^^^^

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

Extra Resources
^^^^^^^^^^^^^^^

You will have the best luck if you run the following trinket full screen.

.. raw:: html

    <iframe src="https://trinket.io/embed/python/0e731cdd38" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

.. raw:: html

   <iframe src="https://trinket.io/embed/python/6c939d8315" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

.. raw:: html

   <iframe src="https://trinket.io/embed/python/b175bb94fc" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

.. raw:: html

   <iframe src="https://trinket.io/embed/python/814e6138f2" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

.. raw:: html

   <iframe src="https://trinket.io/embed/python/1c38aa544b" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

Lecture Slides
^^^^^^^^^^^^^^

.. raw:: html

    <iframe src="https://docs.google.com/presentation/d/156lDf0BKfMeVD6-LCg2w53AIj4pwlK11OMBl8dx2-9E/embed?start=false&loop=false&delayms=30000" frameborder="0" width="480" height="299" allowfullscreen="true" mozallowfullscreen="true" webkitallowfullscreen="true"></iframe>
