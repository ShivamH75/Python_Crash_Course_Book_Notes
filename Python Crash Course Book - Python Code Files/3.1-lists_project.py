# Problem statement: Create list of guests for wedding invitation
# Criteria 1. user should be able to add members
# criteria 2. user should be able to view list of added members - as per sequence of added and alphabetically sorted
# criteria 3. user should be able to delete any member 
# criteria 3. user should be able to replace member with other (keeping the sequence same)
# criteria 4. Display total count of guests

familyMembers = []

member = input ("Enter name of family member: ")

print(familyMembers)

def addNewMember():
    newMember = input ("Enter name of member: ")
    familyMembers.append(newMember)

def showList ():
    for i in familyMembers:
        print(i)

def guestCount():
    print(len(familyMembers))