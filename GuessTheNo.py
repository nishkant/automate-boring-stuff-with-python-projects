# writing a code for 'guess the number' game.
import random

##############################################################################
# selecting the range
print("Select a range from which I should pick a number, starting from 1.")
domain = int(input())
print("Okay, I am choosing the number from 1 to ", domain)
##############################################################################

# picking a number
PickedNo = random.randint(1, domain)

##############################################################################
# Taking a guess and validating

attempts = []  # defining an empty list
while True:
    print("Take a guess.")
    GuessedNo = int(input())

    attempts.append(GuessedNo)  # recording the inputs given by user.

    if GuessedNo > PickedNo:
        print("Slightly lower")
    elif GuessedNo < PickedNo:
        print("Slightly Higher")
    else:
        break
##############################################################################


score = len(attempts)  # calculating the no of attempts

print("")
print("Congratulations You have guessed the correct number in %d attempts." % (score))
print("")
print( "Your attempts were :" , attempts)
print("")