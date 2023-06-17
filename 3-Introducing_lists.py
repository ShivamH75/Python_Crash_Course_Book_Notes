# list example 

fruits = ["apple", "banana", "mango"]

print(fruits)   #if list is print directly, it prints with quotations and brackets

print(fruits[0])    # prints 0th element of list

# Add elements to the list
# 1. add at last - AppEND 

fruits.append("cherry") #append is inbuilt function to add elements at last. function is added at last of variable name.
print(fruits)

# 2. modify elements of the list

fruits[0] = "Jackfruit"     #replaces the 0th element
print(fruits)

# 3. Insert element in the list without deleting already present elements 
# syntax: list_name.insert(index, "element name")
fruits.insert(2, "Strawberry")

print(fruits)

# 4. Delete element from list by its Index

del fruits[0]           #this can also delete whole variable

print(fruits)

# 5. Remove item by its position - POP()

bikes = ["yamaha", "honda", "bajaj", "ducati"]

removedBike = bikes.pop(1)              
#removes element at 1th place. if nothing is mentioned in (), then 0th element will get popped up

print(bikes)
print(removedBike)          #removed element can be stored 

# 6. Remove item by its value
bikes.remove("bajaj")
print(bikes)

## ORGANIZING A LIST
cars1 = ["bmw", "ford", "audi", "honda", "toyota", "lambo"]

# 1. Sort list PERMANENTLY 
cars1.sort(reverse=False)        #to sort in reverse, put "False"

print(cars1)
# use another variable for not losing original order of list elements

# 2. Sort list TEMPORARILY
cars2 = ["bmw", "ford", "audi", "honda", "toyota", "lambo"]

print("Here is temporarily sorted list- ", sorted(cars2))
print ("Here is original list again -", cars2)

# NOTE: Sort will not work properly if some elements are with lowercase and some with uppercase

# 3. Print list in reverse
cars2.reverse()
print(cars2)

# 4. Find number of elements of list
print(len(cars2))

