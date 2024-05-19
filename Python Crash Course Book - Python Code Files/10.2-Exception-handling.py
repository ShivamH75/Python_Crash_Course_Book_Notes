# Exceptions are handled with try-except blocks.
# A try-except block asks Python to do something, but it also tells Python what to do if an exception is raised.

# Handling the ZeroDivisionError Exception
# print(5/0)
'''this will throe - ZeroDivisionError: division by zero'''

try:
    print(5/0)
except:
    print("Not possible to divide any number by zero.!")

try:    # put code that may cause error in 'try' block
    '''user input must be in number only'''
    num = input("Enter your age: ")
    print("You were born in the year: ", 2023 - int(num))

except ValueError:     # mention type of possible error
    print("Enter age in number format only.")


## Using Exceptions to Prevent Crashes
# try block : code that may cause error
# except block : code to dhandle exception, if code in try block fails.
# else : code to keep running the program, if code in try block suceeds.

"""Program to divide 2 numbers, q to quit"""
while True:
    num1 = input("Enter first number: ")
    if num1 == 'q':
        print("thanks for using our code")
        break
    num2 = input("Enter second number: ")
    if num2 == 'q':
        print("thanks for using our code")
        break

    try:
        result = int(num1) / int(num2)
    except ZeroDivisionError:
        print(f"Cannot divide {num1} by {num2}")
    except ValueError:
        print("Enter number only..")
    else:
        print(result)

    

## Handling the FileNotFoundError Exception
from pathlib import Path

folderName = 'text files'
fileName = 'pidigits.tx'
mypath = Path(folderName + '/' + fileName) #this input must go as a whole string
# content3 = mypath.read_text()
# print(content3)

try:
    content3 = mypath.read_text()
except FileNotFoundError:
    print(f'''File "{fileName}" is not found in "{folderName}" to read.''')

'''--------------------------------------------------------------------------'''
# Working with Multiple Files
# create a function that reads number of words from a text file 
def count_words(path):
    try:
        contents = path.read_text()
    except FileNotFoundError:
        print(f"File {path} not found")
        # pass                                # do nothing, when try fails.
    else:
        words = contents.split()
        num_of_words = len(words)
        print(f"File {path} has {num_of_words} number of words.")

path = Path('pizza.py')
count_words(path)           # function call

'''count words in multiple files'''
dict1 = ['pizza.py', 'pizzaModule.py', 'abc.py', 'roughWork.py']

for file in dict1:
    path = Path(file)
    count_words(path)


'''-----------------------------------------------------'''
# Failing Silently - do nothing when try fails
# in the except block, write 'pass'. it will not display any message. Code will continue to run in 'else' block.
'''-----------------------------------------------------'''
