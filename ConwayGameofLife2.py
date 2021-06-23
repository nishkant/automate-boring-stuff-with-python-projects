'''
    2nd code for Game of life, 1st one was copied .
    Basically it is a modification of that copied code.

    Created- 25 may, 2021
    The 2nd amendment and other edits- 27 may, 2021

    Things changed:-
        1. Instead of selecting alive and dead cell by using random module , we have taken input from the user to 
           get the cordinates of alive cells.
        2. While specifying neighbouring co-ordinates we didnt used the "%" operator to reduce the cordinate to binary.
                Instead to prevent error at the border cases we used try and except statement .
                This also solved the problem that the the code was interpreting the last and first cells (border cells)
                as neighbours.

'''

import copy, time

#####################################################################################################
#taking inputs for alive cord.
x_cord = []
y_cord = []
cord = []
print("Enter x and y cordinates of the cells which you want to be alive initially.")
print("Press enter to exit.")
while True:
    try:
        a = int(input("Enter x cord:"))
        x_cord.append(a)
        b = int(input("Enter y cord:"))
        y_cord.append(b)
        cord.append((a,b))
    except:
        break

print(cord)

#####################################################################################################
#creating the grid

WIDTH = 60
HEIGHT = 12
# Create a list of list for the cells:
nextCells = []
for x in range(WIDTH):
    column = [] # Create a new column.
    for y in range(HEIGHT):
        column.append(' ') # Add a dead cell.
    nextCells.append(column) # nextCells is a list of column lists

#Making cells alive as per initiall given cordinates.
for x in range(WIDTH):
    for y in range(HEIGHT):
        for (x,y) in cord:
            nextCells[x][y] = "#"

#####################################################################################################
#printing the initiall grid

while True: # Main program loop.
    print('\n\n\n\n\n') # Separate each step with newlines.
    currentCells = copy.deepcopy(nextCells)
    # Print currentCells on the screen:
    for y in range(HEIGHT):
        print("|", end="")
        for x in range(WIDTH):
            print(currentCells[x][y], end="|") # Print the # or space.
        print()
        print("-------------------------------------------------------------------------------------------------------------------------") # Print a newline at the end of the row.

#####################################################################################################
#specifying the cordinates and counting the no. of alive neighbours.    
    
    # Calculate the next step's cells based on current step's cells:
    for x in range(WIDTH):
        for y in range(HEIGHT):
# Get neighboring coordinates:
# # `% WIDTH` ensures leftCoord is always between 0 and WIDTH - 1
            leftCoord  = (x - 1) #% WIDTH
            rightCoord = (x + 1) #% WIDTH
            aboveCoord = (y - 1) #% HEIGHT
            belowCoord = (y + 1) #% HEIGHT
            # Count number of living neighbors:
            numNeighbors = 0
            try:
                if currentCells[leftCoord][aboveCoord] == '#':
                    numNeighbors += 1 # Top-left neighbor is alive.
                if currentCells[x][aboveCoord] == '#':
                    numNeighbors += 1 # Top neighbor is alive.
                if currentCells[rightCoord][aboveCoord] == '#':
                    numNeighbors += 1 # Top-right neighbor is alive.
                if currentCells[leftCoord][y] == '#':
                    numNeighbors += 1 # Left neighbor is alive.
                if currentCells[rightCoord][y] == '#':
                    numNeighbors += 1 # Right neighbor is alive.
                if currentCells[leftCoord][belowCoord] == '#':
                    numNeighbors += 1 # Bottom-left neighbor is alive.
                if currentCells[x][belowCoord] == '#':
                    numNeighbors += 1 # Bottom neighbor is alive.
                if currentCells[rightCoord][belowCoord] == '#':
                    numNeighbors += 1 # Bottom-right neighbor is alive.

#####################################################################################################
#Executing the game of life rules.

                # Set cell based on Conway's Game of Life rules:
                if currentCells[x][y] == '#' and (numNeighbors == 2 or numNeighbors == 3):
                # Living cells with 2 or 3 neighbors stay alive:
                    nextCells[x][y] = '#'
                elif currentCells[x][y] == ' ' and numNeighbors == 3:
                # Dead cells with 3 neighbors become alive:
                    nextCells[x][y] = '#'
                else:
                # Everything else dies or stays dead:
                    nextCells[x][y] = ' '
            except:
                continue


    time.sleep(1.2) # Add a 1.2 -second pause after printing each grid to reduce flickering.

