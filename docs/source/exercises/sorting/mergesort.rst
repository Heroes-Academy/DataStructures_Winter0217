Merge Sort
==========

A top-down merge sort will take a list and do the following procedure:

1. Check if the list is larger than length 1
2. If it is, split at the best halfway point
3. Call itself on each half. 
4. Go through the halves, taking the smallest one each time, and add it
to the result. 

Bottom-up merge sort:

1. assume everything is already list size 1. 
2. queue everything up.
3. merge the top two. add back to queue. 

