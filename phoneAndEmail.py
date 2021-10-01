
#! python3

''' A program file for sorting phone nos. and email addresses.
    Created: Jul 15, 2021
    Edit-1: Sep 24, 2021
        - Resumed learning after Jul 15 and added methods to efficiently print found regexes.
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


mobileRegex = re.compile(r'''(
                        (\+91)?             # country code
                        [\s|\-|\.]?         # seperator
                        (\d{3})             # first 3 digits
                        # [\s|\-|\.]?         # seperator
                        (\d{3})             # middle digits
                        # [\s|\-|\.]?         # seperator
                        (\d{4})             # last 4 digits
                        )''', re.VERBOSE)


landlineRegex = re.compile(r'''(
                            [0]?            # for mobiles
                            (\d{3}(\s|\-|\.))?        # std code (I put the seperator in the same grp as it is not required whe)
                            # (\s|\-|\.)?     # seperator
                            (\d{3})         # first 3 digit
                            (\d{4})         # next 4 digits
                            )''', re.VERBOSE)

###########################################################################

docText = str(pyperclip.paste()) # copied doc in which we have to search for mail and ph.no.
# pasted as a string so as to use string formatting options during copying to clipboard.

###########################################################################


matches = []

for groups in emailRegex.findall(docText):
    matches.append(groups[0])
for groups in landlineRegex.findall(docText):
    matches.append(groups[0])
for groups in mobileRegex.findall(docText):
    matches.append(groups[0])


if len(matches) > 0:
    pyperclip.copy("\n".join(matches))
    print("The emails and numbers are copied to the clipboard")
    print("\n".join(matches))
else:
    print("No emails and phone numbers found.")
    








