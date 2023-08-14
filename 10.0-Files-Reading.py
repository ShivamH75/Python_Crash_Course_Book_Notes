#  imported 'Path' class from "pathlib" module. pathlib is a inbuilt module.
from pathlib import Path

# created an instance 'readFile' from Path class. VS Code shows suggestion for attribute to pass in the class
readFile = Path('text files/pidigits.txt')

# created variable named 'contents' and assigned 'read_text()' method to it
contents = readFile.read_text()

# variable now contains info which has been read from the file
print(contents)


# we can also check prior to reading the file, if that file really exists or not
if readFile.exists() == True:
    print(readFile.read_text())
else:
    print("File does not exist in the path")


##  Relative and Absolute File Paths
# Relative path - Relative to the current working directory

readOne = Path('text files/pidigits.txt')
'''file is read with ref. of location of current working file'''
print(readOne.read_text())

# Absolute File Paths - path wrt location in the computer storage
# if required files does not exist in working directory of current file, we can use absolute path system 

path_of_file = 'E:\\010101 SHIVAM\\01_PROGRAMMING\\Python Programming\\Python_crash_couse-Book\\text files\\dolphin.txt'

readTwo = Path(path_of_file)
'''file is read wrt its location in storage'''
print(readTwo.read_text())



# ____________________________________________________________________________
from pathlib import Path

pathVar = Path('E:\\010101 SHIVAM\\01_PROGRAMMING\\Python Programming\\Python_crash_couse-Book\\text files\\piDigits.txt')

contentsRead = pathVar.read_text()

for line in contentsRead.split():       #split()
    print(line)

for line in contentsRead.splitlines():      #splitlines()
    print(line)


# replace 'dolphin' with 'shark' in the text file

path1 = Path('E:\\010101 SHIVAM\\01_PROGRAMMING\\Python Programming\\Python_crash_couse-Book\\text files\\dolphin.txt')

contents = path1.read_text()

contents_modified = contents.replace('dolphin', 'sharks')   
#replace('oldWord', 'newWord')

print(contents_modified)

'''-------------------------------------------------------------------------'''
# The encoding argument is needed when your system’s default encoding doesn’t match the encoding of the file that’s being read. 
# This is most likely to happen when reading from a file that wasn’t created on your system.
path2 = Path('E:\\010101 SHIVAM\\01_PROGRAMMING\\Python Programming\\Python_crash_couse-Book\\text files\\dolphin.txt')

contents2 = path2.read_text(encoding='utf-8')

print(contents2)