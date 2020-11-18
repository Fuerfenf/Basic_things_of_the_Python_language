# Python supports a List like a container called UserList present in the collections module.
# This class acts as a wrapper class around the List objects. This class is useful when one wants to create a list
# of their own with some modified functionality or with some new functionality.
# It can be considered as a way of adding new behaviors for the list.
# This class takes a list instance as an argument and simulates a list that is kept in a regular list.
# The list is accessible by the data attribute of the this class.

from collections import UserList

L = [1, 2, 3, 4]

# Creating a userlist
userL = UserList(L)
print(userL.data)

# Creating empty userlist
userL = UserList()
print(userL.data)


# Creating a List where
# deletion is not allowed
class MyList(UserList):

    # Function to stop deleltion
    # from List
    def remove(self, s=None):
        raise RuntimeError("Deletion not allowed")

        # Function to stop pop from  

    # List
    def pop(self, s=None):
        raise RuntimeError("Deletion not allowed")

    # Driver's code


L = MyList([1, 2, 3, 4])

print("Original List")

# Inserting to List"
L.append(5)
print("After Insertion")
print(L)

# Deliting From List
L.remove()