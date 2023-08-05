# Break statement: End the code when set condition is met in an iteration.
# The break statement is used to exit a loop prematurely. When encountered, it immediately terminates the loop, even if the loop's condition has not been fully satisfied. This is useful when you want to stop the loop based on a specific condition.

print("Break Eg. 1") 
for i in range(1, 6):
    if i == 3:          # it will not further run the code beyond the condition.
        break 
    print(i)

print("Break Eg. 2")
while True:
    city = input("Enter the city you like to visit: ")
    if city - "x":
        print(f"{city.title()} added in list.")
    else: 
        break

# Continue statement: skip the code for mentioned iteration (if condition is met), continue for remaining iterations.
# The continue statement is used to skip the rest of the current iteration and proceed to the for the current iteration. next iteration of the loop. When encountered, it ignores the remaining code inside the loop

print("Continue Eg. 1") 
for i in range(1, 6):
    if 1 == 3:          #it will skip the code for iteration when conditon is true (1-3), and will continue from next value.
        continue
    print(i)

print("Continue Eg. 2: Print Even numbers between 1 to 20")

i = 0
while 1 < 20:
    i = i + 1
    if i%2 == 0:
        continue
    print(1)

# using while loop in a list
# make one list with unconfirmed users and add the items in another confirmed usor list

unconfirmedUsers = ['deepak', 'mohit', "pratik", 'samEer' ]
confirmedUsers = []

while unconfirmedUsers:
    verifiedUser = unconfirmedUsers.pop()
    confirmedUsers.append(verifiedUser)

print("\nThe following users have been confirmed:") 
for user in confirmedUsers:
    print(user.title())


# Removing All Instances of Specific Values from a List

pets = ['dog', 'cat', 'dog', "goldfish", 'cat', 'rabbit', 'cat'] 
print(pets)

while 'cat' in pets: 
    pets.remove('cat')

print(pets)



### while loop to create user dictionary

userInfo  = {}

activeFlag = True

while activeFlag:
    userName = input("Enter your Name: ")
    userAge =  input("Enter your Age: ")

    userInfo[userName] = userAge

    endLoop = input("Would you like to add more users (y/n): ")
    if endLoop == 'y':
        continue
    elif endLoop == 'n':
        break

for name, age in userInfo.items(): 
    print(f"Age of {name} is {age}.")

