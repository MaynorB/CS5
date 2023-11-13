#
# hw8pr4.py
#

#
# Example user-interaction looping program
#  (a variant of the one we reviewed in class)
#

def menu():
    """Prints the menu of options that the user can choose."""
    print()
    print("(0) Enter a new list")
    print("(1) Continue (and re-print)!")
    print("(2) Find the Average")
    print("(3) Find the standard deviation")
    print("(4) Find the minimum and its day")
    print("(5) Find the maximum and its day")
    print("(6) Your TT investment plan")
    print("(9) Break! (quit)")
    print()


def find_average(L):
    """
    Takes a list and returns the average of all values in the list
    """
    sum = 0
    for i in range(len(L)):
        sum += L[i]
    return sum / len(L)

def standard_deviation(L):
    """
    Gets the standard deviation of L
    """
    deviation = 0
    for i in range(len(L)):
        deviation += L[i] - find_average(L)
        deviation = deviation ** 2
    deviation /= len(L)
    deviation = deviation ** (1/2)
    return deviation

def find_min(L):
    """
    Find the minimum of L and returns its index
    """
    min = L[0]
    index = 0
    for i  in range(len(L)):
        if L[i] < min:
            min = L[i]
            index = i
    return index

def find_max(L):
    """
    Find the maximum of L and returns its index
    """
    max = L[0]
    index = 0
    for i  in range(len(L)):
        if L[i] > max:
            max = L[i]
            index = i
    return index

def tts(L):
    """
    calculates ther max profit and returns the profit, day to buy and sell
    """
    max_so_far = 0
    b_day = 0
    s_day = 0
    for b in range(len(L)):
        for s in range(b + 1, len(L)):
            diff = L[s]-L[b]
            if diff > max_so_far:
                max_so_far = diff
                b_day = b
                s_day = s
    return max_so_far, b_day, s_day



def main():
    """The main user-interaction loop."""
    secret_value = 4.2

    L = [30, 10, 20]  # an initial list

    while True:       # The user-interaction loop
        print("\n\nThe list is", L)
        menu()
        choice = input("Choose an option: ")

        #
        # "Clean and check" the user's input
        # 
        try:
            choice = int(choice)   # Make into an int!
        except:
            print("I didn't understand your input! Continuing...")
            continue

        #
        # Run the appropriate menu option
        #
        if choice == 9:    # We want to quit
            break          # Leaves the while loop altogether

        elif choice == 1:  # We want to continue (and print) ...
            print("Continuing...")
            continue       # Goes back to the top of the while loop,
                           # ..where it will print L

        elif choice == 0:  # We want to enter a new list
            newL = input("Enter a new list: ")    # Enter _something_
            
            #
            # "Clean and check" the user's input
            #
            try: 
                newL = eval(newL) # eval runs Python's interpreter! Note: Danger!
                if type(newL) != type([]): 
                    print("That didn't seem like a list. Not changing L.")
                else: 
                    L = newL  # Here, things were OK, so let's set our list, L
            except:
                print("I didn't understand your input. Not changing L.")

        elif choice == 2:  #Finds the average
            n = find_average(L) # Get the next element from the predict function
            print("The Average is", n)

        elif choice == 3:  # Deviation
            d = standard_deviation(L)
            print("The Standard deviation is: ", d)
        elif choice == 4:  # Minimum
            m = find_min(L)
            print("The minimum value in L is", L[m], " at day ", m)

        elif choice == 5:  # Maximum
            m = find_max(L)
            print("The minimum value in L is", L[m], "at day ", m)
        elif choice == 6:
            profit, buy_day, sell_day = tts(L)
            print("Max profit will be ", profit, " when you buy on day ", buy_day, " and sell on day ", sell_day)

        else:
            print(choice, " ?      That's not on the menu!")

    print()
    print("See you yesterday!")