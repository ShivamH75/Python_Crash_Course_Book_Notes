cars = ['honda', 'suzuki', 'ducati']

for car in cars:
    if car == 'honda':
        print("honda is present in the cars list!")
cars = ['honda', 'suzuki', 'ducati', 'bmw']

for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())

# Output >>
# Honda
# Suzuki
# Ducati
# BMW

# The first car in the list is 'honda'. Since it is not equal to 'bmw', the else branch of the if statement is executed. car.title() converts the string to title case, where the first letter is capitalized and the rest are lowercase. Therefore, the output is 'Honda'.

# The second car is 'suzuki', which is also not equal to 'bmw'. Hence, the else branch is executed again, resulting in the output 'Suzuki'.

# The third car is 'ducati', and as before, it is not equal to 'bmw'. The else branch is executed, producing the output 'Ducati'.

# The last car in the list is 'bmw', which matches the condition car == 'bmw'. Consequently, the if branch is executed. car.upper() converts the string to uppercase, resulting in the output 'BMW'.

#  each items is iterated and checked for If/Else condition

#  Q. from a list of usernames, check if entered username matches with the names in the list. Consider that entered username is checked without considering upper/lower cases in it.
#  Q. have a standard list of pizza toppings. take a list of toppings from customer. compare both lists. inform chef to add which toppings if match is found. inform customer if match is not found from both the list.

# dominos_toppings = ['onion', 'tomato', 'mushroom', 'capsicum']

# my_toppings = ['onion', 'tomato']

# if my_toppings in dominos_toppings:
#     print("your pizza is ready with toppings")
# else:
#     print("not available")


# ____________________________________________________________________________________________________________
#  check if a value is present in the list. use keyword = 'in'
dominos_toppings = ['onion', 'tomato', 'mushroom', 'capsicum']
my_requested_topping = 'onion'

if my_requested_topping in dominos_toppings:
    print(f"{my_requested_topping.title()} is present in the Menu")

# ____________________________________________________________________________________________________________
#  check if a value is not present in the list. use keyword = 'not'
my_requested_topping = 'pineapple'

if my_requested_topping not in dominos_toppings:
    print(f"{my_requested_topping.title()} is not present in the Menu")

# ____________________________________________________________________________________________________________
#  if-elif-else ladder to determine stage of a person as per his age
# <2 baby;  2-4 toddler; 4-13 kid; 13-18 teenager; 18-65 elder; 65+ elder
# user_age = int(input("Enter your age: "))

# if (user_age < 2):
#     stage = 'baby'
# elif (user_age < 4):
#     stage = 'toddler'
# elif (user_age < 13):
#     stage = 'kid'
# elif (user_age < 18):
#     stage = 'teenager'
# elif (user_age < 65):
#     stage = 'adult'
# else:
#     stage = 'elder'

# print(f"Your stage of life is {stage.title()}")


# ____________________________________________________________________________________________________________
#  way to check values of one list are present in sencond list
dominos_toppings = ('onion', 'tomato', 'cheese', 'mushroom', 'capsicum')    #can be made as set, as toppings list is fixed and non-modifiable by dominos

my_requested_toppings = ['onion', 'chillie', 'tomato', 'paneer', 'cheese']

# use for loop to iterate each item
for my_topping in my_requested_toppings:
    if my_topping in dominos_toppings:
        print(f"Adding {my_topping} on pizza")

    else:
        print(f"Sorry {my_topping} is not available")
print("Finished making your pizza!!")
```
