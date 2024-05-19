## A function is a Reusable block of code which only runs when it is called.
# You can pass data, known as parameters, into a function. 
# A function can return data as a result.

# Structure of a function 
def greetUser():
    '''docString: a comment which tells what does the function do'''
    print("Hello User")         # actual useful/working code

greetUser() # 'function call: function is called with necessary arguments in the brackets.

#'def' is the function definition. It tells name of the function and () holds the type of information it holds.
# code beside the indentation is the 'body' of the function.

def greetUserWithName (name):   # NOTE: what we pass in function definition is "PARAMETER" 
    """pass parameter in the function"""
    print (f"Hello, {name.title()}.")

greetUserWithName('rohan')      # NOTE: what wepass in function call is "ARGUMENT"
greetUserWithName('deepak')
greetUserWithName('rahul')


## Ways to pass arguments in a function call 
# 1. positional arguments: the sequence of passing arguments must match the sequench in which the parameters are passed

def showUserInfo(name, age, city): 
    print(f"My name is {name.title()}. My age is {age} years. I live in {city.title()} city.")

showUserInfo('shivam', 23, 'nashik')

# 2. 'keyword' argument: we can pass arguments while mentioning their parameters. no need to worry about sequence.

showUserInfo (name="shivam", city ="MUMBAI", age=23)


# Default Values: we can obtain values from the arguments in the parameter itself

def petInfo(petName, petType="dog"): 
    print(f"Hello, i have a {petType}, whose name is {petName}")

petInfo('rocky')                    #if 'petType' is not passed, default value from parameter will be set in argument. 
petInfo('silvester', 'cat')         #if value is passed, then it will be used.

#NOTE: here, order of the parameters is very important. use parameters without default value before, then mention parameters with default value. # we can call function by various ways. (positional, relational, default) calls.

