#
# hw6pr5.py -  Python!
#
#  Gold and Black:   this is "Intro to loops"! 
#
# Name: Maynor
#

import random

def fac(n):
    """Loop-based factorial function
       Argument: a nonnegative integer, n
       Return value: the factorial of n
    """
    result = 1                 # starting value - like a base case
    for x in range(1, n + 1):  # loop from 1 to n, inclusive
        result = result * x    # update the result by mult. by x
    return result              # notice this is AFTER the loop!

#
# Tests for looping factorial
#
print("fac(0) should be 1:", fac(0))
print("fac(5) should be 120:", fac(5))


def power(b,p):
    """
    Loop based power function
    Argument: non negativce integers b and p
    Return Value: base b raised to the p
    """
    result = 1
    for i in range(p):
        result *= b
    return result

#
# tests for looping power
#
print("power(2, 5): should be 32 ==", power(2, 5))
print("power(5, 2): should be 25 ==", power(5, 2))
print("power(42, 0): should be 1 ==", power(42, 0))
print("power(0, 42): should be 0 ==", power(0, 42))
print("power(0, 0): should be 1 ==", power(0, 0))

def summer(L):
    """
    Loop based function ading up values in L
    Argument: A list L filled with numbers
    Return Value: sum of all the values in L as an int 
    """
    sum = 0
    for i in range(len(L)):
        sum += L[i]
    return sum
print("")
print("summer([10,10,10,2,10]): should be 42 ==", summer([10,10,10,2,10]))
print("summer([10,10,10,2]): should be 32 ==", summer([10,10,10,2]))
print("summer([11, 11]): should be 22 ==", summer([11,11]))
print("summer([47]): should be 47 ==", summer([47]))
print("summer([ ]): should be 0 ==", summer([ ]))

def summedOdds(L):
    """
    Loop based function adding up the odd numbers
    Argument: A list L filled with numbers
    Return Value: Sum of all odd values in L
    """
    sum = 0
    for i in range(len(L)):
        if(L[i] % 2 == 1):
            sum += L[i]
    return sum

# tests!
print("")
print( "summedOdds([4, 5, 6])      should be 5 :",  summedOdds([4, 5, 6]) )   
print( "summedOdds(range(3, 10))   should be 24 :",  summedOdds(range(3, 10)) )


def summedExcept(exc, L):
    """
    Loop based function adduping up values except for a specific number
    Argument: exc is a number to be exempt from the sum
    L is a list of numbers
    Return Value: Sum of all values except for exc
    """
    sum = 0
    for i in range(len(L)):
        if(L[i] != exc):
            sum += L[i]
    return sum



# tests!
print("")
print( "summedExcept(5, [4, 5, 6])      should be 10 :",  summedExcept(5, [4, 5, 6]) )   
print( "summedExcept(5, [5, 5, 5])      should be 0 :",  summedExcept(5, [5, 5, 5]) ) 



def summedUpto(exc, L):
    """
    Loop based function that adds up all values up to a certain value
    Argument: Exc is an integer that will stop the loop
    L is a list of values
    Return Value: Sum of all values up to exc in the list
    """
    sum = 0
    for i in range(len(L)):
        if(L[i] == exc):
            break
        sum += L[i]
    return sum

print("")
print( "summedUpto(5, [4, 5, 6])      should be 4 :",  summedUpto(5, [4, 5, 6]) )   
print( "summedUpto(5, [4, 6, 5])      should be 10 :",  summedUpto(5, [4, 6, 5]) ) 
print( "summedUpto(5, [4, 6, 32])     should be 42 :",  summedUpto(5, [4, 6, 32]) ) 


def countGuesses(hidden):
    """Use a while loop to guess "hidden", from 0 to 99.
       Argument: hidden, a "hidden" integer from 0 to 99.
       Result: the number of guesses needed to guess hidden.
    """
    guess = random.choice(range(0, 100))     # 0 to 99, inclusive
    numguesses = 1                           # We just made one guess, above
    while guess != hidden:
        guess = random.choice(range(0, 100)) # Guess again!
        numguesses += 1                      # Add one to our number of guesses
    return numguesses

def unique(L):
    """
    This should be your uniqueness-tester, written for Lab6
    Usually, it uses the recursive pattern:
    """

    if L == []:
        return True
    elif  L[0] in L[1:] :
        return False
    else:
        result = unique(L[1:])
        return result
    

def untilARepeat(high):
    """
    Keeps guessing numbers until a repeat occurs 
    Argument: an int named high, setting the max range of guess
    output: the number of guesses till a repeat occured
    """
    L = []
    guess = random.choice(range(0, high))     # 0 to 99, inclusive
    numguesses = 1
    L = L + [guess]
    while unique(L):
        guess = random.choice(range(0, 100)) # Guess again!
        numguesses += 1                      # Add one to our number of guesses
        L = L + [guess]
    return numguesses

"""
Here's what I got when I analyzed 10,000 calls of untilARepeat(365):
The average "birthday room" size: 13.9704
The largest "birthday room": 40
The smallest "birthday room": 2
Did any have exactly 42 people?: False
How many times did rooms have exactly 2 people?: 30
Did any have exactly 1 person?: False
Did any have exactly 142 people?: False
"""


def rs():
    """One random step"""
    return random.choice([-1, 1])

def rwalk(radius):
    """Random walk between -radius and +radius  (starting at 0 by default)"""
    totalsteps = 0          # Starting value of totalsteps (_not_ final value!)
    start = 0               # Start location (_not_ the total # of steps)

    while True:             # Run "forever" (really, until a return or break)
        if start == -radius or start == radius:   
            return totalsteps # Phew!  Return totalsteps (stops the while loop)

        start = start + rs()
        totalsteps += 1     # addn totalsteps 1 (for all who miss Hmmm :-)


    # it can never get here!
"""
First, I created an LC with 10,000 radius-5 random-walk trials, using this line:

LC = [rwalk(5) for x in range(10000)]

Out of those 10,000 radius-5 trials, the average number of steps
(sum(LC) / len(LC)) needed to reach the boundary was:

++++++++++++
+ 25.1472  +
++++++++++++

Out of those 100,000 radius-5 trials, the average number of steps
++++++++++++
+24.9337   +
++++++++++++

Out of those 1,000,000 radius-5 trials, the average number of steps
++++++++++++
+ 24.98553 +
++++++++++++

Next I measure the time it took to compute 10,000 times, 100,000 times, 1,000,000 times.

10,000 took 429 ms
100,000 took 4.39 s
1,000,000 took 43.4 s

Out of those 10,000 radius-6 trials, the average number of steps
++++++++++++
+ 35.7938  +
++++++++++++

Out of those 10,000 radius-7 trials, the average number of steps
++++++++++++
+ 48.8442  +
++++++++++++

Out of those 10,000 radius-10 trials, the average number of steps
++++++++++++
+ 99.2602  +
++++++++++++



If you set a random walker in the middle of an interval with radius radius, on 
average, how many steps would you expect the random walker to take before reaching the edge of the interval? 
The radius on average

If you set a random walker walking... how far away from the starting point would you expect our walker to be after numsteps steps?
    half of numsteps 
"""