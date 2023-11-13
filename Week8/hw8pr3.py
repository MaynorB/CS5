#
# hw8pr3.py
#

# Name: Maynor

import random
import time

PI = 3.14
#
# a function that throws one dart, returning true  (if it hits the circle)
#                                            false (otherwise)
#
def dart():
    """ Throws one dart between (-1,-1) and (1,1).
        Returns True if it lands in the unit circle; otherwise, False.
    """
    x = random.uniform(-1, 1)
    y = random.uniform(-1, 1)
    
    if x**2 + y**2 < 1:
        return True        # HIT (within the unit circle)
    else:
        return False       # miss (landed in one of the corners)
    

def forpi(N):
    """Throws N darts, estimating pi."""
    pi = 42    # A suitably poor initial estimate
    throws = 0  # No throws yet 
    hits = 0    # No "hits" yet  (hits ~ in the circle)
    for i in range(N):
        if(dart()):
            hits += 1
            throws += 1
        else:
            throws += 1
        pi = 4 * (hits/throws)
        print(str(hits) + " hits out of " + str(throws) + " throws so that pi is " + str(pi))
    return pi
    
def whilepi(error):
    """
    Thorws N darts until the estimate is error away from actual pi
    """
    pi = 42    # A suitably poor initial estimate
    throws = 0  # No throws yet 
    hits = 0    # No "hits" yet  (hits ~ in the circle)
    while abs(pi - PI) > error:
        if(dart()):
            hits += 1
            throws += 1
        else:
            throws += 1
        pi = 4 * (hits/throws)
        print(str(hits) + " hits out of " + str(throws) + " throws so that pi is " + str(pi))
    return throws

def forpi_np(N):
    """
    forPi without printing
    """
    pi = 42    # A suitably poor initial estimate
    throws = 0  # No throws yet 
    hits = 0    # No "hits" yet  (hits ~ in the circle)
    for i in range(N):
        if(dart()):
            hits += 1
            throws += 1
        else:
            throws += 1
        pi = 4 * (hits/throws)
    return pi

def whilepi_np(error):
    """
    whilepi without printing
    """
    pi = 42    # A suitably poor initial estimate
    throws = 0  # No throws yet 
    hits = 0    # No "hits" yet  (hits ~ in the circle)
    while pi - PI > error:
        if(dart()):
            hits += 1
            throws += 1
        else:
            throws += 1
        pi = 4 * (hits/throws)
    return throws

"""
On average, how close to 𝝅 does forpi_np(N) get when N = 1, 10, 100, 1000  ?
On average, how many throws are needed for whilepi_np(e) to get within e = 1, .1, .01, 0.001?

N=1 and e=1:
    LC = [forpi_np(1) for x in range(1000)]
    (sum(LC) / len(LC)) = 3.184
    LC = [whilepi_np(1) for x in range(1000)]
    (sum(LC) / len(LC)) = 1.793

N=10 and e=.1:
    LC = [forpi_np(10) for x in range(1000)]
    (sum(LC) / len(LC)) = 3.1391999999999856
    LC = [whilepi_np(.1) for x in range(1000)]
    (sum(LC) / len(LC)) = 33.961

N=100 and e=.01:
    LC = [forpi_np(100) for x in range(1000)]
    (sum(LC) / len(LC)) =3.1454799999999854
    LC = [whilepi_np(.01) for x in range(1000)]
    (sum(LC) / len(LC)) = 639.899

N=1000 and e=.001:
    LC = [forpi_np(1000) for x in range(1000)]
    (sum(LC) / len(LC)) =  3.1415880000000014
    LC = [whilepi_np(.001) for x in range(1000)]
    (sum(LC) / len(LC)) = 4216.824

    

    Does forpi or whilepi estimate 𝝅 more efficiently? Why?
        forpi as it does not account for how close it is

    Does forpi or whilepi estimate 𝝅 more accurately? Why?
        whilepi as it will not stop until the marigin of error is met
"""
