#
# hw3pr2.py - algorithms and use-it-or-lose-it
#

NEXT_CHAR = { "a": "b", "A": "B",
              "b": "c", "B": "C",
              "c": "d", "C": "D",
              "d": "e", "D": "E",
              "e": "f", "E": "F",
              "f": "g", "F": "G",
              "g": "h", "G": "H",
              "h": "i", "H": "I",
              "i": "j", "I": "J",
              "j": "k", "J": "K",
              "k": "l", "K": "L",
              "l": "m", "L": "M",
              "m": "n", "M": "N",
              "n": "o", "N": "O",
              "o": "p", "O": "P",
              "p": "q", "P": "Q",
              "q": "r", "Q": "R",
              "r": "s", "R": "S",
              "s": "t", "S": "T",
              "t": "u", "T": "U",
              "u": "v", "U": "V",
              "v": "w", "V": "W",
              "w": "x", "W": "X",
              "x": "y", "X": "Y",
              "y": "z", "Y": "Z",
              "z": "a", "Z": "A",
}

print("Onward, Algorithms!")

def encipher(s, N):
    """
    A function that rotates the characters in S by integer N
    Arguments:
    S is a string to be rotated
    N:no negative integer between 0 and 25/
    Output: a string where letters in s were rotated by N places
    """
    if s == "":
        return ""
    else:
        return shiftN(s[0], N) + encipher(s[1:], N)
    

def shiftN(c, N):
        """ returns c, shifted by N spots """
        if N == 0: return c
        return shiftN( shift1(c), N-1 ) 

# The function shift1(c)

def shift1(c):
    """ rotate 1 character, c, by 1 place 
        c must be 1 character.
        non-characters don't change!
    """
    if c not in NEXT_CHAR:   # if c is NOT there,
        return c             # just return it unchanged
    else:
        return NEXT_CHAR[c]  # else return the next char
    
def decipher(s):
    """
    Descipers string s using scrabble/letter score. It goes through every possibility and returns the string with the lowest score
    S: a string to be deciphered
    Outputs a deciphered string to the best of its ability.  
    """
    LC = [encipher(s,n) for n in range(26) ]
    LoL = [[scrabbleScore(x),x] for x in LC ]
    minimum = min(LoL)
    return minimum[1]

def scrabbleScore(S):
    if len(S) == 0:
        return 0
    else:
        return letterScore(S[0]) + scrabbleScore(S[1:])

def letterScore(let):
    if let in "aeioulnrstAEIOULNRST":
        return 1
    elif let in "bcmpBCMP":
        return 3
    elif let in "dgDG":
        return 2
    elif let in "fhvwyFHVWY":
        return 4
    elif let in "kK":
        return 5
    elif let in "jxJX":
        return 8
    elif let in "qzQZ":
        return 10
    else:
        return 0
    
def blsort(L): 
    """
    Sorts L
    L: a list filled with 0 and 1
    Outputs a list sorted, 0 to 1

    Uses if statements to determine if the value is 0 or 1 and assigns apprpritately.
    """
    if len(L) == 0:
        return []
    else:
        if L[0] == 0:
            return [L[0]] + blsort(L[1:])
        else:
            return blsort(L[1:]) + [L[0]]
        
def gensort(L): 
    """
    Sorts L
    L: a list filled with nums
    Outputs a list sorted in ascending order
    """
    if len(L) == 0:
        return []
    else:
        low = min(L)
        L = remOne(low, L)
        return [low] + gensort(L)

def remOne(e,L):
    """Returns a new copy of L with the first e removed."""
    if len(L) == 0: 
        return L
    elif L[0] == e:
        return L[1:]
    else:
        return L[0:1] + remOne(e, L[1:])

def jscore(S, T):
    """
    Returns the score of the number of letters S and T shared
    S: a string
    T: a string
    Output: an int definingbhow mnay letters S and T share
    """
    if len(S) == 0:
        return 0
    elif S[0] in T:
        T = remOne(S[0], T)
        S = remOne(S[0], S)
        return 1 +  jscore(S,T)
    else:
        return 0 + jscore(S[1:], T)
    
def exact_change(target_amount, L):
    """
    Determines if target_amount can be calculated using nums in L
    target_amount: an int
    L: a list made up of N
    Output is either true or false based if target_amount can be summed up
    """
    if target_amount == 0:
        return True
    elif target_amount < 0: 
        return False
    elif len(L) == 0:
        return False
    else:
        return exact_change(target_amount - L[0], L[1:]) or exact_change(target_amount, L[1:])



def LCS(S, T): 
    """
    
    """
    if S == "" or T == "":
        return ""
    elif S[0] == T[0]:
        return S[0] + LCS(S[1:], T[1:])
    else:
        result1 = LCS(S[1:], T)

        result2 = LCS(S, T[1:])
        if len(result1) > len(result2):
            return result1
        elif len(result1) < len(result2):
            return result2
        else:
            return result1