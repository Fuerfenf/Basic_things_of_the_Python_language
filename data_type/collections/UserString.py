# Python supports a String like a container called UserString present in the collections module.
# This class acts as a wrapper class around the string objects. This class is useful when one wants to create
# a string of their own with some modified functionality or with some new functionality.
# It can be considered as a way of adding new behaviors for the string. This class takes any argument that can be
# converted to string and simulates a string whose content is kept in a regular string.
# The string is accessible by the data attribute of this class.


from collections import UserString

d = 12344

# Creating an UserDict
userS = UserString(d)
print(userS.data)

# Creating an empty UserDict
userS = UserString("")
print(userS.data)


# Creating a Mutable String
class Mystring(UserString):

    # Function to append to
    # string
    def append(self, s):
        self.data += s

        # Function to rmeove from

    # string
    def remove(self, s):
        self.data = self.data.replace(s, "")

    # Driver's code


s1 = Mystring("Geeks")
print("Original String:", s1.data)

# Appending to string
s1.append("s")
print("String After Appending:", s1.data)

# Removing from string
s1.remove("e")
print("String after Removing:", s1.data)
