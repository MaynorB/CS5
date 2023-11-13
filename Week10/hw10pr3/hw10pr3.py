# coding: utf-8
#
# The top line, above, is important -- it ensures that Python will be
# able to use this file even if you paste in text with fancy Unicode
# characters that aren't part of normal ASCII.
#
# For another example of such a file, see
# https://www.cl.cam.ac.uk/~mgk25/ucs/examples/UTF-8-demo.txt
#
# OK! Now we're ready for hw10pr3.py ...
#
# Name: Maynor
#

#
# First, some helper/example functions for files + text ...
#
# To make the examples work, you should have the text file named "a.txt"
# in the same directory as this .py file!
#
# If you _don't_ have "a.txt", create it.  Here are its contents:
"""
I like poptarts and 42 and spam.
Will I get spam and poptarts for
the holidays? I like spam poptarts!
"""
import random


def get_text(filename):
    """Opens a file named 'filename', reads
       it, and returns its contents (as one big string).

       Example:
          In [1]: get_text("a.txt")
          Out[1]: 'I like poptarts and 42 and spam.\nWill I get spam and poptarts for\nthe holidays? I like spam poptarts!\n\n\n\n'

          In [1]: len(get_text("a.txt"))
          Out[1]: 102  # Well, _around_ 102, depending how many \n's you have at the end of a.txt.
                       # Note that '\n' is ONE character:   len('\n') == 1
    """
    #
    # First we have to open the file (just like opening a book to read it).
    # We assume the "utf-8" encoding, which accepts more characters than plain ASCII
    #
    # Other common codings welcome, e.g., utf-16 or latin1
    # See [docs.python.org/3.8/library/codecs.html#standard-encodings]
    # for the full list (it's big!).
    #
    f = open(filename, encoding = 'utf-8')

    #
    # Read the contents of the file into a string named "text", close
    # the file, and return the string.
    #
    text = f.read()
    f.close()
    return text

def word_count(text):
    """Word-counting function.
       Counts the number of "words" (space-separated sequences) in
       the string "text".

       Examples:
          In [1]: word_count('This has four words!')
          Out[1]: 4

          In [1]: word_count(get_text("a.txt"))
          Out[1]: 20                 # If it's the a.txt file above
    """
    #
    # The text of the file is one long string.  Use "split" to get words!
    #
    LoW = text.split()    # We could use text.split("\n") to get _lines_.

    #
    # LoW is a List of Words, so its length is the word count.
    #
    result = len(LoW)

    # Comment out, as needed...
    if result < 100:
        print("LoW[0:result] is", LoW[0:result])  # For sanity checking...
    else:
        print("LoW[0:100] is", LoW[0:100])        # without going too far...

    return result



# Use the string library to implement remove_punctuation:
import string    # See https://docs.python.org/3/library/string.html
                 # Note: str is different: docs.python.org/3/library/stdtypes.html#textseq

def remove_punctuation(text):
    """Accepts a string named "text".  Returns an equivalent string, _but_
       with all non-(English)-text characters removed (keeps only
       letters + digits).

       + Vary to suit the language at hand!

       Examples:
          In [1]: remove_punctuation("42_isn't_.!?41.9bar")
          Out[1]: '42isnt419bar'

          In [2]: remove_punctuation(get_text("a.txt"))
          Out[2]: 'Ilikepoptartsand42andspamWillIgetspamandpoptartsfortheholidaysIlikespampoptarts' # (Not so useful w/o spaces!)
    """
    new_text = ''
    CHARS_TO_KEEP = string.ascii_letters + string.digits # + string.whitespace + string.punctuation
    for c in text:  # c is each character
        # Use the Python string library
        if c in CHARS_TO_KEEP:
            new_text += c
        else:
            pass # don't include it  [WARNING: as written, this removes spaces!]

    # We're finished!
    return new_text


def vocab_count(text):
    """Returns a dictionary of (punctuationless, lower-cased) words in "text".

       + Removes everything not in string.ascii_letters (via the function
         above).
       + Also, lower-cases everything (alter to suit your taste or
         application!).
       + Builds and returns a dictionary of how many times each word occurs.

       Examples:
          In [1]: vocab_count("Spam, spam, I love spam!")
          There are 5 words.
          There are 3 *distinct* words in the text.

          Out[1]: {'spam': 3, 'i': 1, 'love': 1}


          In [2]: vocab_count(get_text("a.txt"))
          There are 20 words.
          There are 11 *distinct* words in the text.

          Out[2]:
                    {'i': 3,
                    'like': 2,
                    'poptarts': 3,
                    'and': 3,
                    '42': 1,
                    'spam': 3,
                    'will': 1,
                    'get': 1,
                    'for': 1,
                    'the': 1,
                    'holidays': 1}
    """
    LoW = text.split()
    print("There are", len(LoW), "words.")  # For info - comment out if you like

    d = {}
    for word in LoW:
        word = remove_punctuation(word)  # Remove punctuation!
        word = word.lower()   # Make lower case!

        if word not in d:     # If it's not already in the dictionary, d
            d[word] = 1       # Set count to 1  (the VALUE is the count, here)
        else:                 # ..or if it IS already in the dictionary, d
            d[word] += 1      # ..add 1 to count (again, the VALUE is the count)

    print("There are", len(d), "*distinct* words in the text.\n")
    return d            # This way we can _use_ or look up the keys in d...




