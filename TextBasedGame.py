##Version : 1.0.0
"""
Text Bassed Guessing Game.
"""

print("Hello and welcome to the world of hulosraft!") ## I Know a very wierd name.
print("You are about to witness a Text Based Game!!")
print("Brace Yourself.")
ready_ = raw_input("Are you ready?> ")




def door_1():
    print("A hard one..")
    print("Crack this puzzle to go to the next round!")
    a = raw_input("My first is often at the front door.\nMy second is found in the cereal family.\nMy third is what most people want.\nMy whole is one of the united states.\nWhat am I?")
    if a == "Matrimony":
        print("Absolutely Right!, Give yourself a pat.")
    else:
        print("Wrong!")
        print("Kicked Out")


def door_2():
    print("Crack this puzzle to go to the next round!")
    b = raw_input("What has four fingers and a thumb, but is not living?")
    if b == "Glove":
        print("Well Done!")
    else:
        print("Wrong!")
        print("Kicked Out")


def door_3():
    print("Crack this puzzle to go to the next round!")
    c = raw_input("I can only live where there is light, but I die if the light shines on me. What am I?")
    if c == "Shadow":
        print("Well Done!")
    else:
        print("Wrong!")
        print("Kicked Out")


def start():
    print("You are standing in front of the castle of walalala..")
    print("The are 3 doors, Door1, Door2, Door3")
    door = raw_input("Which one do you choose?")
    if door == "1" or door == "Door1" or door == "door1":
        door_1()
    elif door == "2" or door == "Door2" or door == "door2":
        door_2()
    elif door == "3" or door == "Door3" or door == "door3":
        door_3()
    else:
        print("Do you know how to play a text based game???")
        exit(1)




if ready_ == 'yes' or ready_ == 'y' or ready_ == "Yes" or ready_ == "Y":
    print("Alright Amigo, Lets go")
    start()
elif ready_ == "no" or ready_ == 'n' or ready_ == "No" or ready_ == "N":
    print("Thats Sad!")
    exit(1)
else:
    print("Sorry we dint understand that command")











