# coding: utf-8
#
# hw0pr2if.py
#

""" ipyh
Title for your adventure:   The Quest.

Notes on how to "win" or "lose" this adventure:
  To win, choose the table.
  To lose, choose the door.
"""

import time

def adventure():
    """This function runs one session of interactive fiction
       Well, it's "fiction," depending on the pill color chosen...
       Arguments: no arguments (prompted text doesn't count as an argument)
       Results: no results     (printing doesn't count as a result)
    """
    delay = 0.0          # change to 0.0 for testing or speed runs,
                         # ..larger for dramatic effect!

    user_name = input("What do they call you, worthy adventurer? ")

    print()
    print("Welcome,", user_name, " to the Libra Complex, a labyrinth")
    print("of weighty wonders and unreal quantities...of poptarts!")
    print()

    print("Your quest: To find--and partake of--a poptart!")
    print()
    flavor = input("What flavor do you seek? ")
    if flavor == "strawberry":
        print("Wise! You show deep poptart experience.")
    elif flavor == "s'mores":
        print("The taste of the campfire: well chosen, adventurer!")
    else:
        print("Each to their own, then.")
    print()

    print("On to the quest!\n\n")
    print("A corridor stretches before you; its dim lighting betrays, to")
    print("one side, a table supporting nameless forms of inorganic bulk")
    print("and, to the other, a door ajar, leaking laughter--is that")
    print("laughter?--of lab-goers.")
    time.sleep(delay)
    print()

    choice1 = input("Do you choose the table or the door? [table/door] ")
    print()

    if choice1 == "table":
        print("As you approach the table, its hazy burdens loom ever larger,")
        print("until...")
        time.sleep(delay)
        print("...they resolve into unending stacks of poptarts, foil")
        print("shimmering.  You succeed, sumptuously, in sating the")
        print("challenge--and your hunger.")

        choice2 = input("Do you consume all the poptars? (Y/N): ")
        if choice2 == "Y":
            print("great choice, it's bulking season")
        elif choice2 == "N":
            print("Then no gains for you ", user_name)

        print("As the sun sets, time passing by from the poptsrts you ate, you realize a drink is missing")
        time.sleep(1)
        print("It's time to choose a drink!")
        print()
        print("On the table there's milk and juice")
        choice3 = input("What do you grab?")
        if choice3 == "milk":
            print("Milk is always a good option")
        elif choice3 == "juice":
            print("Any kind of juice is best... except for cranberry, you like that then we going to have problems")
        else:
            print("Nothing? water for you then...basic smh")

        print("Alright the journey is almost over, this journey of poptarts")
        print()
        print("The narrator is getitng tired of speaking so looks like we have one final event to go")
        print()
        print("You decide to go onto a walk after consuming poptarts and up ahead...")
        print()
        choice3 = input("In front of you there is a Chipotle, McDonalds, Burger King, Pollo Loco, and an Olive Garden, to which do you enter?")
        if choice3 == "Chipotle":
            print("I...we could have been friends, you've lost all respect now")
            print()
            print("Like you could have put your own choice")
            print()
            print("But nooooooooo, you had to choose chipotle")
            print()
            print("Whatever, not worth my time to rant on Chiptole rn")
        print("Your story comes to a close, as you happily eat the resstraunt of your choice")
        print("Unless you chose Chiptole, then you explode")
        print()
        print("The End")
        

    else:  
        print("You push the door into a gathering of sagefowl, athenas,")
        print("and stags alike, all relishing their tasks. Teamwork and")
        print("merriment abound here, except...")
        time.sleep(delay)
        print("...they have consumed ALL of the poptarts! Drifts of wrappers")
        print("coat the floor.  Dizzy, you grasp for a pastry. None is at")
        print("hand. You exhale and slip under the teeming tide of foil as")
        print("it finishes winding around youuuu.... u./.edndwn ewjdnwnjw cwdccddwdww")
        time.sleep(delay)
        time.sleep(delay)
        time.sleep(delay)
        time.sleep(delay)
        time.sleep(delay)
        print("nitializing...")
        time.sleep(delay)
        time.sleep(delay)
        print("Now ain't that a sad ending, well good thing I'm here now")
        choice4 = input("Now, in front of you is a Deep Fryer, Microwave, and an Oven... chose one")
        if choice4 == "Deep Fryer":
            print("great choice, it's KFC branded sooooooo a rat probably somersaulted into it")
        elif choice4 == "Microwave":
            print("Microwave goes Mmmmmmmmmmmmmmmmmmmmmmmmmmm")
        elif choice4 == "Oven":
            print("... yeah nothing here")
        else:
            print("So you either mispelled or chose none...very fun you are")
        print("Alright Alright, let's wrap this up real quick")
        print("I have a hot pocket and I like to enjoy it warm")
        choice5 = input("Speaking about hot pockets, do you like them warm?")
        if choice5 == "yes":
            print("Good, Very good, and you spelt it right. Alright just bear with me while someone else spelt it wrong or wrote cold")
        else:
            print("WHY WHY WHY WHY WHY WHY WHY WHY WHY WHY WHY WHY WHY WHY")
            print("Two options, you spelt 'yes' very wrong or you're insane, probably that one")
        print("Alright I'm done with this part of the story, Ima sleep now because this took too long to wrtie.")


 
