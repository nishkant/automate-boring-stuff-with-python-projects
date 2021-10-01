'''
    A regex version of string.strip() method.
    Created: Oct 01, 2021
    Creator: Nishkant
'''

import re

def regexStrip(string, strip = " "):

    beginStrip = re.compile(f"^[{strip}]") 
    # using f'string for creating character class of given strip string in the function.
    # above regex will check for the striping string from the beginning.

    while True:
        if len(beginStrip.findall(string)) != 0: 
            string = string[1:] # slicing the detected character from the front.
        else:
            break

    endStrip = re.compile(f"[{strip}]$")
    # above regex will check for the striping string from the end.

    while True:
        if len(endStrip.findall(string)) != 0:
            string = string[:-1] # slicing the detected character from the back.
        else:
            break

    return string # returning the modified string.


# example..
print(regexStrip("ghodighodispameggsghodighodi", "hgodi"))

    