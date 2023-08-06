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



# few ideas for pratice:

def returnValue(dictName, keyName):
    '''function to return value of argument key'''
    return dictName.get(keyName)

# 1. **Calculate Pizza Price:** Create a function that takes the size of the pizza, the number of toppings, and any special requests as parameters and calculates the total price of the pizza. You can define a base price for different sizes and add an extra cost for each topping.

def calculate_pizza_price(size, *Toppings):

    basePrice = 100
    availableSize = {'small': 100, 'medium': 150, 'large': 200}
    boxCost = {'small': 10, 'medium': 15, 'large': 20}

    sizeCost = returnValue(availableSize, size)
    packingCost = returnValue(boxCost, size)
    toppingCost = len(Toppings) * 5

    print(f"You have ordered {size} sized pizza with following toppings: {Toppings}")
    print(f"Final Pizza Cost: ",basePrice + sizeCost + toppingCost +  packingCost)

# calculate_pizza_price('small', 'onion', 'olive')



# 2. **Display Menu:** Write a function that displays a menu of different pizza options along with their descriptions and prices. You can use dictionaries or lists to store the menu items and details.

# display_menu


# 3. **Order Tracker:** Build a function that simulates an order tracker for a pizza place. Users can place orders, and the function can keep track of the order status (cooking, out for delivery, delivered).

# track_order_status


# 4. **Pizza Recommendation:** Create a function that takes the customer's preferred crust type, toppings, and dietary restrictions as inputs and recommends a pizza option that suits their preferences. You can use conditional statements to match preferences to available options.

# recommend_pizza


# 5. **Ingredient Inventory:** Develop a function that manages the inventory of pizza ingredients. You can have functions to add ingredients, remove ingredients, and check the current stock of each ingredient.

# manage_inventory


# 6. **Pizza Cutter:** Design a function that takes the size of a pizza and the number of slices desired, and calculates the angle at which the pizza should be cut to achieve equal slice sizes.

# calculate_pizza_cutting_angle


# 7. **Pizza Party Planner:** Build a function that helps plan a pizza party. Given the number of guests and the average number of slices each person eats, calculate how many pizzas need to be ordered.

# plan_pizza_party


# 8. **Discount Calculator:** Create a function that calculates the final price of a pizza order after applying discounts. You can have different discount rules based on the total order amount or specific promotions.

# calculate_discounted_price


# 9. **Specialty Pizza Creator:** Write a function that lets the user create their own specialty pizza by choosing crust type, sauce, cheese, and toppings. The function can then display the custom pizza details.

# create_specialty_pizza


# 10. **Calories Counter:** Develop a function that takes a list of toppings as input and calculates the estimated total calories in a pizza based on the toppings selected.

# calculate_calories

