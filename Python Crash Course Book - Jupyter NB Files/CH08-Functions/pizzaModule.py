class Pizza:
    def __init__(self, size, category):
        self.size = size
        self.category = category

    def showToppingList(self):
        '''method to print available toppings as per category of pizza'''
        if self.category == 'veg':
            print("Available VEG Toppings: Paneer, Onion, Mushroom")
        elif self.category == 'nonveg':
            print("Available NON-VEG Toppings: Egg, Pepperoni, Chicken")

    def pizzaCost(self):
        '''print pizza cost as per pizza size'''
        if self.size == 'small':
            print(f"{self.size.title()} Pizza cost is 100 Rs.")
        elif self.size == 'medium':
            print(f"{self.size.title()} Pizza cost is 150 Rs.")
        elif self.size == 'large':
            print(f"{self.size.title()} Pizza cost is 200 Rs.")


# myPizza = Pizza('small', 'veg')

# myPizza.pizzaCost()
# myPizza.showToppingList()