"""
Opens a file and reads the content
"""


def read(path):
    try:
        a = open(path)
        print(a.read())
    except:
        print("File not found!")


if __name__ == '__main__':
    filetoread = input("Enter the name of the file>> ")
    read(filetoread)

#Note : Make sure the file is in the directory.
