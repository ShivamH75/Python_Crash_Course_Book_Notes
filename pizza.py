def createPizza(size, category='Veg', *toppings):
    '''function to return details of pizza'''
    print(f"You have ordered {category}, {size} inch pizza with following toppings: ")
    for topping in toppings:
        print(f"-{topping}")

# createPizza(12, 'veg', 'onion', 'chillie')

def showToppings(category):
    '''function to display list of toppings based on category of pizza'''
    if category == 'veg':
        print("following toppings are available for Veg pizza: ")
        print("Onion, Capsicum, Tomato, Cheese, Olives")
    elif category == 'nonveg':
        print("following toppings are available for Non-Veg pizza: ")
        print("Egg, Pepperoni, Chicken")
    elif category == 'mixed':
        print("following toppings are available for Mixed pizza: ")
        print("Paneer, Soya")

# showToppings('veg')

