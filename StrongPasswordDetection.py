'''
    A regex prograam for checking password strength.
    Created: Sep 30, 2021
    Creator: Nishkant
'''
import re

##################################################################################
# Conditions given for the strong password:-
# - Atleast 8 char long
# - Both upercase and lower case letters.
# - At least one digit.

atLeastOneDigit = re.compile(r"([0-9])")
upperCase = re.compile(r"([A-Z])")
lowerCase = re.compile(r"([a-z])")
atLeast8Char = re.compile(r"\w{8,10}?")

def isPasswordStrong(password):

    if len(atLeast8Char.findall(password)) != 0 and len(lowerCase.findall(password)) != 0 and len(upperCase.findall(password)) != 0 and len(atLeastOneDigit.findall(password)) != 0:
        print("Thank you for entering the password.")
        return True
    else:
        print("Not a strong password, Please try another one.")
        print('''
The password should contain atleast one upercase,
one lowercase , one numerical char,
and must have atleast 8 charachters.
        ''')
        return False

while True:
    password = input("Enter your password here:")
    if isPasswordStrong(password):
        break