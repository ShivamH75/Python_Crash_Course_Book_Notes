#  Sometimes you’ll want to store multiple dictionaries in a list, or a list of items as a value in a dictionary. This is called NESTING. 
# we can Nest list in dict, dict in list, dict in dict
# listEg= ['tom', 'jerry'] # dictEg { "name": "tom", "age" : 3)

# import random
# num random.randint(1,3)
# aliens = []       # create a empty list

# alienGreen = {"color":"green", "speed":"slow", "points":5}
# alienYellow = {"color":"yellow", "speed":"medium", "points":10}
# alienRed = {"color":"red", "speed": "fast", "points":15}

# for alien in range(30):
#     num = random.randint(1,3)
#     if num == 1:
#         aliens.append(alienGreen)
#     elif num == 2:
#         aliens.append(alienYellow)
#     else:
#         aliens.append(alienRed)

# for alien in aliens:
#     print(alien)

28 # 1. List of Dictionaries
aliens = []        # create a empty list

for alien in range(30):     # range function to run loop for 30 times
    alien = {"color": "green","speed":"slow", "points":5}   
    aliens.append(alien)        # add the alien to the list

    for alien in aliens [0:3]: # change properties of first 3 aliens to yellow
        if alien['color'] == 'green':
            alien['color'] = 'yellow'
            alien['speed'] = 'medium'
            alien['points'] = 10

for alien in aliens[:5]:
    print(alien)

# 2. List in a Dictionary
# list can be nested in a diectionary when we want multiple values to be stored as a value for a key

pizza = {
    'crust': 'medium',
    'toppings': ['pineapple', 'mushroom', 'olive']
    }
print (f"You have ordered {pizza['crust']}-crust pizza with following toppings: ")

for topping in pizza['toppings']:
    print(topping)


# another example
fav_lang = {
    'shivam' : ['python', 'c', 'c++'],
    'akash': ['java'],
    'tejas': ['javascript']
    }

for name, lang in fav_lang.items():
    if len(lang) == 1:
        print("Favourite language of {name} is: ")
        for lan in lang:
            print(lan)
    else:
        print(f"Favourite languages of {name} are: ")


# 3. A Dictionary in a Dictionary
# e.g. dictionary of users (key) with their info multiple items.

userData = {
    'shivam11' : {
        'FirstName' : 'Shivam',
        'LastName': 'Hundekari',
        'Age': 23
},
    'rahu187' : {
        'FirstName' : "Rahul",
        'LastName': 'Sutar',
        'Age' : 24
    }
}

for username, userinfo in userData.items(): 
    print("\nUsername of person is {username} with following details:")

    for infokey, infoValue in userinfo.items():
        print(f"{infokey} {infoValue}")


# Another method to print data of dict inside dict
for username, user_info in userData.items():    #user_info is dict and we loop through it
    print(f"\nUsername: {username}") 
    full_name = f"{user_info['FirstName']}"
    age = user_info['Age']
    print (f"\tFull name: {full_name.title()}") 
    print (f"\tAge: {age}")