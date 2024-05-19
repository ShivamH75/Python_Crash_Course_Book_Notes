# LIST SLICING : lists[m:n]
fruits = ['0apple', '1banana', '2orange', '3grape', '4watermelon', '5kiwi', '6pineapple', '7mango', '8strawberry', '9pear']

# 1. slice list from mth to nth element
fruits1 = fruits[2:7]       #7th element will not printed
print(fruits1)

# 2. slicing list from FIRST to nth element
fruits2 = fruits[8:]
print(fruits2)

# 3. slicing list from nth to LAST element
fruits3 = fruits[5:]
print(fruits3)

# 4. slicing list from 3rd last to LAST element
fruits4 = fruits[-3:]
print(fruits4)

#  SLICING in for LOOP:
food_items = ['pizza', 'burger', 'sushi', 'pasta', 'taco', 'salad', 'steak', 'ramen', 'fried chicken', 'ice cream']

print("first 3 foods in the list are: ")
for food in food_items[0:3]:
    print(food)

#  COPYING a LIST
my_cars = ['Toyota', 'Honda', 'Ford', 'Chevrolet', 'BMW']
your_cars = my_cars[:]     
 #if copied without [:], same data will get added in next operations

my_cars.append("Audi")
your_cars.append("Hyundai")

print(my_cars)
print(your_cars)