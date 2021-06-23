#! python3
'''
    A code for bulletizing the copied lines.
    Created: Jun 09, 2021
    Creator: Nishkant
'''

import sys, pyperclip

copiedText = pyperclip.paste()  #variable containg the text on the clipboard.

splittedText = copiedText.split("\n")  #splitting the text at every new line.

bulletedText = []  #creating a list for stroing the new bulletized text.


for line in splittedText:
    line = "* " + line  #adding a bullet and a space to each new line fron the clipboard.
    bulletedText.append(line)  #adding each line to the list.

pyperclip.copy("\n".join(bulletedText)) #joining the splitted text again with a new line and copying it to the keyboard.
print("Bullets are added to each new line.")

