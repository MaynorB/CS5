# CS5 Gold, Lab 3
# Filename: hw3pr1.py
# Name:Maynor 
# Problem description: Lab 3 problem, "Sounds Good!"

import time
import random
import math
import csaudio
from csaudio import *
import wave
wave.big_endian = 0  # if you are having trouble, try commenting out this line...



# a function to get started with a reminder
# about list comprehensions...
def three_ize(L):
    """three_ize is the motto of the green CS 5 alien.
       It's also a function that accepts a list and
       returns a list of elements each three times as large.
    """
    # this is an example of a list comprehension
    LC = [3 * x for x in L]
    return LC



# Function to write #1:  scale
def scale(L, s):
    """
        Input L: a list to be scaled by s
        Int s: an integer to scale L
        output: List L scaled by s
    """
    LC = [s * x for x in L]
    return LC






# here is an example of a different method
# for writing the three_ize function:
def three_ize_by_index(L):
    """three_ize_by_index has the same behavior as three_ize
       but it uses the INDEX of each element, instead of
       using the elements themselves -- this is much more flexible!
    """
    # we get the length of L first, in order to use it in range:
    N = len(L)
    LC = [3 * L[i] for i in range(N)]
    return LC



# Function to write #2:  add_2
def add_2(L, M):
    """
    List L: to be added to elements of list M
    List M: to be added to elements of list L
    Output: a list which each element added with length of the shorter list
    """
    N = min(len(L), len(M))  # N is the min length!
    LC = [L[i] + M[i] for i in range(N)]
    return LC




# Function to write #3:  add_3
def add_3(L,M,P):
    """
    List L: to be added to elements of list M and P
    List M: to be added to elements of list L and P
    List P: to be added to elements of List M and L
    Output: a list which each element added with length of the shorter list
    """
    N = min(len(L), len(M), len(P))  # N is the min length!
    LC = [L[i] + M[i] + P[i] for i in range(N)]
    return LC





# Function to write #4:  add_scale_2
def add_scale_2(L, M, L_scale, M_scale):
    """
    L: a list of ints
    M: a list of ints
    L_scale: int to scale L
    M_scale: int to scale M
    Output: A list of length of the shorter list of L/M where first scaled then added togther
    """
    m_scaled = scale(M, M_scale)
    l_scaled = scale(L, L_scale)
    N = min(len(m_scaled), len(l_scaled))
    LC = [m_scaled[i] + l_scaled[i] for i in range(N)]
    return LC






# Helper function:  randomize

def randomize(x, chance_of_replacing):
    """randomize accepts an original value, x
       and a fraction named chance_of_replacing.

       With the "chance_of_replacing" chance, it
       should return a random float from -32767 to 32767.

       Otherwise, it should return x (not replacing it).
    """
    r = random.uniform(0, 1)
    if r < chance_of_replacing:
        return random.uniform(-32768, 32767)
    else:
        return x






# Function to write #5:  replace_some
def replace_some(L, chance_of_replacing):
    """
    L: a list
    chance_of_replacing: a float value that determines the chance of a value being replaced
    output: a list that has elements changed or not
    """
    LC = [randomize(x, chance_of_replacing) for x in L]
    return LC




#
# below are functions that relate to sound-processing ...
#


# a function to make sure everything is working
def test():
    """A test function that plays swfaith.wav
       You'll need swfaith.wav in this folder.
    """
    play('swfaith.wav')


# The example changeSpeed function
def changeSpeed(filename, newsr):
    """changeSpeed allows the user to change an audio file's speed.
       Arguments: filename, the name of the original file
                  newsr, the new sampling rate in samples per second
       Result: no return value, but
               this creates the sound file 'out.wav'
               and plays it
    """
    print("Playing the original sound...")
    play(filename)

    samps, sr = readwav(filename)   # get samps and sr from the file!

    print("The first 10 sound-pressure samples are\n", samps[:10])
    print("The number of samples per second is", sr)

    # we don't really need this line, but for consistency...
    newsr = newsr             # from the input! (not needed, a reminder!) 
    newsamps = samps          # same samples as before
    write_wav([newsamps, newsr], "out.wav") # write data to out.wav
    print("\nPlaying new sound...")
    play('out.wav')   # play the new file, 'out.wav'



