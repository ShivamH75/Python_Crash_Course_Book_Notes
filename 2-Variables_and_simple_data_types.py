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