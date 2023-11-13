# CS5, hw4pr1
# Filename: hw4pr1.py
# Name: 
# Problem description: Binary <-> decimal conversions

def isOdd(N):
    """
    Deternmines if N is odd
    Argument:
    N is an integer
    output is a boolean based on if N is odd
    """
    if (N % 2 == 0):
        return False
    else:
        return True


def numToBinary(N):
    """
    Converts N into binary
    Arguments:
    N is an int
    Output:
    Binary number representing N
    """
    if N == 0:
        return ''
    elif N%2 == 1:
        return   numToBinary(N//2) + '1'
    else:
        return   numToBinary(N//2) + '0'

def  binaryToNum(S):
    """
    Converts S into base 10 form
    Arguments:
    S is a binary string
    Output is a base 10 number representing S
    """
    if S == '':
        return 0

    # if the last digit is a '1'...
    elif S[-1] ==  '1':
        return (binaryToNum(S[:len(S)-1]) * 2 + 1)

    else: # last digit must be '0'
        return (binaryToNum(S[:len(S)-1]) * 2+ 0)
    
def increment(S):
    """
    Takes S and returns the next number in binary
    Input:
    S is a string representing a binary number
    Output is the next largest number in binary
    """
    if ("0" not in S):
        return "0" * len(S)
    n = binaryToNum(S)
    next = n + 1
    binary_next = numToBinary(next)
    return "0" * (len(S) - len(binary_next)) + binary_next

def count(S, n):
    if (n == 0):
        print(S)
    else:
        print(S)
        count(increment(S), n - 1)
    
def  numToTernary(N):
    """
    Converts N into Ternary
    Arguments:
    N is an int
    Output:
    Terenary number representing N
    """
    if N == 0:
        return ''
    elif N % 3 == 2:
        return   numToTernary(N//3) + '2'
    elif N % 3 == 1:
        return   numToTernary(N//3) + '1'
    else:
        return   numToTernary(N//3) + '0'
    
# 59 in Terenary is 2012, as the order will go 1,3,9,27. There is two 27 that can fit in 59, it will decrease it to 5. it is two ones and a three to make a five
 
def ternaryToNum(S):
    """
Converts S into base 10 form
Arguments:
S is a Ternary string
Output is a base 10 number representing S
    """
    if S == '':
        return 0
    elif S[-1] ==  '2':
        return (ternaryToNum(S[:len(S)-1]) * 3 + 2)
    elif S[-1] ==  '1':
        return (ternaryToNum(S[:len(S)-1]) * 3 + 1)
    else: 
        return (ternaryToNum(S[:len(S)-1]) * 3 + 0)
    
def balancedTernaryToNum(S):
    """
    Converts S into base 10 form
    Arguments:
    S is a Ternary string made up of plus and minus
    Output is a base 10 number representing S
    """
    if S == '':
        return 0
    elif S[-1] ==  '-':
        return (balancedTernaryToNum(S[:len(S)-1]) * 3 - 1)
    elif S[-1] ==  '+':
        return (balancedTernaryToNum(S[:len(S)-1]) * 3 + 1)
    else: 
        return (balancedTernaryToNum(S[:len(S)-1]) * 3 + 0)
    
def numToBalancedTernary(N):
    """
    Converts N into ternary string made up of +, - and 0
    Arguments:
    N is a num
    Output is ternary string of +, -, 0 representing N
    """
    if N == 0:
        return ''
    elif N % 3 == 2:
        return numToBalancedTernary(N//3 + 1) + '-'
    elif N % 3 == 1:
        return numToBalancedTernary(N//3) + '+'
    else:
        return numToBalancedTernary(N//3) + '0'
    