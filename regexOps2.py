import re

'''Substituting Strings with the sub() Method'''
namesRegex = re.compile(r'Agent \w+')  #"\w+" for one or more character.
print(namesRegex.sub('CENSORED', 'Agent Alice gave the secret documents to Agent Bob.'))


# denoting groups in sub method 
# we can use \1,\2,\3 to denote first second third etc group in regex expression
agentNamesRegex = re.compile(r'Agent (\w)\w*')
print(agentNamesRegex.sub
(r'\1****', 'Agent Alice told Agent Carol that Agent Eve knew Agent Bob was a double agent.'))



'''managing complex expressions'''
phoneRegex = re.compile
(r'((\d{3}|\(\d{3}\))?(\s|-|\.)?\d{3}(\s|-|\.)\d{4}(\s*(ext|x|ext.)\s*\d{2,5})?)')

phoneRegex = re.compile(r'''
((\d{3}|\(\d{3}\))?  #area code
(\s|-|\.)? # seperator
\d{3}  # first 3 digits
(\s|-|\.) # seperator
d{4} # 4 digits
(\s*(ext|x|ext.)\s*\d{2,5})?) # extension
''', re.VERBOSE)