def flipflop(filename):
    """flipflop swaps the halves of an audio file
       Argument: filename, the name of the original file
       Result: no return value, but
               this creates the sound file 'out.wav'
               and plays it
    """
    print("Playing the original sound...")
    play(filename)

    samps, sr = readwav(filename)   # get samps and sr from the file!

    print("The first 10 sound-pressure samples are\n", samps[:10])
    print("The number of samples per second is", sr)

    print("Computing new sound...")
    # this gets the midpoint and calls it x
    x = len(samps)//2
    newsamps = samps[x:] + samps[:x]
    newsr = sr               # same sr as before

    write_wav([newsamps, newsr], "out.wav") # write data to out.wav
    print("\nPlaying new sound...")
    play('out.wav')   # play the new file, 'out.wav'




# Sound function to write #1:  reverse
def reverse(filename):
    """
    reverse the file
       Argument: filename, the name of the original file
       Result: no return value, but
               this creates the sound file 'out.wav'
               and plays it
    """
    print("Playing the original sound...")
    play(filename)

    samps, sr = readwav(filename)   # get samps and sr from the file!

    print("The first 10 sound-pressure samples are\n", samps[:10])
    print("The number of samples per second is", sr)

    print("Computing new sound...")

    x = len(samps)//2
    newsamps = samps[::-1]
    newsr = sr               # same sr as before

    write_wav([newsamps, newsr], "out.wav") # write data to out.wav
    print("\nPlaying new sound...")
    play('out.wav')   # play the new file, 'out.wav'




# Sound function to write #2:  volume
def volume(filename, scale_factor):
    """
    Lowers the volume of the sound
    Arguments: filename, the name of the file
                scale_factor, scales the volume for the file
    Result: plays a file where volume is scaled 
    
    """
    print("Playing the original sound...")
    play(filename)

    samps, sr = readwav(filename)   # get samps and sr from the file!

    print("The first 10 sound-pressure samples are\n", samps[:10])
    print("The number of samples per second is", sr)

    print("Computing new sound...")

    newsamps = scale(samps , scale_factor)
    newsr = sr               

    write_wav([newsamps, newsr], "out.wav") # write data to out.wav
    print("\nPlaying new sound...")
    play('out.wav')   # play the new file, 'out.wav'





# Sound function to write #3:  static
def static(filename, probability_of_static):
    """
    Output samples have a chance of being replaced with stattc
    Arguments: filename is the file's name
                probability_of_static, chance of being replaced
    """
    print("Playing the original sound...")
    play(filename)

    samps, sr = readwav(filename)   # get samps and sr from the file!

    print("The first 10 sound-pressure samples are\n", samps[:10])
    print("The number of samples per second is", sr)

    print("Computing new sound...")

    newsamps = [randomize(x, probability_of_static) for x in samps]
    newsr = sr               

    write_wav([newsamps, newsr], "out.wav") # write data to out.wav
    print("\nPlaying new sound...")
    play('out.wav')   # play the new file, 'out.wav'


# Sound function to write #4:  overlay
def overlay(filename1, filename2):
    """
    Overlays the two file given
    filename1: the first file
    filename2: the second file
    """
    print("Playing the original sound...")
    play(filename1)
    print("Playing second one")
    play(filename2)
    samps1, sr1 = readwav(filename1)   # get samps and sr from the file!
    samps2, sr2 = readwav(filename2)

    print("1)The first 10 sound-pressure samples are\n", samps1[:10])
    print("2)The first 10 sound-pressure samples are\n", samps2[:10])

    print("#1 The number of samples per second is", sr1)
    print("#2 The number of samples per second is", sr2)


    print("Computing new sound...")

    newsamps = add_scale_2(samps1, samps2, 0.5, 0.5)
    newsr = sr1          

    write_wav([newsamps, newsr], "out.wav") # write data to out.wav
    print("\nPlaying new sound...")
    play('out.wav')   # play the new file, 'out.wav'





