'''
    How often does a streak of 6 heads/tails occur in flipping a coin 100 times ???

    Code to calculate the number of streaks in an experiment of flipping a coin 100 times and 
    repeating it 10000 times to calculate a decent average of percentage of streaks.
  
    Created: 27 may, 2021
    Some comments added: 28 may, 2021
    Creator: Nishkant
'''
import random
j = 1 #initiallizing counter for loop.
StreakCount = [] #Initializing a dictioanry for storing no. of streaks for each experiment.

while j<=10000:
#####################################################################################################
    #obtaining the outcomes of the experiment 1 time.

    coin = ["H", "T"]  #defining a coin
    outcomes = []  #creating a list to store the hundred outcomes.
    for x in range(100):
        outcomes.append(random.choice(coin))
    # print(outcomes)

#####################################################################################################
    #counting the no. of streaks.

    NoOfStreaks = 0  
    count = 0   #for counting the outcomes one by one

    
    for i in ("H","T"):      #checking streaks for both heads and tales.
        for x in outcomes:
            if x == i:
                count += 1
                if count == 6:
                    NoOfStreaks += 1
                    count = 0      #after reaching 6 reassigning count as zero to count a new streak.
                else:
                    continue 
            else:
                count = 0
    StreakCount.append(NoOfStreaks)           #adding no. of streaks for each experiment.
    j += 1
#####################################################################################################
#what percentage of the coin flips contains a streak of heads or tails in a row?

                    
#print(StreakCount)
print()

print("The max no of streaks in a single experiment are ", max(StreakCount))  #for max no of streaks in a single experiment.
print()

#calculating the percentage
j = 0
for x in StreakCount:
   j = j + x   #addition of all elements of a list.

print((j*6)/10000 , " percent of the coin flips contain a streak of six heads or tails in a row.")   

#####################################################################################################


''' 
The code may take some time to run depending on your system power as we are doing an experiment 10000 times.
Sorry to annoy your processor.
          :)
'''