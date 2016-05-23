print("Lets create a TODO list!")

print("Hey! Welcome, you can create your own TODO list")

todolist1 = []
while True:
    todo = raw_input("What would you like to add to the list?>> ")
    print("Okay Great, Added!")
    todolist1.append(todo)
    stop = raw_input("Anything else?> ")
    if stop == "no":
        break
    else:
        continue

printing = raw_input("Do you want to see your TODO?> ")
if printing == "yes":
    print todolist1
else:
    exit()


