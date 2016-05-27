"""
To find the greatest of two numbers!
"""

## Read the two numbers.

number1 = raw_input("Enter number 1>> ")
number2 = raw_input("Enter number 2>> ")

if int(number1) > int(number2):
    print "Number1, which is %d is greater than %d" % (int(number1), int(number2))
else:
    print "Number2, which is %d is greater than %d" % (int(number2), int(number1))
