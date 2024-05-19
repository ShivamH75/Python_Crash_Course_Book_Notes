# small project to print sum of numbers between 1 to 10


# step1: create empty list
exampleList = []

# step2: add numbers between 1 and 100 in the list
for number in range(1, 11):
    exampleList.append(number)

# step3: use sum() function to get sum of numbers in the list
sumOfList = sum(exampleList)
print(sumOfList)