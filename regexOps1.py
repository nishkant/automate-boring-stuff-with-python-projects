
import re

''' creating a regex object. '''
phoneNumRegex = re.compile(r"\d{3}-\d{3}-\d{4}")  # raw string


''' searching the string for any regex object match '''
mo = phoneNumRegex.search('My number is 415-555-4242 , 415-555-4244, 415-555-4222.')


''' returning the actual matched regex. '''
print("The phone no. is", mo.group())



''' grouping with parenthesis. '''
phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
mo = phoneNumRegex.search('My number is 415-555-4242.')

area_code = 1
ph_no = 2

print("\nThe area code is", mo.group(area_code))
print(f"The number is {mo.group(ph_no)}.") # using "f" string.
print(mo.group())
print(mo.group(0))



''' using pipe method ''' 
# this method is used to match one of many expressions.
# if more than one of the provided expressions is present in the string then the one occuring first...
# will be returned.
cartoonRegex = re.compile(r"Shinchan|Doraemon|Kazama|Boo|Nobita|Ferb")
mo1 = cartoonRegex.search("Shinchan and kazama were playing.")
mo2 = cartoonRegex.search("Doraemon ki pocket me sanp.")
mo3 = cartoonRegex.search("Masao and Boo went to Kazama's home.")

print(f"\n{mo1} \n{mo2} \n{mo3}")
print(f"\n{mo1.group()} \n{mo2.group()} \n{mo3.group()}")



'''optional matching with question mark'''
#searching for a phone number which do or do not have area code.
phoneRegex = re.compile(r'(\d\d\d-)?\d\d\d-\d\d\d\d')

mo1 = phoneRegex.search('My number is 415-555-4242')
mo1.group()

mo2 = phoneRegex.search('My number is 555-4242')
mo2.group()



''' matching repetitions with braces'''
hehueregex = re.compile(r"(he)?(hue){3,5}")
mo1 = hehueregex.search("hehuehuehuehueheuheueh") # printed he + 4 times hue
mo2 = hehueregex.search("huehuehuehuehue") #printed 5 times
mo3 = hehueregex.search("huehuehuehue") # printed 4 times
mo4 = hehueregex.search("huehuehuehuehuehue") # printed 5 times
print(mo1.group())
print(mo2.group())
print(mo3.group())
print(mo4.group())

# using this with optional matching

greedyhehe = re.compile(r"(he){3,5}")
nongreedyhehe = re.compile(r"(he){3,5}?")

greedymo = greedyhehe.search("hehehehehe") # printed 5 times (picking the greatest)
nongreedymo = nongreedyhehe.search("hehehehehe") # printed 3 times (picking the least)

print(greedymo.group())
print(nongreedymo.group())



'''findfall method '''
# findfall method returns a list of all the matched objects found in the string,
# unlike the "search" method which only returns the first matched object.
phoneNumRegex = re.compile(r"\d{3}-\d{3}-\d{4}")
mo1 = phoneNumRegex.search('My number is 415-555-4242 , 415-555-4244, 415-555-4222.')
mo2 = phoneNumRegex.findall('My number is 415-555-4242 , 415-555-4244, 415-555-4222.')
print(mo1.group() , "\n", mo2)



'''defining own character classes by using []'''
vowelRegex = re.compile(r"[aeiouAEIOU]")
print(vowelRegex.findall("My name is anthony gonsAlves."))

notVowelRegex = re.compile(r"[^aeiouAEIOU]") # using "^" symbol to compile as a negation of specified character.
print(notVowelRegex.findall("My name is anthony gonsAlves."))

alphabetRegex = re.compile(r"[a-zA-Z]") # using hyphen(-) to specify a range of characters.
print(alphabetRegex.findall("My name is anthony gonsAlves\n."))



'''carret, dollar, wildcard character.'''
beginsWithATregex = re.compile(r"^.at")
print(beginsWithATregex.search("Rat ate a sheep with sauce.").group())

endsWithRegex = re.compile(r"sauce\.$")
print(endsWithRegex.search("Rat ate a sheep with sauce.").group())



'''dot-star character.'''
# dot - any single value(except a new line), star - zero or more.
nameRegex = re.compile(r"First Name: (.*) Last Name: (.*)")
mo = nameRegex.search('First Name: Nishkant Last Name: Jain')
print(mo.group(1))
print(mo.group(2))


# using '*' character for one or more.
# \w for any letter , digit symbol
# .character for any wild card character(any other character before "at")
# This character can be used to find ### RHYMING WORDS ### in a given text.
atRegex = re.compile(r'\w*.at')
print(atRegex.findall('The cat in the hat sat on the flat mat splat.'))


'''case insensitive matching'''
dogRegex = re.compile("dog", re.IGNORECASE)
print(dogRegex.search("The dog is a faithfull animal but humans are unfaithfull DoGs.").group())
print(dogRegex.findall("The dog is a faithfull animal but humans are unfaithfull DoGs. Dog, DOG, dog L"))


