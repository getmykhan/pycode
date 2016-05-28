## Working with files.

from os.path import exists

print("File Manipulation")
print ".." * 5

filetoopen = raw_input("Enter the name of the file that you want to write into") ## The file must be in the directory

if exists(filetoopen):
    print("The File is Avaliable..")
    print("Opening......")
else:
    print("The file does not exist in the directory\nA new file with that name will be created ")

filetowriteto = open(filetoopen, 'a+')

to_truncate = raw_input("Do you want to start a fresh file yes or no?> ")
if to_truncate == "yes" or to_truncate == "y":
    filetowriteto.truncate()
else:
    print("Okay!")

while True:
    whattowrite = raw_input("What do you want to enter into the file?>> ")
    filetowriteto.write(whattowrite)
    addmore = raw_input("Do you want to add more? Y or N>> ")
    if addmore == "N":
        break
    else:
        continue


