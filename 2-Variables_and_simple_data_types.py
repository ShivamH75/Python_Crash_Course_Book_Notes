# String Methods

string1 = 'sample date For test'

# 1. convert first character of each word into uppercase
print(string1.title())

# 2. convert all characters into uppercase
print(string1.upper())

# 3. convert all characters into lowercase
print(string1.lower())

# 4. F-Strings : Insert variable values into the string
userName = 'Shivam'
userCity = 'Nashik'
convertedFstring = f'{userName} is from {userCity} City'
print(convertedFstring)

# Add Whitespaces (whitespaces means non-printable characters like tabs and spaces)
print('Languages: \n\tPython\n\tJavascript')

# Remove Whitespaces from left and right
string2 = " string with whitespaces on left and right    "
string2_2 = string2.lstrip()
string2_3 = string2.rstrip()

print(string2_3)

# Remove prefixes and suffixes from string
stringWithPrefixAndSuffix = 'https://wikipedia.com'

print(stringWithPrefixAndSuffix.removeprefix('https://').removesuffix('.com'))

# Escape with single or double quotes as a part of string 
print("He said \"Hello\"")
print('He shouted, \'Run!\'')   


# ________________________________________________________________________________
# Numbers 
# 1. To represent power - use double **
print(2**3)         # cube of 2

# 2. calculations take place as per BODMAS rule
print(2 + 5*8 -2)

# 3. int + float combinations
print(4.0/2.0)          # float / float = float
print(4/2)          # int / int = float

# ________________________________________________________________________________
# Misc info 
# 1. Assign multiple variables in a single line
x,y,z = 'Hello', 23, 3.14
print (x,y,z)

# 2. Provide underscre in numbers for better readibility - will get ignored in code
oneCrore = 1_00_00_000
print(oneCrore)

# 3. CONSTANTS - Py dont have inbuilt constant types, but CAPS can be used as good practice
PI_VALUE = 3.14
