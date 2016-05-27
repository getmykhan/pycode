## The text book exercise doesnt work.
"""
We will look at how Dictionary Works. A Useful tool!
"""

print ".." * 20



# A Small Dictionary

dict1 = {"Name": "Joe",
         "Age": 21,
         "Place": "New York",
         "Developer": "Python"}

print("Okay will clear a loop till your done")

while True:
    a = raw_input("Enter name that you want to see!>> ")
    if a == "nothing":
        break
    else:
        print(dict1[a])
        continue

print(dict1)
add = raw_input("Do you want  to add something to the dictionary?>> ")
if add == "yes":
    whattoadd = raw_input("What do you want to add?> ")
    whattoaddval = raw_input("And what is the value that you want to add?>> ")
    dict1[whattoadd] = whattoaddval
    print("Do you want to see the new updated Dictionary?>> ")
    yesorno = raw_input(">> ")
    if yesorno == "yes":
        print dict1
    else:
        exit(1)


def del1():
    to_delete = raw_input("Enter what you want to delete from the Dictionary?>> ")
    del dict1[to_delete]


doyouwanttodelete = raw_input("Do you want to delete any item from the list? >> ")
if doyouwanttodelete == "yes":
    del1()
else:
    print("exiting", "..." * 20)

print ".." * 20
