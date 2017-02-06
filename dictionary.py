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

#copy(); To copy 1 dictionary to the other.

dict1 = {"name": "Lola", "Age": 12 }
#The content of dictionary will be copied and assigned to the dict2
dict2 = dict1.copy()

print(dict2)

#fromkeys; used to add vale to multiple keys at the same time. Effective.

sequenceOth = ('Number', 'Value', 'Integer' , 'Digits')
dict2 = dict2.fromkeys(sequenceOth, 10)

print(dict2)

#get(); Very handy function to get the value of a key; if the key is not in the dictionary; it returns none.

print(dict2.get('Number'))
print(dict2.get('Age')) #will return none.

#keys() # This fuction will return the all the keys in the dictionary

print(dict2.keys())
