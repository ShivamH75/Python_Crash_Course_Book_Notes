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

del fruits[0]

print(fruits)

