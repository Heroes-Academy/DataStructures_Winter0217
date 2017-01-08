Week 6: Trees
=============


Summary
-------

We covered trees.  We started with a basic implementation, discussed how they worked.
Specifically, we covered the standard tree terminology, and how they might get programmed.  Then, we went through how they can be traversed and the difference in the types of searches through a tree.

Homework
--------

You will be augmenting the code we had in class:

.. code-block:: python
    :linenos:

    class Tree:
        def __init__(self, root, left=None, right=None):
            self.left = left
            self.right = right
            self.value = root

You should write methods for it to do the following:
1. Insert a number, following the binary search tree property
  - Every left child should be smaller than its parent
  - Every right child should be larger than its parent
2. Search for a number with a tree that is full of the previous property
  - Check if the current value is what you are looking for
  - If it is not, then move onto the left or right child, depending on whether the number you are looking for is larger or smaller than the parent.
  - You can write this as a non-recursive function if you'd like.



Extra Resources
---------------

Online Books
^^^^^^^^^^^^
1. `Think like a Computer Scientist <https://www.cs.swarthmore.edu/courses/cs21book/build/ch21.html>`_

Videos
^^^^^^
1. `Harvard CS50 <https://www.youtube.com/watch?v=mFptHjTT3l8>`_

Lecture Slides
--------------

.. raw:: html

    <iframe src="https://docs.google.com/presentation/d/1jlgu-tTYEosg69xBVv22PHhyZJ6xnOURyzhoH4PIvZY/embed?start=false&loop=false&delayms=30000" frameborder="0" width="480" height="299" allowfullscreen="true" mozallowfullscreen="true" webkitallowfullscreen="true"></iframe>
