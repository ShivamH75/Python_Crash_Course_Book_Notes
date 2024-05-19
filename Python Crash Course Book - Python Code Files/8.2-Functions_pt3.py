## Passing list to the function

def greetUser(names):           #here we model the parameter as a list
    "function to greet individual member of a list"
    for name in names: 
        print (f"Hello, {name.title()}")


boyNames = ['amol', 'pratik', 'santosh'] 
girlNames = ['maya', 'riya', 'geeta']

greetUser(boyNames)         # we have passed list as a argument in the function 
greetUser(girlNames)


## Modifying a List in a Function 

def formatterFunction(ogList): 
    '''function that converts elements of list into title case'''
    sampleList = []
    while ogList:
        current_design = ogList.pop()
        format_design = current_design.title()
        sampleList.append(format_design)
        
    return sampleList[::-1]                     # [::-1] for returning a list as Reversed


original_list = ['Hello', 'HeYY', 'holla'] 
print (original_list)

formatted_list = formatterFunction (original_list)
print (formatted_list)

#Preventing a Function from Modifying a List

originalAnimals = ['cat', 'dog', 'tiger', 'fox'] 
print (originalAnimals)

sampleVar = formatterFunction(originalAnimals[:]) # way of passing copy of our list- functionName (listName[:]) 
print(sampleVar)

print (originalAnimals)         #original list is not affected