"""
[a] What was in the file you analyzed?   -->    Music Lyrics to Problematic by boywitheuke
    + Feel free to include it (up to you).

[b] How many words did it have?  -->     424
    Use word_count.

[c] How many characters did it have?  -->       2233

    Note: there's no function for this, but len(get_text("a.txt")) will do it!


[d] How many _distinct_ words did it have?  -->   158
    Use vocab_count.
    Adapt as you see fit...

[e] What are three words that appeared unusually often for this text?  -->  Light, Wish, Back
    - ...relative to a generic distribution of "all text"

    For example, it's _not_ unusual if "the" or "a" are the
    most common words in an English text.

    Mainly because the song is about leaving it behind 


[f] Other thoughts/insights?!

    I have no braincells no more
"""

#
# Now, to the Markov modeling (createDictionary) and Markov text
# generation (generateText)
#
# Be sure to create your 500-word "CS-Essay,"" with:
#    In [1]: d = createDictionary(get_text("yourfile.txt"))
#    In [2]: generateText(d, 500)       # Then copy the "essay" below ...
#

#
# Function #1  (createDictionary)
#
def createDictionary(text):
    """ 
    Takes a text, converts into list of words, then finally returns a dictionary that is a Markov model  of the words
    """
    LoW = text.split()

    d = {}
    pw = '$'   # pw indicates previous word

    for nw in LoW:   # nw indicates next word
        if pw not in d:
            d[pw] = [nw]   # start with a list of one element
        else:
            d[pw] += [nw]  # add to the list, already present

        pw = nw  # pw is the "new" previous word

    # Here, check for whether that new previous word, pw, ends in 
    # punctuation -- if it _does_ then set pw to be '$'
    # that way, it will be back at the start of a new sentence!
        if pw[-1] in '.!?':
            pw = '$'

    return d

#
# Function #2   (generateText)
#
def generateText(d, N):
    """
    Generates a string of text of N words using d
    """
    print()  # start by printing a newline
    key = '$'

    for i in range(N):
        next_word = random.choice(d[key])  # Next word -- will be replaced (alas)
        key = next_word
        # Here's how to print so that things don't always start on the next line
        # Using end = ' ' stops it going to the next line
        print(next_word, end = ' ')
        if next_word[-1] in '.!?':
            key = '$'

    print()                  # Final print, newline


#
# Your 500-or-so-word "CS Essay" (paste into the triple-quoted strings below):
# I am using the 'Problamatic' by Boywithuke to make a song title "Problamatic but the computer decides my fate"
#
"""
I wasn't problematic I'm looking back at times we had The one to panic, panic 
I'm trying not to pull me out If I see behind her eyes 
Yes, I wish I wish I wasn't problematic 
I'm burning bridges into ashes Light them up like matches How could you understand it, stand it? 
I let me free Light my noose and things we did and set me be 
Take my home I thought you could you in my noose and things we had The one to panic, panic 
I'm semi-automatic I'm looking back at times we could you were better off alone 
Without you in my home I were better than that maybe you understand it, stand it? 
I wish I wasn't problematic I'm looking back at times we did you understand it, stand it? 
Watch me as I wasn't problematic I'm burning bridges into ashes
Light my noose and things we had The things we could you understand it, stand it? 
I wish I wish I see behind her cadence yesterday She began making mistakes 
Then, I wasn't problematic I'm semi-automatic I'm trying not to pull me hear the choir full of liars Tell 'em I wish I want peace 
I wish I wasn't problematic I'm trying not to panic, panic I'm looking back into ashes 
Light them up like matches How could you were ever stuck inside a dream I'm semi-automatic 
I'm trying not to panic, panic I'm burning bridges into ashes Light my heart Let me higher than I want peace 
I know that maybe you stab me free Light my home on my heart Let me out If I know that maybe you in my knees 
Beggin' for the harm in my knees Beggin' for thinking we did you back at times we did and things we could you love me as I want peace 
I know that I wasn't problematic I'm burning bridges into ashes Light them up like matches 
How could you in my home on fire Take my noose and set me be The one to panic, panic 
I'm burning bridges into ashes Light my knees Beggin' for the harm in asking: Why? 
I wish I wish I wasn't problematic I'm trying not to panic, panic I'm burning bridges into my arms 
Fool for another Her actions turning reckless She didn't even noticed That she called me in my home 
I wish I know that maybe you love me out If I wasn't problematic I'm semi-automatic I'm better off alone 
Without you could you that you're not to pull me in asking: Why? I want peace I want peace I were ever stuck inside a dream 
I'm semi-automatic I'm semi-automatic I'm trying not tired Where the choir full of liars Tell 'em 
I wish I wish I wasn't problematic I'm semi-automatic I'm trying not to panic, panic I'm trying not tired 
Where the choir full of liars Tell 'em I thought you understand it, stand it? I wasn't problematic I'm trying not to 
"""
#Coming out: Never