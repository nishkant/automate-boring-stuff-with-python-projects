
#a raw string ignores all the '\'s and treats them as normal text.
print(r"C:\Users\Al\Desktop") #example of a raw string


#using triple quotes for printing multiple line strings.
print("""hello, 
my name is anthony gonsalves

mai duniya me akela hun.

geiegeige""")


#using "f" string to use variables inside a string.
#thats much easier than using %s,%d characters.
name = "NJ"
height = "5'10"
print(f"My name is {name} and I am {height} feet tall")


#upper(), lower(), isupper(), and islower() string methods
a = "Amar"
print(a.lower())
print(a.upper())
print(a.islower())
print(a.isupper())



#join method
print("".join(["My", "name", "is", "L"]))
#split method
print("MY name is L".split(" "))
#partition method
print('Hello, world!'.partition('w'))


#Justifying Text with the rjust(), ljust(), and center() Methods
print("hello".rjust(20,"%"))
print("hello".ljust(10,"@"))
print("hello".center(30,"*"))
########################
#use case of justification method
def printPicnic(itemsDict, leftWidth, rightWidth):
 print('PICNIC ITEMS'.center(leftWidth + rightWidth, '-'))
 for k, v in itemsDict.items():
    print(k.ljust(leftWidth, '.') + str(v).rjust(rightWidth))
picnicItems = {'sandwiches': 4, 'apples': 12, 'cups': 4, 'cookies': 800000}
printPicnic(picnicItems, 12, 5)
printPicnic(picnicItems, 20, 6)
#########################


#strip method
spam = ' Hello, World '
print(spam.strip())
print(spam.lstrip())
print(spam.rstrip())
print("absabsabsgoodabsmorningabsguysabsabs".strip("abs"))


#unicode indexes
ord("a")
ord("b")
chr(ord("a")+ 1)
ord("A")
chr(44)
chr(23)
chr(67)


#pyperclip module for copying and pasting.
import pyperclip
pyperclip.copy("sheep sheep")