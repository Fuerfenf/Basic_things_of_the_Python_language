#  polymorphism means same function name (but different signatures) being uses for different types.
# https://www.geeksforgeeks.org/polymorphism-in-python/?ref=lbp
# Python program to demonstrate in-built poly-morphic functions
# len() being used for a string
print(len("geeks"))  # 5
# len() being used for a list
print(len([10, 20, 30]))  # 3


# A simple Python function to demonstrate Polymorphism
def add(x, y, z=0):
    return x + y + z
# Driver code


print(add(2, 3))  # 5
print(add(2, 3, 4))  # 9


# Polymorphism with class methods:
class India:

    def capital(self):
        print("New Delhi is the capital of India.")

    def language(self):
        print("Hindi is the most widely spoken language of India.")

    def type(self):
        print("India is a developing country.")


class USA:

    def capital(self):
        print("Washington, D.C. is the capital of USA.")

    def language(self):
        print("English is the primary language of USA.")

    def type(self):
        print("USA is a developed country.")


obj_ind = India()
obj_usa = USA()
for country in (obj_ind, obj_usa):
    country.capital()
    country.language()
    country.type()

