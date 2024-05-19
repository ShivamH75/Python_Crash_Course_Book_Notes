# Lists are mutable, i.e. items can be changed
#  Tuples are immutable
#  Tuple syntax: dimensions = (100, 200)
#  Understand with example; Lists can be helpful for building menu items of Hotel, where items keeps on changing.
#  Tuples can be used to build menu of Restaurant, where menu items are fixed.

# 1. Tuple Syntax
restaurantMenu = ("Samosa", "Pakora", "Aloo Tikki", "Papdi Chaat", "Dahi Vada")

# 2. print items of Tuple 
print(restaurantMenu)
print(restaurantMenu[0])
print(restaurantMenu[3],'\n')

# 3. Looping through Tuple
for food in restaurantMenu:
    print(food)

# 4. to change the tuple, we have to again redefine it 
print("Old Menu: ", restaurantMenu)

restaurantMenu = ("Aloo Tikki", "Papdi Chaat", "Dahi Vada", "Samosa", "Pakora")
print("New Menu: ", restaurantMenu)