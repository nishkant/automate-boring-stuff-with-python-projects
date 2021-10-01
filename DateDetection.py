'''
    A regex program to extract dates of the format (DD/MM/YYYY) from a text file.
    Created: Sep 28, 2021
    Creator: Nishkant
'''


import re, pyperclip

############################################################################################

# Defining regex for DD/MM/YYYY (year - (1000-2999)) format.

######################################################

# dateRegex = re.compile(r'''(
#             ((0[1-9])|([10-31])) # DD
#             /                # seperator
#             ((0[1-9])|([10-12])) # MM
#             /                # seperator
#             ([1000-2999])    # YYYY 
#             )''', re.VERBOSE)

# So I made this mistake while defining character classes for the days months and years...
# I thought that for years 1000-2999 the character class [1000-2999] will be okay but this is not how it works...
# It is like one charachter class is defined for only one character at a time so for 1000-2999 we will define it like,
# ([12][0-9]{3})

######################################################

dateRegex = re.compile(r'''(
            (0[1-9]|[12][0-9]|3[01]) # DD(01-09|10-29|30-31)
            /                # seperator
            (0[1-9]|1[0-2]) # MM (01-09|10-12)
            /                # seperator
            ([12][0-9]{3})    # YYYY (1000-2999)
            )''', re.VERBOSE)

############################################################################################

# using findfall to extract dates in the given format.            

text = str(pyperclip.paste())
dates = dateRegex.findall(text)

############################################################################################

# Till now our program works fine for the format but it's not upto the mark for checking the...
# ... legitimacy of the dates , For example see the below two cases-

# 31/04/2888 ## 31st date of april.
# 29/02/2019 ## 29th of feb in a non leap year. 

# also if we try to include the corrections in our regex only then it will become very tedious task ...
# ... and will loose the concept of reges i.e. to simply detect regularly occuring expressions.

############################################################################################

# Therefore, now we will define the legitimacy bylaws to which our programm will adhere so as to ...
# detect a real and legit date.

# Lets get started....

# Naming group indexes to make our programm more understandable.
day = 1 
month = 2
year = 3

def isLeapYear(y):
    '''Function to identify a leap year.'''
    if int(y) // 4 == 0:
        if int(y) // 100 == 0 and int(y) // 400 != 0:
            return False
        else:
            return True

def isValidDate(items):
    '''A function to check if a date is valid or not.'''

    # April, June, September, and November have 30 days, February has 28 days,
    # and the rest of the months have 31 days. 

    if items[month] in ["04","06","09","11"] and items[day] == "31":
        return False

    elif items[month] == "02" and items[day] in ["29","30","31"]:
        return False

    # February has 29 days in leap years. 
    # Leap years are every year evenly divisible by 4,
    # except for years evenly divisible by 100,
    # unless the year is also evenly divisible by 400.

    elif items[month] == "02" and items[day] == "29" and isLeapYear(items[year]):
        return True

    else:
        return True

############################################################################################

# validating and collecting the dates.

# 30/06/2002 ## test case

legitDates = []
for items in dates:
    if isValidDate(items):
        legitDates.append(items[0])


print(legitDates)