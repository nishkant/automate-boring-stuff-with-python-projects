'''
    A code for multiplayer TicTacToe game.
    Last Edited: Jun 13, 2021
    Creator: Nishkant
'''


import sys

#creating a dictionary for an empty game board.
theBoard = {(1,1): ' ', (1,2): ' ', (1,3): ' ',
            (2,1): ' ', (2,2): ' ', (2,3): ' ',
            (3,1): ' ', (3,2): ' ', (3,3): ' '}

def printBoard(board):
    ''' For printing the game board '''

    print()
    print(board[(1,1)] + ' | ' + board[(1,2)] + ' | ' + board[(1,3)])
    print('--$---$--')
    print(board[(2,1)] + ' | ' + board[(2,2)] + ' | ' + board[(2,3)])
    print('--$---$--')
    print(board[(3,1)] + ' | ' + board[(3,2)] + ' | ' + board[(3,3)])
    print()

def WinCheck(board):
    ''' For cheking if any player has won in the TicTacToe game '''

    g = 0 # initiallizing a switch which will turn to 1 if any player wins.
          # will be helpful for performing actions after the win in any condition.

    # Checking for rows....
    for P in ("O", "X"):
        for i in range(1,4): #checking each row one by one.
            if board[(i,1)] == board[(i,2)] == board[(i,3)] == P:                
                g = 1
                break   
    # checking for columns....
        for i in range(1,4):
            if board[(1,i)] == board[(2,i)] == board[(3,i)] == P:               
                g = 1
                break

    # checking for diagonas....
        if board[(1,1)] == board[(2,2)] == board[(3,3)] == P:
            g = 1
            break
        elif board[(3,1)] == board[(2,2)] == board[(1,3)] == P:
            g = 1
            break
    #printing the winning message, game board and exiting the game if a player wins.
    if g == 1:
        print("****************************************************")
        printBoard(board)
        print(P," won." + " Tum to bade heavy player nikle.")
        print("****************************************************")
        sys.exit()
    

#starting the game.....
print('''
New game started...

Enter the position in the format (a,b) where a is row no. and b is column no.
Starting from top left i.e. (1,1).

Enjoy the game :)''')

turn = 'X'

for i in range(9): #running the loop for all 9 spaces.
    printBoard(theBoard)
    while True: #used for compensating errors by the user while giving inputs.
        print('Turn for ' + turn + '. Move on which space?')
        try:
            a, b = input().split(",")
            a = int(a)
            b = int(b)
        except:
            print("Please enter a valid position.")
            continue
        if (a,b) not in theBoard.keys(): #if the format entered is correct but the position is not available.
            print("Please enter a valid position.")
        elif theBoard[(a,b)] != " ": #if already occupied space is entered.
            print("This position is already occupied , choose a different one.")
        else:
            theBoard[(a,b)] = turn
            break
    # changing the turns.
    if turn == 'X':
        turn = 'O'
    else:
        turn = 'X'
    #checking if someone won...
    WinCheck(theBoard)

#using for-else statement and printing in case of a draw.
else:
        print("****************************************************")
        printBoard(theBoard)
        print("Its a draw ,tired of your old tricks, try somethin different.")
        print("****************************************************")

