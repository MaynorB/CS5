def numToBaseB(N, B):
    """
    Converts base 10 num into base B as a string
    Arguments:
    N is a num in base 10
    B is the base to conver to
    Output is  N in base B in a string
    """
    if N == 0:
        return ""
    else: 
        return numToBaseB( N//B, B ) + str(N % B)
    
def baseBToNum(S, B):
    """
    Converts String Base B into Num base 10
    Arguments:
    S is a num in Base B
    B is the base S is in
    Output is S converted to Base 10
    """
    if S == "":
        return 0
    else:
        return baseBToNum(S[:-1], B) * B + int(S[-1])
    
def baseToBase(B1, B2, s_in_B1):
    """
    Converts s_in_b1 into base B2
    Arguments:
    B1: the base s_in_B1 is in
    B2: the base to convert to
    s_in_B1: the num to be converted in String
    Output is s_in_B1 in B2
    """
    B = baseBToNum(s_in_B1, B1)
    finalB = numToBaseB(B, B2)
    return finalB

def  add(S, T):
    """
    Add binary S and T
    Arguments:
    S is a binary string
    T is another binary String
    Output is S and T added together and is in binary
    """
    m = baseBToNum(S, 2)
    n = baseBToNum(T,2)
    sum = m + n
    sum = numToBaseB(sum, 2)
    return sum

def addB(S, T):
    """
    Adds S and T only in binary
    S is a string representing a binary
    T is a string representing a binary
    Output is S abd T added together, in binary
    """
    #base cases!
    if(S == '' and len(T) > 0):
        return T
    elif (len(S) > 0 and T == ''):
        return S
    elif(S == '' and T == ''):
        return ''
    elif S[-1] == '0' and T[-1] == '0':
        return addB(S[:-1], T[:-1]) + '0'  
     
    elif S[-1] == '1' and T[-1] == '0':
        return addB(S[:-1], T[:-1]) + '1'
    
    elif S[-1] == '0' and T[-1] == '1':
        return addB(S[:-1], T[:-1]) + '1'
    
    elif S[-1] == '1' and T[-1] == '1':
        S = addB(S[:-1], '1')
        return addB(T[:-1],S) + '0'
    
def compress(S):
    """
    Comprersses S into a run-length encoding of 8 bit-byte
    S is a binary number string
    Output is S compressed into 8 bit byte string
    """
    if(S == ""):
        return ""
    num = frontNum(S)
    binary_num = numToBinary(num)
    first = S[0]
    zero_count = 7 - len(binary_num)
    S = S[num:]
    return first + zero_count * "0" + binary_num + compress(S)


def frontNum(S):
    if len(S) <= 1:
        return 1

    elif S[0] == S[1]:
        return 1 + frontNum(S[1:])

    else:
        return  1
    
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
    elif N % 2 == 1:
        return   numToBinary(N//2) + '1'
    else:
        return   numToBinary(N//2) + '0'
    
def uncompress(C):
    """
    Decompresses C from 8-bit bytes into binary String
    C is a string representing 8-bit byte
    Output is a string in binary
    """
    if(C == ""):
        return ""
    num_choice = C[0]
    binary_num = C[1:8]
    binary_num = binaryToNum(binary_num)
    return printB(num_choice, binary_num) + uncompress(C[8:])


def printB(num, total):
    return num * int(total)

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