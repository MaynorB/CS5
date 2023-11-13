# CS5, Lab1 part 2
# Filename: hw1pr2.py
# Name: Maynor Bac-Itzep
# Problem description: First few functions!


def dbl(x):
    """Result: dbl returns twice its argument
       Argument x: a number (int or float)
       Spam is great, and dbl("spam") is better!
    """
    return 2*x

#Problem 1
def sq(x):
    """Result: sq returns x squared
    Argument x: a number (int/float)
    Strings may vary"""
    
    return x * x

#Problem 2
def interp(low, hi, fraction):
   """Returns the steps of fraction from low to high
   Argument low: the left part of the range
   Argument hi: the right part
   fraction: the step of the range from low to hi
   I don't know how to explain, so just...waffle
   """
   range = hi - low
   step = range * fraction
   finalResult = step + low
   return finalResult
#This was easier than expected

#Problem 3
def checkends(s):
    """Checks if first and last letter are the same
    Argument s: A string
    Beans, that is the question
    """
    if s[0] == s[len(s) - 1]:
        return True
    else:
        return False
    
def has42(d):
    """
   Checks if 42 is in dictionary d
    Argument d: a dictionary
   I have no idea if the last line is actually useful...oh well
    """
    if 42 in d:
        return True
    else:
        return False

def  hasKey(k,d):
    """
   Checks if k is in key d
   Arguemnt k: a key
   Argument d: a dictionary
   Do grutors enjoy reading? Or do they just lock in rooms coding? Will I be like that? I think it'll be funny..NOT
   """
    if k in d:
        return True
    else:
        return False
    
def flipside(s):
    """
    returns a string that the first and last half are swapped
    Argument S: the string to be swapped
    I want iced coffee
    """
    x = len(s)//2
    firstH = s[0:x]
    secondH = s[x:]
    return secondH + firstH

def convertFromSeconds(s):
    """
    returns a list of seconds converted into total days, hours, minutes and seconds left
    Argument s: An int 
    Too many dayz
    """
    days = s // (24*60*60)  # Number of days
    s = s % (24*60*60)      # The leftover
    hours = s // (60 * 60)
    s = s % (60 * 60)      # The leftover
    minutes = s // (60)
    s %= 60
    seconds = s
    return [days, hours, minutes, seconds]
