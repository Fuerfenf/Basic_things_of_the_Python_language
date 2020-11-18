# Python supports a dictionary like a container called UserDict present in the collections module.
# This class acts as a wrapper class around the dictionary objects.
# This class is useful when one wants to create a dictionary of their own with some modified functionality
# or with some new functionality. It can be considered as a way of adding new behaviors for the dictionary.
# This class takes a dictionary instance as an argument and simulates a dictionary that is kept in a regular dictionary.
# The dictionary is accessible by the data attribute of this class.

from collections import UserDict

d = {'a': 1,
     'b': 2,
     'c': 3}

# Creating an UserDict
userD = UserDict(d)
print(userD.data)

# Creating an empty UserDict
userD = UserDict()
print(userD.data)


# Creating a Dictionary where
# deletion is not allowed
class MyDict(UserDict):

    # Function to stop deleltion
    # from dictionary
    def __del__(self):
        raise RuntimeError("Deletion not allowed")

        # Function to stop pop from

    # dictionary
    def pop(self, s=None):
        raise RuntimeError("Deletion not allowed")

        # Function to stop popitem

    # from Dictionary
    def popitem(self, s=None):
        raise RuntimeError("Deletion not allowed")

    # Driver's code


d = MyDict({'a': 1,
            'b': 2,
            'c': 3})

print("Original Dictionary")
print(d)
