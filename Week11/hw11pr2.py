import random
class Board:
    """A data type representing a Connect-4 board
       with an arbitrary number of rows and columns.
    """

    def __init__(self, width, height):
        """Construct objects of type Board, with the given width and height."""
        self.width = width
        self.height = height
        self.data = [[' ']*width for row in range(height)]

        # We do not need to return anything from a constructor!

    def __repr__(self):
        """This method returns a string representation
           for an object of type Board.
        """
        s = ''                          # The string to return
        for row in range(0, self.height):
            s += '|'
            for col in range(0, self.width):
                s += self.data[row][col] + '|'
            s += '\n'

        s += (2*self.width + 1) * '-' + "\n"   # Bottom of the board

        # Add code here to put the numbers underneath
        for col in range(0, self.width):
            s += " " + str(col % 10)
            

        return s       # The board is complete; return it
    def addMove(self, col, ox):
        """
        drops ox into the respective coloumn to the next avaliable row
        """
        if self.allowsMove(col):
            count = -1
            for row in range(0, self.height):
                if (self.data[row][col] == " "):
                    count += 1
            self.data[count][col] = ox


    def clear(self):
        """
        Clears the Board
        """
        for row in range(0, self.height):
            for col in range(0, self.width):
                self.data[row][col] = " "

    def setBoard(self, moveString):
        """Accepts a string of columns and places
           alternating checkers in those columns,
           starting with 'X'.

           For example, call b.setBoard('012345')
           to see 'X's and 'O's alternate on the
           bottom row, or b.setBoard('000000') to
           see them alternate in the left column.

           moveString must be a string of one-digit integers.
        """
        nextChecker = 'X'   # start by playing 'X'
        for colChar in moveString:
            col = int(colChar)
            if 0 <= col <= self.width:
                self.addMove(col, nextChecker)
            if nextChecker == 'X':
                nextChecker = 'O'
            else:
                nextChecker = 'X'
    def allowsMove(self, c):
        """
        checks if the column is legal or if its full to allow the move
        to occur
        """
        if (c < 0 or c > self.width or self.data[0][c] != " "):
            return False
        return True
    
    def isFull(self):
        """
        checks if the board is full
        """
        for col in range(self.width):
            if self.allowsMove(col):
                return False
        return True

    def delMove(self, c):
        """
        Deletes the most recent move for column c
        """
        count = 0
        for row in range(0, self.height):
            if (self.data[row][c] == " "):
                count += 1
            if (count == self.height - 1):
                break
        self.data[count][c] = " "

    def winsFor(self, ox):
        """
        Checks if ox has won the game
        """
        H = self.height
        W = self.width
        D = self.data

        # Check to see if ox wins, starting from any checker:
        for row in range(H):
            for col in range(W):
                if inarow_Neast(ox, row, col, D, 4) == True:
                    return True
                if inarow_Nnortheast(ox, row, col, D, 4) == True:
                    return True
                if inarow_Nsouth(ox, row, col, D, 4) == True:
                    return True
                if inarow_Nsoutheast(ox, row, col, D, 4) == True:
                    return True
                # you need three more, very similar, such checks
                # for the three other directions!

        return False     # only gets here if it never returned True, above

    def colsToWin(self, ox):
        """
        returns the list of columns where ox can move in the next turn in order to win and finish the game
        """
        list = []
        for col in range(self.width):
            if self.allowsMove(col):
                self.addMove(col, ox)
                if self.winsFor(ox):
                    list.append(col)
                self.delMove(col)
        return list
    
    def aiMove(self, ox):
        """
          return a single integer, which must be a legal column in which to make a move. 
        """

        list_to_win = self.colsToWin(ox)
        if len(list_to_win) > 0:
            return list_to_win[0]
        else:
            opp = ""
            if ox == "X":
                opp = "O"
            else:
                opp = "X"
            opp_list_to_win = self.colsToWin(opp)
            if len(opp_list_to_win) >= 1:
                return opp_list_to_win[0]
        # Trust the process :)
            list_of_legal_cols = []
            for cols in range(0, self.width):
                if self.allowsMove(cols):
                    list_of_legal_cols.append(cols)
            if (len(list_of_legal_cols) == 1):
                return list_of_legal_cols[0]
            num = random.randint(0, len(list_of_legal_cols) - 1)
            return num
                
                        

    def hostGame(self):
        """
        Hosts a two player game of Connect 4
        """
        print("WELCOME ALL TO THE DEATHMATCH OF THE CENTRY")
        print("...what you mean it isn't to the death?...oh wrong sport")
        print("WELCOME ALL TO CONNECT 4!!!!")
        current_player = "X"
        print(self)
        while self.winsFor("X") == False and self.winsFor("O") == False:
            
            while current_player == "X":
                users_col = self.aiMove("X")
                print(users_col)
                while self.allowsMove(users_col) == False:  # _while_ not valid
                    users_col = self.aiMove("X")  # ask for a column
                self.addMove(users_col, "X")
                print(self)
                if self.winsFor("X") or self.isFull():
                    break
                current_player = "O"
                    
            while current_player == "O":
                users_col = int(input("O's CHOICE: "))
                while self.allowsMove(users_col) == False:  # _while_ not valid
                    users_col = int(input("PLEASE CHOOSE AN ACTUAL COLUMN: "))  # ask for a column
                self.addMove(users_col, "O")
                print(self)
                if self.winsFor("O") or self.isFull():
                    break
                current_player = "X"
        if self.winsFor("X") == True:
            print("X wins!!! Congratulations!")
            print("You now get a puppy!! what?... no puppy?.. what is the prize then?.... THERE ISN'T ONE!?!?!")
            print()
            print()
            print("This game trash")
            print(self)
        elif self.winsFor("O") == True:
            print("O wins!!! Congratulations!")
            print("You now get a fox!! what?... no fox?.. what is the prize then?.... A used soda can?...")
            print()
            print()
            print("I uh... I quit")
            print(self)
        else:
            print("Wow...stalemate")
            print("This is no fun")
            print("now i don't get paid")
            print(self)




