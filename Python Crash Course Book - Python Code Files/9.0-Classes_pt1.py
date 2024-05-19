# class is a real world thing or a situation
# objects are instances of a class
# Making an object from a class is called instantiation

class Dog:      #'Dog' is a real world object. so we can make class of it.
                # Dog has info like name, age. It forms attributes. 
                # Dog can bark, run. So it forms the methods. (a function which is part of a class is called as Method)

    def __init__(self, name, age):  # this is a special method that runs when instances         are created of a class. self parameter is required in the method definition.
        # __init__() method initializes the name,age attributes.
        self.Name = name    # 'self.Name' takes the value associated with 'Name' and assigns it to instance being created (name).
        self.Age = age 
        #  Variables that are accessible through instances are called attributes.

    def sit(self):          # this is a method of class 'Dog'. No need to seperately add all the parameters.
        print(f"Dog {self.Name} will sit.")

    def bark(self):
        print(f"my dog {self.Name} is barking... bow..bow..")


#  Making an Instance from a Class 
myDog = Dog('tommy', 12)      #we added class to a variable and defined the arguments. 
#  'myDog' is an instance created  from 'Dog' class

print(f"{myDog.Name.title()} is my dog. His age is {myDog.Age}.")
#  to use attributes of instance, use dot notation - myDog.Name


## Calling Methods
myDog.sit()         # syntax: instance_name.method_name
# After we create an instance from the class Dog, we can call any method defined in Dog. 

my_2nd_dog = Dog('julie', 6)        # we can create multiple instances from a class

my_2nd_dog.bark()




# Practice problem
#  Restaurant: Make a class called Restaurant. The __init__() method for Restaurant should store two attributes: a restaurant_name and a cuisine_type. Make a method called describe_restaurant() that prints these two pieces of information, and a method called open_restaurant() that prints a message indicating that the restaurant is open.Make an instance called restaurant from your class. Print the two attributes individually, and then call both methods.

class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        '''method to initialize the attributes'''
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"Name of the Restaurant: {self.restaurant_name}")
        print(f"Type of the Cuisine: {self.cuisine_type}")

    def open_restaurant(self):
        print(f"Restaurant {self.restaurant_name} is now Open!")

# creating the instances 
Res1 = Restaurant('Green Leaf', 'Continental')

Res1.describe_restaurant()
Res1.open_restaurant()


