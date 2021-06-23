#! python3
'''
    mclip.py - A multi clipboard program.
    Created: Jun 08, 2021
    Creator: Code copied from the book "Automate boring stuff with python."
'''
#this dict contains the keyphrases and the string or text associated with them to be copied on the clip board.
TEXT = {'agree': """Yes, I agree. That sounds fine to me.""",
        'busy': """Sorry, can we do this later this week or next week?""",
        'upsell': """Would you consider making this a monthly donation?"""}


import sys, pyperclip

if len(sys.argv) < 2:  #sys.argv represents the arguments given in the command line
    print('Usage: py mclip.py [keyphrase] - copy phrase text')
    sys.exit()

keyphrase = sys.argv[1] # first command line arg is the keyphrase

if keyphrase in TEXT:
    pyperclip.copy(TEXT[keyphrase])     #copying the text associated with the keyphrase to the clipboard.
    print('Text for ' + keyphrase + ' copied to clipboard.')
else:
    print('There is no text for ' + keyphrase)


#now we will also create a batch file to run our program easily from the "Run" box.
#after creating the batch file we have to save it in C:Windows folder to access it from run dialog box
