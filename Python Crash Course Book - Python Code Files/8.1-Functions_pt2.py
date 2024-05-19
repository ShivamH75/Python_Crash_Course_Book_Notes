# Return value: the value that the function returns after processing.

def nameFormatter (firstName, lastName):
    """function to return full name in title case"""
    return (f"{firstName.title()} {lastName.title()}")

print(nameFormatter('amol', 'SiNgH'))

# Making an Argument Optional
#we can include additional parameters in function, which might not be always required by user in arguments

def fullName(first, last, middle=''):           # optional parameter is defined as in 
    """return full name of the user, middle name is optional"""
    if middle:
        return(f"{first} {middle} {last}") 
    else: 
        return(f"{first} {last}")

    # return(f" {first} {middle} {last}")       # will get 2 spaces if middlename is not mentioned

print (fullName('akash', 'bodke'))
print (fullName('akash', 'bodke', 'mohan'))
       

# return a dictionary from function 
def returnDict(name, middleName, lastName):
    dict1 = {}
    dict1['First Name'] = name 
    dict1['Middle Name'] = middleName
    dict1['Last Name'] = lastName
    return dict1

newDict = returnDict('shivam', 'ashok', 'hundekari') 
print(newDict)

# return a dictionary from function - use optional parameter

def returnDict(name, middleName, lastName, age = None): 
    """age as optional parameter"""
    dict1= {}
    dict1['First Name'] = name 
    dict1['Middle Name'] = middleName
    dict1['Last Name'] =  lastName

    if age:
        dict1['Age'] = age          # use if-else if optional parameter exists

    return dict1

newDict = returnDict('shivam', 'ashok', 'hundekari')
print (newDict)


#while loop in a function

def getName(): 
    while True:
        print("please provide your info. press q to quit.") 
        name = input("Enter your Name: ")
        if name == 'q':
            break
        surname = input("Enter your Surname: ") 
        if surname == 'q':
            break
        
        print(f"Hello, {name.title()} {surname.title()}")
        

getName()       #function runs as a while loop
