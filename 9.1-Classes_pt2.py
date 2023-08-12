# Working with Classes and Instances
# You can modify the attributes of an instance directly or write methods that update attributes in specific ways.

class Car:
    '''sample class to experiment with'''
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def get_desName(self):
        long_name = f"{self.year}  {self.make} {self.model}"
        return long_name

my_car = Car('audi', 'r8', 1999)      
print(my_car.get_desName())
        

# 1. Setting a Default Value for an Attribute
# default value can be set to attribute in the init method itself

class Pizza:
    def __init__(self, size, cheese):
        self.size = self
        self.cheeze = cheese
        self.base_price = 100           #here default value is set to an attribute

    def get_price(self):
        print(f"Base price of any pizza is {self.base_price}")


my_pizza = Pizza('small', 'mozzeralla')
my_pizza.get_price()


# # 2. Modifying Attribute Values
# three ways to change an attribute’s value: 
# i. you can change the value directly "through an instance"
my_pizza.base_price = 150
my_pizza.get_price()

# ii. set the value through a method
#  pass the new value to a method that handles the updating internally

class Pizza2:
    def __init__(self, size, cheese):
        self.size = self
        self.cheeze = cheese
        self.base_price = 100

    def updatePrice(self, newPrice):
        '''method to change the parameter of previous method'''
        self.base_price = newPrice

    def increasePrice(self, increamentalValue):
        '''method to add increament to original base price'''
        self.base_price = self.base_price + increamentalValue 


    def get_price(self):
        print(f"Base price of any pizza is {self.base_price}")

myPizza = Pizza2(12, 'shredder')
myPizza.updatePrice(200)                #pass the new value through a method
myPizza.get_price()

# iii. increment the value (add a certain amount to it) through a method. 
myPizza2 = Pizza2(12, 'shredder')
myPizza2.updatePrice(200)                #pass the new value through a method
myPizza2.get_price()

myPizza2.increasePrice(10)      # incremental value to add in base value
myPizza2.get_price()
