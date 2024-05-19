# # **INHERITANCE**
# If the class you’re writing is a specialized version of another class you wrote, you can use inheritance. 
# When one class inherits from another, it takes on the attributes and methods of the first class. 
# The original class is called the parent/super class, and the new class is the child/sub class. The child class can inherit any or all of the attributes and methods of its parent class, but it’s also free to define new attributes and methods of its own.

class Car:
    """A simple attempt to represent a car."""
    def __init__(self, make, model, year):
        """Initialize attributes to describe a car."""
        self.make = make
        self.model = model
        self.year = year

    def getCarDetails(self):
        '''method to describe a car'''        
        print(f"| CarName: {self.model} | CarBrand: {self.make} | CarYear: {self.year} |")

myCar = Car('Honda', 'City', 2008)
myCar.getCarDetails()

#creating a new child class from original parent class
class ElectricCar(Car):
    def __init__(self, make, model, year):
        """Initialize attributes of the parent class."""
        super().__init__(make, model, year)       
        # The super() function is a special function that allows you to call a method from the parent class. 
        # This line tells Python to call the __init__() method from Car, which gives an ElectricCar instance all the attributes defined in that method.    
              
        # self.power = power                              # child class can also have its own attribute

    def evSpecialMethod(self, batteryCapacity):
        self.batteryCapacity = batteryCapacity
        print(f"Battery capacity of {self.make}-{self.model} ({self.year}) is {batteryCapacity} kW-Hr.")

myEV = ElectricCar('Nissan', 'Leaf', 2023)

myEV.getCarDetails()        #instance created from child class can use all the methods of parent class

myEV.evSpecialMethod(150)       # child class can have its own methods


# ---------------------------------------------------------------------------------------------------
## Overriding Methods from the Parent Class
# consider there is one method in parent class, which is not useful in child class.
# to override the parent class method, simply create new method in child class with same name
#  priority will be given to method of child class, if instance is created from child class.

class Pizza:
    def __init__(self):
        pass

    '''method needs to be defined as static methods using the @staticmethod decorator, since they don't need to access "instance-specific" attributes.'''
    @staticmethod
    def VegMenu():
        print("Options for Veg toppings: Paneer, Onion, Mushroom")
    
    @staticmethod
    def NonVegMenu():
        print("Options for Non-Veg toppings: Chicken, Bacon, Papperoni")

class VegPizza(Pizza):
    def __init__(self):
        super().__init__()

    @staticmethod
    def NonVegMenu():
        print("Strictly veg toppings..")

myPizza = VegPizza()

myPizza.NonVegMenu()



# _________________________________
# Instances as Attributes
#  You can break your large class into smaller classes that work together; this approach is called "composition".
#  If we find that we are adding more attributes and methods to one class only, we can create seperate class for it.
## use case: we created ElectricCar class, and wanted to use Battery class in it. which is specific.

class Battery:
    def __init__(self, capacity = 35):
        self.capacity = capacity

    def BatCapacity(self):
        print(f"Capacity of battery is {self.capacity} kW-Hr.")

    def getRange(self):
        if self.capacity <= 50:
            print(f"For battery capacity {self.capacity} kW-Hr, range is 100 miles")
        else:
            print(f"For battery capacity {self.capacity} kW-Hr, range is 200 miles")



class EleCar(Car):
    def __init__(self, make, model, year):

        super().__init__(make, model, year)
        self.capacity = Battery()
        '''self.capacity is an attribute, which is assigned as a new instance of Battery() class'''


myLeaf = EleCar("Tesla", "Roadster", 2021)

myLeaf.getCarDetails()
myLeaf.capacity.BatCapacity()           #syntax: instanceName.attributeName.methodName()
myLeaf.capacity.getRange()


# ________________________________________________________________________________________
# Importing Classes
# 1. Importing a Single Class
# step 1: create a seperate file, include the parent class in it 
# step 2: in the working file, import the required class - 
# from <moduleName> import <className>
# step 3: create instance, assign attributes to it
# step 4: assign methods to the instance

# Storing Multiple Classes in a Module - multiple classes can be stored in same file, even if they are of parent-child type

# 2. Importing Multiple Classes from a Module
#  syntax: from <moduleName> import <class1Name>, <class2Name>, <class3Name>

# 3. Importing an Entire Module
#  syntax: import <moduleName>

# 4. Importing All Classes from a Module            # methid not recommended
#  from <moduleName> import *                  # asterick imports all the classes 

# 5. Importing a Module into a Module
# (look more in details)                e.g. below
# from car import Car
# from electric_car import ElectricCar


## Using Aliases - can be used if conflict exists in file names
# from <moduleName> import <className> as <classAliasName>