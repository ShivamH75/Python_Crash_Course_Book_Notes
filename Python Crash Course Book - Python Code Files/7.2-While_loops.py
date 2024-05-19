# FOR LOOP
# 1. Use a for loop when you know the number of times you want to iterate or when you want to iterate over elements in a collection (e.g., list, tuple, string, etc.).
# 2. The for loop automatically takes care of handling the iteration and doesn't require you to manage a loop variable explicitly.
# 3. It is ideal when you want to perform a specific action for each item in a sequence.

fruits = ["apple", "banana", "orange"] 
for fruit in fruits:
    print (fruit)

# WHILE LOOP
# Use a while loop when you don't know in advance how many times you want to iterate, and the loop's continuation depends on a condition.
# The while loop requires you to manage a loop variable explicitly, and you need to take care of incrementing or decrementing it (if applicable) inside the loop.
# It is ideal when you want to repeat a specific action until a certain condition becomes false.

count = 0

while count < 3:
    print("Hello!")
    count += 1

## Parrot program- loop will run until you say stop

# message = ""
# while message != 'stop':
#   message input("hello parrot: ")
#       if message == 'stop': 
#           print("Ok boss, i'll stop!")
#       else: 
#           print("Parrot says: ", message)

# using 'flags' to determine the running condition of the loop (find more about iportance of flag in while loop). there could be multiple conditions which will cause the loop to stop. we can set these conditions to flag, so that main code will gets simplified

flagActive = True

message = ""

print("stop: parrot will stop talking, sleep: Parrot will sleep, fly: parrot will fly")

while flagActive:
    message = input ("owner says to parrot: ")
    if message == 'stop':
        print("Ok boss, i'll stop repeating!")
        flagActive = False      # multiple condition to end the loop
        
    elif message == 'sleep':
        print("Parrot has slept...zzzz...")
        flagActive = False      # multiple condition to end the loop
        
    elif message == 'fly':
        print("Parrot has flew away... brrr...")
    else:
        print("Parrot says to owner: ", message)