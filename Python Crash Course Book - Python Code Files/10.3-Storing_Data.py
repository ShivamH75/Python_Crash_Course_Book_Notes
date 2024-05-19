# Storing Data
# The json module allows you to convert simple Python data structures into JSON-formatted strings, and then load the data from that file the next time the program runs. 

from pathlib import Path
# steps
# 1. import json module
import json

# 2. create a list of numbers
numbers = [2, 3, 5, 7, 11, 13]

# 3. mention in Path the file which we will be using to store json data
path = Path('text files/file_to_write_into.json')

# 4. used method 'json.dumps()' to store the list data in a new variable
contents = json.dumps(numbers)

# 5. used 'write_text' method to write the 'contents' into json file
path.write_text(contents)


# json.loads() to read the list back into memory:
# step 1: assign path of file in 'path' variable
path = Path('text files/file_to_read_from.json')

# step 2: read_text() method to read the file on mentioned path
contents = path.read_text()

# step 3: json.loads() method to load content from readed file
numbers = json.loads(contents)

# step 4: print the variable which was assigned json.load data
print(numbers)


## Saving and Reading User-Generated Data
path = Path('text files/userinfo.json')

if path.exists():
    contents = path.read_text()
    username = json.loads(contents)
    print(f"Welcome back, {username}!")
else:
    username = input("What is your name? ")
    contents = json.dumps(username)
    path.write_text(contents)
    print(f"We'll remember you when you come back, {username}!")

