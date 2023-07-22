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
