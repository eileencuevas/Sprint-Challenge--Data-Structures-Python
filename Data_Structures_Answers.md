Add your answers to the questions below.

1. What is the runtime complexity of your ring buffer's `append` method?
   O (c), as accessing items in an array has a constant runtime and assigning things has a constant runtime.

2. What is the space complexity of your ring buffer's `append` function?
   O (c), as it uses already-existing variables to accomplish what it is intended to do.

3. What is the runtime complexity of your ring buffer's `get` method?
   O (n), as it loops through an entire array once in order to build the array we return in this function.

4. What is the space complexity of your ring buffer's `get` method?
   O (n), as the size of the new array may be less than the size of the storage in the class, but is entirely dependent of the size of the class's storage as it can grow up to the size of the class's storage.

5. What is the runtime complexity of the provided code in `names.py`?
   O (n ^ 2), as we're nesting a loop in a loop and have to go through each item in both arrays to see if they match a certain criteria.

6. What is the space complexity of the provided code in `names.py`?
   O (2n log n), or just O (n log n), as we are building two new arrays entirely dependent on the sizes of the inputs given to us, and one duplicates array which will be half the size of the combined sizes of the inputs given to us

7. What is the runtime complexity of your optimized code in `names.py`?
   O (n). Making the dictionary used in this function involves looping over names_1, which by itself has a runtime of O (n) but as we're only setting up keys to variables the actions taken by the loop is constant, so the overall runtime stays O (n) for that portion. Next, we loop through names_2 which has a runtime of O (n) and the actions taken in that loop have a constant runtime (checking if something is in a dictionary is fast), making that sequence O (n) overall. O (n) + O (n) is just O (2n), which we can shorten to O (n).

8. What is the space complexity of your optimized code in `names.py`?
   O (n log n), as the duplicates array's size would be, at max, half the total amount of names provided.
