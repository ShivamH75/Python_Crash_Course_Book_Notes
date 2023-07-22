# Looping Through All KEY-VALUE Pairs
# Looping through all key-value pairs works particularly well for dictionaries which stores the same kind of information for many different keys. 
sample_dict = {
    'name': 'John Doe',
    'age': 30,
    'city': 'New York',
    'email': 'johndoe@example.com',
    'is_employed': False
}

for key, value in sample_dict.items():      # method 'items()' is used in dictionaries to return sequence of key-value pairs
    print(f"\nKey = {key}")
    print(f"Value = {value}")

favLanguages = {
    'john' : 'ruby',
    'steven' : 'peaRl',
    'shivam' : 'pyThOn'
} 

for user, lang in favLanguages.items():
    print(f"Favourite language of {user.title()} is {lang.title()}")

# _________________________________________________________________
#  Looping Through All the KEYS in a Dictionary
favLanguages1 = {
    'john' : 'ruby',
    'steven' : 'peaRl',
    'shivam' : 'pyThOn',
    'sachin' : 'c',
    'pratham' : 'c++',
    'rohan': 'java',
    'manoj' : 'assembly',
    'pravin' : 'cotlin',
    'PranaY' : 'javascript',
    'rishikesh' : 'ABab'
} 

# print names of all the keys
for name in favLanguages1.keys():
# for name in favLanguages1:        #This will give same output, because keys is the default behaviour when looping through dictionary
    print(name)

# Work with keys, conditionally obtain input if key is present in dictionary
friends = ['shivam', 'manoj']
for name in favLanguages1.keys():
    print(f"Hello {name}!!")

    if name in friends:
        print(f"Ohh, {name}!! it seems your fav lang is {favLanguages1.get(name)}")

# 'keys()' method also returns sequence of keys
seq = 1
for name in favLanguages1.keys():
    print(f"{seq}. {name.title()}")
    seq = seq + 1

for name in sorted(favLanguages1.keys()):      #print keys in ascending order
    print(f"{seq}. {name.title()}")
    seq = seq + 1


# _________________________________________________________________
#  Looping Through All the VALUES in a Dictionary
