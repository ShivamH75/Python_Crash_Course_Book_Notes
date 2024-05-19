# input() function : take input from user and assigns it to defined variable ## structure- varName = input("Enter text that user can read corresponding with action: ")

#1. directly enter prompt message in input() 
name = input("Hello, enter your name: ")

# 2. user prompt variable inside input(), incase the message is lengthy 
prompt = "This is survey. User needs to enter name for registration." 
prompt += prompt + "\nPlease Enter your name: "

name= input (prompt)

## integer as input. int value is taken as string. need to convert it in order to perform logical operations

birthYear = input("Enter your Birth Year: ")
birthYear = int(birthYear)

from datetime import datetime 
currentYear = datetime.now().year
## other attributes of 'datetime' object - month, day, hour, minute, second, microsecond

print("Your age is: ", abs(birthYear-currentYear))
# abs() method returns the non-negative value

## Modulo operator: divides one number by another and returns the remainder 

def evenORodd(num):
    if (num%2) == 0: return("Given number is Even.")    # have used 'return' here, check why 'print' was giving 'None'
    else:
        return("Given number is odd")

print(evenORodd(61))