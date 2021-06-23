'''
Determining Collatz Sequence for a given number
'''
#############################################################################################
#First defining a function for running one operation of collatz seq on a given no.


def collatz(number):  
    
    # try:  #using try-except statement to avoid error if any string is entered while calling the function.

    #     if number > 0:   #using a loop so that the operation is executed only on a positive integer

            if number % 2 == 0:  #for even int
                output =  number//2
                print(output)
                return output
         
            elif number % 2 == 1:   #for odd int
                output = number*3 + 1 
                print(output)
                return output 
        
            # else:    #If the input given is not an integer.
            #     print("Please enter a positive integer.")

        # else: #If the input given is a negative number.
        #     print("Please enter a positive integer.")


    # except:     #If the input given is a string.
    #     print("Please enter a positive integer.")

       
#############################################################################################

#defining function to run collatz operation again and again until '1' is obtained 
#Thus completeing the collatz sequence.

def CollatzSeq(input):    #here we used a standard name as a argument but it wont affect our program as we have defined it locally
    while True:
        if input>0:
            input = collatz(input)
            if input != 1:
                continue
            else:
                break
        else:
            print("Please enter a positive integer.")
            break
#############################################################################################

print("Collatz sequence")

  #using try-except statement while obtaining user input so as to tackle any non integer entry
  
try:  
    UserInput = int(input("Enter a positive integer here: "))
    CollatzSeq(UserInput)
except:
    print("Please enter a positive integer.")
   


     