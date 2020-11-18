# key is separated from its value by a colon(:). Values of a dictionary can be of any type, but the keys must be of
# an immutable data type such as strings, numbers, or tuples
# https://www.geeksforgeeks.org/python-dictionary/

# access dictionary elements, you can use the familiar square brackets along with the key to obtain its value.
# Following is a simple example
diction = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}
print("dict['Name']: ", diction['Name'])
print("dict['Age']: ", diction['Age'])

# update a dictionary by adding a new entry or a key-value pair, modifying an existing entry,
# or deleting an existing entry as shown below in the simple example
dict1 = {'Name': 'Zara', 'Age': 8, 'Class': 'First', 'School': "DPS School"}
print("dict['Age']: ", dict1['Age'])
print("dict['School']: ", dict1['School'])

# remove individual dictionary elements or clear the entire contents of a dictionary
del dict1['Name']  # remove entry with key 'Name'
dict1.clear()  # remove all entries in dict
del dict1  # delete entire dictionary

# -> Dictionary Functions
#   len(dict)
# Gives the total length of the dictionary. This would be equal to the number of items in the dictionary.
len(diction)
#   str(dict)
# Produces a printable string representation of a dictionary
print(str(diction))
#   type(variable)
# Returns the type of the passed variable. If passed variable is dictionary, then it would return a dictionary type.
type(diction)

# -> Dictionary Methods
#   dict.clear()  Removes all elements of dictionary dict
#   dict.copy() Returns a shallow copy of dictionary dict
#   dict.fromkeys() Create a new dictionary with keys from seq and values set to value.
diction.fromkeys(('Name', 'Age'), "Null")
#   dict.get(key, default=None) For key key, returns value or default if key not in dictionary
diction.get('Name')
diction.get('Age', 6)
# in check key in diction
print('Age' in diction)
#   dict.items() Returns a list of dict's (key, value) tuple pairs
diction.items()
#   dict.keys Returns list of dictionary dict's keys
diction.keys()
#   dict.setdefault(key, default=None)
# Similar to get(), but will set dict[key]=default if key is not already in dict
diction.setdefault('Points', None)
# 	dict.update(dict2) Adds dictionary dict2's key-values pairs to dict
dict2 = {'Name': 'Zara', 'Age': 7}
dict3 = {'Sex': 'female'}
dict.update(dict2)
#   dict.values() Returns list of dictionary dict's values
diction.values()


# Defaultdict in Python
# https://www.geeksforgeeks.org/defaultdict-in-python/

# Defaultdict is a container like dictionaries present in the module collections.
# Defaultdict is a sub-class of the dict class that returns a dictionary-like object.
# The functionality of both dictionaries and defualtdict are almost same except for the fact that defualtdict
# never raises a KeyError. It provides a default value for the key that does not exists.
from collections import defaultdict


# Function to return a default
# values for keys that is not
# present
def def_value():
    return "Not Present"


# Defining the dict
d = defaultdict(def_value)
d["a"] = 1
d["b"] = 2

print(d["a"])
print(d["b"])
print(d["c"])
