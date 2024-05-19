from name_function import get_formatted_name

while True:
    first = input("Enter first name: ")
    if first == 'q':
        break
    last = input("Enter last name: ")
    if last == 'q':
        break

    formatted_name = get_formatted_name(first,last)
    print(f"Your name: {formatted_name}")