# This is the end of the Board class
# Below are some boards that will be re-created each time the file is run:

bigb = Board(15,5)
b = Board(7,6)
b = Board(7, 6)

# Functions to check who won

def inarow_Neast(ch, r_start, c_start, A, N):
    """
    Checks if ch is found N in a row eastbound
    """
    num_rows = len(A)      # Number of rows is len(A)
    num_cols = len(A[0])   # Number of columns is len(A[0])

    if r_start < 0 or r_start >= num_rows:
        return False       # Out of bounds in rows

    # Other out-of-bounds checks...
    if c_start < 0 or c_start > num_cols - N:
        return False       # Out of bounds in columns

    # Are all of the data elements correct?
    for i in range(N):                  # Loop index i as needed
        if A[r_start][c_start+i] != ch: # Check for mismatches
            return False                # Mismatch found--return False

    return True                         # Loop found no mismatches--return True
def inarow_Nsouth(ch, r_start, c_start, A, N):
    """
    Checks if ch is found N in a row eastbound
    """
    num_rows = len(A)      # Number of rows is len(A)
    num_cols = len(A[0])   # Number of columns is len(A[0])
    if r_start < 0 or r_start > num_rows - N:
        return False       # Out of bounds in rows
    # Other out-of-bounds checks...
    if c_start < 0 or c_start >= num_cols:
        return False       # Out of bounds in columns
    # Are all of the data elements correct?
    for i in range(N):                  # Loop index i as needed
        if A[r_start + i][c_start] != ch: # Check for mismatches
            return False                # Mismatch found--return False
    
    return True

def inarow_Nsoutheast(ch, r_start, c_start, A, N):
    """
    Checks if ch is found N in a row southeast bound
    """
    num_rows = len(A)      # Number of rows is len(A)
    num_cols = len(A[0])   # Number of columns is len(A[0])
    if r_start < 0 or r_start > num_rows - N:
        return False       # Out of bounds in rows
    # Other out-of-bounds checks...
    if c_start < 0 or c_start > num_cols  - N:
        return False       # Out of bounds in columns
    # Are all of the data elements correct?
    for i in range(N):                  # Loop index i as needed
        if A[r_start + i][c_start + i] != ch: # Check for mismatches
            return False                # Mismatch found--return False
    
    return True

def inarow_Nnortheast(ch, r_start, c_start, A, N):
    """
    Checks if ch is found N in a row northeast bound
    """
    num_rows = len(A)      # Number of rows is len(A)
    num_cols = len(A[0])   # Number of columns is len(A[0])
    if r_start < num_cols - N or r_start >= num_cols:
        return False       # Out of bounds in rows
    # Other out-of-bounds checks...
    if c_start < 0 or c_start > num_rows - N:
        return False       # Out of bounds in columns
    # Are all of the data elements correct?
    for i in range(N):                  # Loop index i as needed
        if A[r_start - i][c_start + i] != ch: # Check for mismatches
            return False                # Mismatch found--return False
    return True

