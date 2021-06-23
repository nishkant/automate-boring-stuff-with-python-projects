'''
    Adding items of a list to a dictionary.
    Created: Jun 03, 2021
    Creator: Nishkant
'''


from FantasyGameInventory import disp_inventory #importing the function of prev program

dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
inventoryy = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}  #initiall dictionary

def addToInventory(inventory, addedItems):

    ##############################################
    # Doubt:after using below two lines the loop was not working properly
    # Status: Unsolved
    # inventory = dict(inventory)
    # addedItems = list(addedItems)
    ##############################################
    for x in addedItems:
        if x in inventory:
            inventory[x] += 1  
        else:
            inventory[x] = 1

addToInventory(inventoryy, dragonLoot)

disp_inventory(inventoryy)

