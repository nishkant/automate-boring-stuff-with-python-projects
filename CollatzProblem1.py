'''
Determining Collatz Sequence for a given number
'''
#############################################################################################
#First defining a function for running one operation of collatz seq on a given no.


def collatz(number):  
    
    try:  #using try-except statement to avoid error if any string is entered while calling the function.

        if number > 0:   #using a loop so that the operation is executed only on a positive integer

            if number % 2 == 0:  #for even int
                output =  number//2
                print(output)
                return output
         
            elif number % 2 == 1:   #for odd int
                output = number*3 + 1 
                print(output)
                return output 
        
            else:    #If the input given is not an integer.
                print("Please enter a positive integer.")

        else: #If the input given is a negative number.
            print("Please enter a positive integer.")


    except:     #If the input given is a string.
        print("Please enter a positive integer.")

'''
In the above function we wanted to specify the data type of my argument i.e 'number' to a positive integer only,
so that whenever a negative number, float , or string is given as an input it shows an error and later on is 
compensated within the try and except statement we used for strings.
But as of now we couldn't figure out how to do it, thus we had to use an extra if-else statement to identify 
any neagtive number of float .

REFER COLLATZPROBLEM2 FOR AN ALTERNATIVE SOLUTION TO THIS PROB

'''        
#############################################################################################

#defining function to run collatz operation again and again until '1' is obtained 
#Thus completeing the collatz sequence.

def CollatzSeq(input):    #here we used a standard name as a argument but it wont affect our program as we have defined it locally
    while True:
        input = collatz(input)
        if input != 1:
            continue
        else:
            break

#############################################################################################

print("Collatz sequence")
UserInput = int(input("Enter a positive integer here: "))
CollatzSeq(UserInput)
    