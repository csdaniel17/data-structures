## Big O - Determine the "Big O" for the problems below:

1. double each number in an array of n numbers.
    for n in numbers:
        ...

    * O(n) - looping through an array - every time the array increases num in size you are going to have to loop through


2. given a number between 0 to 6, return Sunday for 0, Monday for 1, Tuesday for 2, Wednesday for 3, Thursday for 4, Friday for 5, and Saturday for 6.
    for n in range(0, 6):
        if ...

    * O(1) - 6 is a constant - it does not depend on the inputs


3. find the result of multiplying each number in an array of n numbers.

    sum = 1
    for n in numbers:
        sum = sum * n

    * O(n) - looping through an array


4. calculate the multiplication table for the numbers between 0 to n.
    for x in range(n):
        for y in range(n):
            # multiply

    * O(n^2) - nested for loops


5. given an array of basketball players that are sorted by average points per game, find the player who scored exactly 10 points per game, if he exists.
    * O(log n) - binary search


6. find the player in an array whose first name is "LeBron".
    * O(n)


7. 2 arrays:
    arr1 = [1, 2, 3]
    arr2 = [2, 4, 8]

    output = []
    for x in arr1:
      for y in arr2:
        output.append(x * y)

    * O(n * m)
