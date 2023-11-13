# hw8pr1.py
# Lab 8
#
# Name:Maynor 
#

# keep this import line...
from cs5png3 import *


#
# A test function...
#
def test_fun():
    """Algorithmic image creation, one pixel at a time.
       This is a test function: it should create
       an image named test.png in the current directory.
    """
    im = PNGImage(300, 200)  # Creates an image of width 300, height 200

    # Nested loops!
    for r in range(200):     # loops over the rows with runner variable r
        for c in range(300): # loops over the columns with c
            if  c == r:   
                im.plotPoint(c, r, (255, 0, 0))
            #else:
            #    im.plotPoint(c, r, (255, 0, 0))
                
    im.saveFile()

#
# start your Lab 8 functions here:
#

def mult(c, n):
    """Mult multiplies c by the positive integer n,
       using only a loop and addition.
    """
    result = 0
    for i in range(n):
        result += c
    return result

print("mult(105, 3) should be 315 and is", mult(105, 3))

def update(c, n):
    """Update starts with z = 0 and runs z = z**2 + c
       for n times
    """
    z = 0
    for i in range(n):
        z = z ** 2
        z += c
    return z

def inMSet(c, n):
    """inMSet accepts
            c for the update step of z = z**2+c
            n, the maximum number of times to run that step.
       Then, it returns
            False as soon as abs(z) gets larger than 2.
            True if abs(z) never gets larger than 2 (for n iterations).
    """
# c = x + y*1j
    z = 0 + 0j
    for i in range(n):
        if abs(z) > 2:
            return False
        z = z ** 2
        z += c
    return True




def weWantThisPixel(col, row):
    """This function returns True if we want to show
       the pixel at col, row and False otherwise.
    """

    # if col % 10 == 0 or row % 10 == 0: it will change into  grid

    if col % 10 == 0 and row % 10 == 0:

        return True
    else:
        return False

def test():
    """This function demonstrates how
       to create and save a PNG image.
    """
    width = 300
    height = 200
    image = PNGImage(width, height)

    # Create a loop that will draw some pixels.

    for col in range(width):
        for row in range(height):
            if weWantThisPixel(col, row):
                image.plotPoint(col, row)

    # We looped through every image pixel; we now write the file.
    image.saveFile()


def scale(pix, pixMax, floatMin, floatMax):
    """scale accepts
           pix, the CURRENT pixel column (or row).
           pixMax, the total number of pixel columns.
           floatMin, the minimum floating-point value.
           floatMax, the maximum floating-point value.
       scale returns the floating-point value that
           corresponds to pix.
    """
    fraction = pix/pixMax
    distance = floatMax - floatMin
    distance *= fraction
    return floatMin + distance



NUM_ITERATIONS = 100  # of updates
XMIN = -1.2  # The smallest real coordinate value
XMAX =  -.6  # The largest real coordinate value
YMIN = -.5   # The smallest imaginary coordinate value
YMAX = -.01  # The largest imaginary coordinate value
FACTOR = 3
WIDTH = 300*FACTOR
HEIGHT = 200*FACTOR
def mset():
    """Creates a 300x200 image of the Mandelbrot set.
    """
    width = 300*1       # We can update the 1 later to enlarge the image...
    HEIGHTheight = 200*1
    image = PNGImage(WIDTH, HEIGHT)

    # Create a loop to draw some pixels

    for col in range(WIDTH):
        for row in range(HEIGHT):
            # Use scale twice:
            #   once to create the real part of c (x)
            x = scale(col, WIDTH, XMIN, XMAX)
            #   once to create the imaginary part of c (y)
            y = scale(row, HEIGHT, YMIN, YMAX)
            # THEN, create c, choose n, and test:
            c = x + y*1j
            n = 25
            if inMSet(c, NUM_ITERATIONS) == True:
                image.plotPoint(col, row,(0,0,225))
            else:
                image.plotPoint(col,row, (0, 0, 0))

    # We looped through every image pixel; we now write the file
    image.saveFile()
