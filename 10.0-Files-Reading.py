#  imported 'Path' class from "pathlib" module. pathlib is a inbuilt module.
from pathlib import Path

# created an instance 'readFile' from Path class. VS Code shows suggestion for attribute to pass in the class
readFile = Path('textFile.txt')

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

readOne = Path('datafiles\\blank_doc01.txt')
'''file is read with ref. of location of current working file'''
print(readOne.read_text())

# Absolute File Paths - path wrt location in the computer storage
# if required files does not exist in working directory of current file, we can use absolute path system 

path_of_file = 'C:\\Users\\Shivam.Hundekari\\Documents\\02 Practice Coding\\Python\Python_crash_course-Book\\ch-10-Files\\datafiles\\blank_doc02.txt'

readTwo = Path(path_of_file)
'''file is read wrt its location in storage'''
print(readTwo.read_text())