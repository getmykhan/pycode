"""
Simple Calculator
"""

class MyCalculator(object):
    def __init__(self):
        print("This is a simple calulator to perform Arithmetic Operations")
        print("**") * 20

    def addition(self):
        c = int(a) + int(b)
        print(c)
    def subtraction(self):
        d = int(a) - int(b)
        print(d)
    def multiplication(self):
        e = int(a) * int(b)
        print(e)
    def division(self):
        f = int(a) / int(b)
        print(f)




obj1 = MyCalculator()

a = raw_input("Enter Value1: ")
b = raw_input("Enter Value2: ")

print("Select the Operation of your choice")
print """
1.)Addition
2.)Subtraction
3.)Multiplication
4.)Division
"""
option = raw_input(">> ")

if option == "1" or option == "addition":
    obj1.addition()
elif option == "2" or option == "subtraction":
    obj1.subtraction()
elif option == "3" or option == "multiplication":
    obj1.multiplication()
elif option == "4" or option == "division":
    obj1.division()
else:
    print("You have entered a wrong value.")
    print("Exiting....")
    print(exit(1))
