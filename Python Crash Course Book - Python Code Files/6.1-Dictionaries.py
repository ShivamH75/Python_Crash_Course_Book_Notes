# Dictionaries help to  connect related information
# Formt of dictioary is Key-Value pairs in Curly Brackets

sampleDict = {
    'name': "Shivam",
    'hobby': "Coding",
    "Age" : 23
}

for item in sampleDict:
    print (sampleDict[item])

#  To Add new key-values in existing dictionary
#  format :: dictName['newKey'] = 'newValue'

sampleDict['company'] = 'Mars ASSOCIATION'
sampleDict['Car'] = 'Audi R8'

print (sampleDict)

#  To modify value of any kwy within a dictionary
sampleDict['Car'] = 'Mercedes Benz G-Wagon'
print (sampleDict)

#  To Delete Entire key-value pair - use 'del' keyword and keyname within []

del sampleDict['company']
print(sampleDict)

# Store one type of info of many ojects
favLanguages = {
    'john' : 'ruby',
    'steven' : 'pearl',
    'shivam' : 'pythOn'
} 

print(f"Shivam's fav language is {favLanguages['shivam'].title()}")

#  if the we mention some key which is not in dictionary, we get 'KeyError'
# print(f"Shivam's fav language is {favLanguages['rahul'].title()}")    

#  To handle situation when key is not preset in dictionary, use the 'get()' method
print(f"Shivam's fav language is {favLanguages.get('rahul')}")   #by default it returns 'None'
print(f"Shivam's fav language is {favLanguages.get('rahul', 'Key not found')}")         #we can also assign the message if the key is not found


 