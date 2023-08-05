# Passing an Arbitrary Number of Arguments (Arbitrary meaning - random choice, any)
# Arbitrary means user can pass any number of arguments against 1 defined parameter
# use the asterisk (*) before the parameter name  

def pizzaToppings(*toppings):
    print("your pizza has these toppings: ")
    print(toppings)

pizzaToppings('onion')
pizzaToppings('olive', 'cheese')

# # the arguments are put inside a set by Python
# op ->   ('olive', 'cheese')

# to print the each Arbitrary argument
def pizzaToppingList(*toppings):
    print('Your pizza has the following toppings: ')
    for topping in toppings:
        print(topping.title())

pizzaToppingList('onion')
pizzaToppingList('olive', 'cheese', 'capsicum', 'mushroom')
