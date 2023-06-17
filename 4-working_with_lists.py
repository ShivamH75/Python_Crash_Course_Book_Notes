# # Looping through lists:
# Print every element of the list

cars = ["bmw", "ford", "audi", "honda", "toyota", "lamborghini"]

for car in cars:
    print(car.upper())
# for every car in 'cars' print the name of the car

# i = 1
# for car in cars:       
#     print(f"{i}. {car}")
#     i = i+1
    
# in range() function to generate sequence of numbers
for num in range (1,10):    # NOTE: last value will not be printed. Suggested to use (last_index + 1) approach
    print(num, end=" ")

# NOTE: The end parameter is set to a space ' ', which ensures that the next item will be printed on the same line with a space separating them.


# Generate numbers with steps:
for num in range (0, 11, 2):        # syntax>> range(first_required_number, last_required_number+1, step_value_for_skip)
    print(num)


# USE RANGE TO GENERATE LIST OF NUMBERS:
numList = list(range(0,11))     #numList variable will get assigned value of List
print(numList)

# Append numbers in the list
emptyList =[]
for nos in range(1,11):
    emptyList.append(nos**2)

print(emptyList)

# find minimum number in list
print(min(emptyList))

# find maximum number in list
print(max(emptyList))

# find sum of all numbers in the list
print(sum(numList))

print('\n')