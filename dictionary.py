## Working with dictionary and set()


dict0 = {}

dict0['name'] = "Joseph"
dict0['Age'] = 22
dict0['School'] = "NA"

#print (dict0)
#print (dict0['name'])

for k , v in dict0.items():
    print (k, ":", v)

#updating the value
dict0['Age'] = 23
#adding a new value with a key name 'age' #note: Age and age are two different key values and they are not the same.
dict0['age'] = 22

print(dict0['Age'], dict0['age'])

# Note dictionary values have no limitations/restrictions.

# The key value should be unique, if the same key repeats in the dictionary then, the last key that is assigned wins.
dict0['name'] = "Michael"
print(dict0['name'])

#Dictionary Functions and built-in methods.

#To find the lenght of all the elements in the Dictionary
lengthOf = len(dict0)
print(lengthOf)

#Returns a string type
stringOf = str(dict0)
print(stringOf)

#Result will be the type, i.e : For the below two lines the output will be : class : dict
typeOf = type(dict0)
print(typeOf)


#clear(); it will clear all the elements in the dictionary

def clearit(argv1):
    dict0.clear()
    if len(dict0) == 0:
        print("The lenght is %d, which means that that the dictionary has been cleared and that there are no items inside " % len(dict0))
    else:
        print("The dictionary has elements")
clearit(dict0)
