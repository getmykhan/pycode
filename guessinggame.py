"""
Guess a number between 1 and 10
"""

import random


print("The Guessing Game.\nGuess a number, any number between 1 and 10.\nEnjoy")

def helpme():
    print("Make a guess between 1 and 10")
    print("Make a wild guess")
    print("If you want to quit, just type exit and click enter.")

randomm = random.randint(1, 11)
while True:
    guess = raw_input("What is the number?> ")
    if guess == "help":
        helpme()
    elif guess == "exit":
        exit(1)
    elif int(guess) == int(randomm):
        print("Absolutely correct")
        break
    elif int(guess) < int(randomm):
        print("Too Small try again")
        continue
    elif int(guess) > int(randomm):
        print("Too Big try again")
    else:
        helpme()
