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



# # Mixing Positional and Arbitrary Arguments
# it is suggested to use positional, relational and then any other type of arguments

# eg. function to recieve fixed info in one parameter, and arbitrary info in another parameters
def mixedPizza(size, category, *toppings):
    print(f"Your {size} sized {category} pizza has following toppings: ")
    for topping in toppings:
        print(topping.title())

mixedPizza('medium', 'veg', 'capsicum', 'olive', 'chillie')
# # here, the first 2 arguments acts as positional arguments, later all followed by Arbitrary
# however, if we use relational arguments with Arbitrary arguments, we get error - SyntaxError: positional argument follows keyword argument


## Using Arbitrary Keyword Arguments
# consider for storing key-value type data in dict, there is a case that some pairs are known, but many k-v pairs can be Arbitrary. 
# so we use "Arbitrary Keyword Arguments", which has two * before the parameter name

# def userDict(name, surname, **allOther):
#     newDict = {}
#     name = input("Enter your name: ")
#     surname = input("Enter your surname: ")
#     anyOtherInfo = input("Do you wanted to add any other info (y/n)? ")
#     if anyOtherInfo == 'y':
#         newInputField = input("Add field name: ")
#         newInputValue = input("Add field value: ")
#     else:
#         print("thank you")

#     newDict['name'] = name
#     newDict['surname'] = surname     .................... practice problem

def build_profile(first, last, **user_info):
    """Build a dictionary containing everything we know about a user."""
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info                         #returns all other values as dict


user_profile = build_profile('albert', 'einstein', location='princeton',field='physics')
print(user_profile)
# positional args will be displayed at the end in the o/p

