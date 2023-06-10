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