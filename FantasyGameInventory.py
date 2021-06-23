'''
    Code to display the items of an "inventory" in a given format.
    Date Created: Jun 02, 2021
    Creator: Nishkant
'''


def disp_inventory(dict):

    print("Inventory:")
    for item in dict.keys():
        print(dict[item], item)


    n_items = 0  #initiallizing a counter for no. of items
    for j in dict.values():
        n_items += j  #adding all the values of the dictionary one by one.
    print("Total number of items: " + str(n_items))

inventory = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}

disp_inventory(inventory)



