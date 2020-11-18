# Protected members -> , just follow the convention by prefixing the name of the member by a single underscore “_”
class Base:
    def __init__(self):
        # Protected member
        self._a = 2


# Creating a derived class
class Derived(Base):
    def __init__(self):
        # Calling constructor of
        # Base class
        Base.__init__(self)
        print("Calling protected member of base class: ")
        print(self._a)


obj1 = Derived()
obj2 = Base()
print(obj2.a)

# Private members
#  to define a private member prefix the member name with double underscore “__”
# Python program to
# demonstrate private members


# Creating a Base class
class Base2:
    def __init__(self):
        self.a = "GeeksforGeeks"
        self.__c = "GeeksforGeeks"


# Creating a derived class
class Derived2(Base2):
    def __init__(self):
        # Calling constructor of
        # Base class
        Base.__init__(self)
        print("Calling private member of base class: ")
        print(self.__a)
    # Driver code


obj3 = Base2()
print(obj3.a)

# Uncommenting print(obj1.c) will
# raise an AttributeError 

# Uncommenting obj2 = Derived() will
# also raise an AtrributeError as
# private member of base class
# is called inside derived class
