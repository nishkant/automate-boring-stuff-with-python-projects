'''
    A code to print table data in justified format.
    Created: Jun 14, 2021
    Creator: Nishkant
'''

tableData = [['apples', 'oranges', 'cherries', 'banana'],
 ['Alice', 'Bob', 'Carol', 'David'],
 ['dogs', 'cats', 'moose', 'goose']]

def printTable(list):

    # recording the largest length string in each sublist acc. to which whole column will be justified.
    colw = [] # list for storing the same.
    for index in range(len(list)):
        length = [] # initiallizing a list for each sublist.
        for subindex in range(len(list[index])):
            length.append(len(list[index][subindex])) # appending length of all the strings in it.
        a = max(length) # selecting the max one.
        colw.append(a)  # appending it in a list.

    # now printing the justified text.
    # as we have to print 1st element of each sublist in 1st row an so onn..
    # ..thus the sublist loop will be outside.
    for subindex in range(len(list[index])):
        for index in range(len(list)):
            print(list[index][subindex].ljust((colw[index])), end = " ")
        print() # adding a new line after each row.

printTable(tableData)

# here at first I interpreted the meaning of justification wrong.
# I thought that the no of points specified in the argument will shift the string by that points to...
# right/left side.
# but it is like the string will occupy the space of no. of points or length of the string whcihever...
# ...is max.
#if no. of points > len(string) then the left points will be occupied by the "spaces".