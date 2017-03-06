Week 8: Problem Solving and Searching
=====================================


Summary
-------

Today we talked about how trees can be used to solve problems!  As you click
through the tutorials below, you will see how you can think about each node
in a tree as being a setting of variables and each child is 1-step beyond the state.

For the take home work, you should work on the project work below. You don't have
to have a working system by next week, but you should have a :code:`class` which
can represent the problem (in the same way we represented Missionaries and Cannibals in the tutorial).
It should also have the set of possible moves, and a function which can generate
the next legal states. 

Also, don't forget, that there is a Binary Search Tree exercise on repl.it. 
It's ok if you don't get it done, but please look at it and ask me questions
if there's anything you don't know. 


Tutorial Pages
^^^^^^^^^^^^^^

- :doc:`Part 1: Introduction <exercises/week8/part1_intro>`
- :doc:`Part 2: State <exercises/week8/part2_state>`
- :doc:`Part 3: Transitions <exercises/week8/part3_transitions>`
- :doc:`Part 4: Searching <exercises/week8/part4_searching>`

Project Work
------------

During the next week, you should be thinking about what kinds of problems
you could solve with these techniques.  The properties the problem should have
will be:

1. Can be represented by a couple of variables
2. Involves a series of steps to get to a solution


Here are some options to get you thinking about it:

1. Towers of Hanoi
    + There are pegs and a certain number of disks
    + The goal is to have the tree be the sequences of moves that you can do
    to solve the game
2. Tic-Tac-Toe
    + The blank game board has 9 open spaces
    + Each move is a selection of a square and a mark
    + The top root has 9 children, the second layer each has 8, and so on
3. Nim or `Chomp <https://en.wikipedia.org/wiki/Chomp>`_
    + These are games where you have a set amount of things---in Nim, it's stones or sticks, 
    and in Chomp it is pieces of candy.  
    + You and another person are playing the game
    + Each person takes turns taking 1, 2, or 3 things
    + Whoever is forced to take the last thing loses
    + So, the problem solving programming for this problem would be to find
    the series of selections you can use to win!

You can also look through these links and see if there is something you'd
like to try:

1. `River Crossing Puzzles <https://en.wikipedia.org/wiki/River_crossing_puzzle>`_
2. `Mathematical Games <https://en.wikipedia.org/wiki/Mathematical_game>`
