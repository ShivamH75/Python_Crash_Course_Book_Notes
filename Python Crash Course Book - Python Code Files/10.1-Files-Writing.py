# Writing to a File

# same 2 lines as read text

from pathlib import Path
path = Path('text files\\writeFile.txt')
'''if there is no existing file in given path, new file will be created'''

sampleString = "Hello Robin"

path.write_text(sampleString)

print(path.read_text())


# Be careful when calling write_text() on a path object. If the file already exists, write_text() will erase the current contents of the file and write new contents to the file
