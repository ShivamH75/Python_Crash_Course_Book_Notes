def returnValue(dictName, keyName):
    '''function to return value of argument key'''
    return dictName.get(keyName)

availableSize = {'small': 100, 'medium': 150, 'large': 200}
# print(returnValue(availableSize, 'large'))

availableToppings = ['paneer', 'olive', 'mushroom', 'q']

print(len(availableToppings))

toppingCost = len(availableToppings) * 5

