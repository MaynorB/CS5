# coding: utf-8
#
# hw0pr2rps.py
#


import random          # imports the library named random

running = True 

def rps():
   
    """This plays a game of rock-paper-scissors
       (or a variant of that game)
       Arguments: none     (prompted text doesn't count as an argument)
       Results: none       (printing doesn't count as a result)
    """
while running: 
    user = input("Choose your weapon: ")
    comp = random.choice(['rock', 'paper', 'scissors'])
    print()

    print('The user (you)   chose', user)
    print('The computer (I) chose', comp)
    print()

    if user == 'rock' and comp == 'scissors':
        print('Ha! I actually chose paper, which annihilates your rock.')
        letter = input("Play Again?  (Y/N): ")
        if letter == "N":
            running = False

    elif user == 'rock' and comp == 'paper':
        print('I won! Your rock is dust!')
        letter = input("Play Again?  (Y/N): ")
        if letter == "N":
            running = False

    elif user == 'rock' and comp == 'rock':
        print('Rats, a tie')
        letter = input("Play Again?  (Y/N): ")
        if letter == "N":
            running = False

    elif user == 'paper' and comp == 'scissors':
        print('Your paper just got shredded')
        letter = input("Play Again?  (Y/N): ")
        if letter == "N":
            running = False
    
    elif user == 'paper' and comp == 'paper':
        print('Great minds think alike')
        letter = input("Play Again?  (Y/N): ")
        if letter == "N":
            running = False

    elif user == 'paper' and comp == 'rock':
        print('Now I can not use my rock for my door')
        letter = input("Play Again?  (Y/N): ")
        if letter == "N":
            running = False
    
    elif user == 'scissors' and comp == 'scissors':
        print('Nothing to say about this')    
        letter = input("Play Again?  (Y/N): ")
        if letter == "N":
            running = False

    elif user == 'scissors' and comp == 'paper':
        print('NOOOOOOOO MY PASSPORT') 
        letter = input("Play Again?  (Y/N): ")
        if letter == "N":
            running = False 

    elif user == 'scissors' and comp == 'rock':
        print('Now you can not cut your trash')  
        letter = input("Play Again?  (Y/N): ")
        if letter == "N":
            running = False
    