#! python3

'''
    A programm to sort and list emails from a text file.
    Created: Sep 26, 2021
    Creator: Nishkant
'''

import re, pyperclip

###########################################################################
# declaring regexes for mobile numbers, landline numbers (indian ph nos.) and email addresses.

emailRegex = re.compile(r'''(
                        [A-Za-z0-9._%+-]+   # username
                        @                   # @ symbol
                        [a-zA-Z0-9.-]+      # domain name
                        \.[a-zA-Z]+         # .something
                        (\.[a-zA-Z]+)?         # .something    ## for eg : abcd@vnit.ac.in
                        )''', re.VERBOSE) 

###########################################################################

docText = pyperclip.paste() # copied doc in which we have to search for mail and ph.no.

# collecting all the regexes with the help of findfall method.
emails = emailRegex.findall(docText)

###########################################################################
# Printing the numbers and mails in a readable format.

print("The emails listed are:-")
print()
# picking only the 1st element from the list fromed by findfall to get rid of the subgrps detected.
for x in emails:
    print(x[0])