# Sound function to write #5:  echo
def echo(filename, time_delay):
    """
    Outputs an echo of filename based on time_delay
    arguments:
    filename; just a the file name
    time_delay: how long the echo waits before playing
    """
    print("Playing the original sound...")
    play(filename)

    samps, sr = readwav(filename)   # get samps and sr from the file!

    print("The first 10 sound-pressure samples are\n", samps[:10])
    print("The number of samples per second is", sr)

    print("Computing new sound...")
    samps2 = [0]*int((sr*time_delay)) + samps
    newsamps = add_scale_2(samps, samps2, 0.5, 0.5)    
    newsr = sr               

    write_wav([newsamps, newsr], "out.wav") # write data to out.wav
    print("\nPlaying new sound...")
    play('out.wav')   # play the new file, 'out.wav'






# Helper function for generating pure tones
def gen_pure_tone(freq, seconds):
    """pure_tone returns the y-values of a cosine wave
       whose frequency is freq Hertz.
       It returns nsamples values, taken once every 1/44100 of a second.
       Thus, the sampling rate is 44100 hertz.
       0.5 second (22050 samples) is probably enough.
    """
    # we get to pick our own sampling rate, sr
    sr = 22050
    # how many data samples to create
    nsamples = int(seconds*sr) # rounds down
    # our frequency-scaling coefficient, f
    f = 2*math.pi/sr   # converts from samples to Hz
    # our amplitude-scaling coefficient, a
    a = 32767.0
    
    # now, create the sound!
    samps = [a*math.sin(f*n*freq) for n in range(nsamples)]
    sr = sr   # not needed, but a reminder
    return [samps,sr]


def pure_tone(freq, time_in_seconds):
    """Generates and plays a pure tone of the given frequence."""
    print("Generating tone...")
    samps, sr = gen_pure_tone(freq, time_in_seconds)

    print("The first 10 sound-pressure samples are\n", samps[:10])
    print("The number of samples per second is", sr)

    print("Writing out the sound data...")
    write_wav([samps, sr], "out.wav") # write data to out.wav

    print("Playing new sound...")
    play('out.wav')




# Sound function to write #6:  chord

def chord(f1, f2, f3, time_in_seconds):
    """
    Plays a chord 
    f1: int for frequency of first note
    f2: int for frequency of second note
    f3: int for frequency of third note
    time_in_seconds: amount of time played

    """
    samps1, sr1 = gen_pure_tone(f1, time_in_seconds)
    samps2, sr2 = gen_pure_tone(f2, time_in_seconds)
    samps3, sr3 = gen_pure_tone(f3, time_in_seconds)

    newsamps= add_scale_3(samps1, samps2, samps3, 0.5, 0.5, 0.5)
    newsr= (sr1 + sr2 + sr3) / 3

    new_sound_data = [newsamps, newsr]

    print("Writing out the new sound data...")
    write_wav(new_sound_data, "out.wav") # write data to out.wav

    print("Playing new sound...")
    return play('out.wav')


def add_scale_3(L, M, P ,L_scale, M_scale, P_scale):
    """
    L: a list of ints
    M: a list of ints
    P: a list of ints
    L_scale: int to scale L
    M_scale: int to scale M
    P_scale: int to scale P
    Output: A list of length of the shorter list of L/M/P where first scaled then added togther
    """
    m_scaled = scale(M, M_scale)
    l_scaled = scale(L, L_scale)
    p_scaled = scale(P, P_scale)
    N = min(len(m_scaled), len(l_scaled), len(p_scaled))
    LC = [m_scaled[i] + l_scaled[i] + p_scaled[i] for i in range(N)]
    return LC