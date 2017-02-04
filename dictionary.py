## Working with dictionary and set()


dict0 = {}

dict0['name'] = "Joseph"
dict0['Age'] = 22
dict0['School'] = "NA"

#print (dict0)
#print (dict0['name'])

for k , v in dict0.items():
    print (k)

#updating the value
dict0['Age'] = 23
#adding a new value with a key name 'age' #note: Age and age are two different key values and they are not the same.
dict0['age'] = 22

print(dict0['Age'], dict0['age'])
