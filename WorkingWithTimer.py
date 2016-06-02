from time import sleep


a = raw_input("Enter Number1>> ")
b = raw_input("Enter Number2?>> ")



print("You will now sleep for 5 seconds..")
sleep(5)


if int(a) > int(b):
    sleep(2)
    print("You have waited for 2 seconds")
    print("Your result will be printed below after 2 seconds")
    sleep(2)
    print("A is greater")
else:
    sleep(2)
    print("You have slept for 2 seconds")
    print("B is greater")
    sleep(10)
    print("Now you will enter a loop, which will run for 10 seconds and exit")


for i in range(0, 10):
    print(10 - i)
    sleep(1)
print("Great Job")
