# Define your dictionary with keys and values
my_dict = {
    "key1": "value1",
    "key2": "value2",
    "key3": "value3",
    "key4": "value4"
}

# Function to display keys when the security code is entered
def display_keys():
    print("List of Keys:")
    for key in my_dict.keys():
        print(key)

# Function to display the value for a given key
def display_value(key):
    if key in my_dict:
        print(f"The value for {key} is: {my_dict[key]}")
    else:
        print(f"Key '{key}' not found in the dictionary.")

# Main program loop
while True:
    # Prompt for the security code
    security_code = input("Enter the security code (1234 to display keys, or 'exit' to quit): ")

    if security_code == "1234":
        display_keys()
    elif security_code == "exit":
        print("Exiting the program. Goodbye!")
        break
    else:
        # If not the security code, assume it's a key and display the value
        display_value(security_code)
