# Metaclass is responsible for generation of classes
# To create our custom metaclass, our custom metaclass have to inherit type metaclass and usually override –
# https://www.geeksforgeeks.org/metaprogramming-metaclasses-python/?ref=lbp
# - __new__(): It’s a method which is called before __init__(). It creates the object and return it.
#              We can overide this method to control how the objects are created.
# - __init__(): This method just initialize the created object passed as parameter


# --------------------------------using type()----------------------------------------------------------
# - When called with only one argument, it returns the type. We have seen it before in above examples.
# - When called with three parameters, it creates a class. Following arguments are passed to it –
#   - Class name
#   - Tuple having base classes inherited by class
#   - Class Dictionary: It serves as local namespace for the class, populated with class methods and variables
def test_method(self):
    print("This is Test class method!")


# creating a base class
class Base:
    def myfun(self):
        print("This is inherited method!")

    # Creating Test class dynamically using


# type() method directly
Test = type('Test', (Base,), dict(x="atul", my_method=test_method))

# Print type of Test
print("Type of Test class: ", type(Test))

# Creating instance of Test class
test_obj = Test()
print("Type of test_obj: ", type(test_obj))

# calling inherited method
test_obj.myfun()

# calling Test class method
test_obj.my_method()

# printing variable
print(test_obj.x)


# --------------------------------without using type()--------------------------------

from functools import wraps


def debug(func):
    '''decorator for debugging passed function'''

    @wraps(func)
    def wrapper(*args, **kwargs):
        print("Full name of this method:", func.__qualname__)
        return func(*args, **kwargs)

    return wrapper


def debugmethods(cls):
    '''class decorator make use of debug decorator
       to debug class methods '''

    for key, val in vars(cls).items():
        if callable(val):
            setattr(cls, key, debug(val))
    return cls


class debugMeta(type):
    '''meta class which feed created class object
       to debugmethod to get debug functionality
       enabled objects'''

    def __new__(cls, clsname, bases, clsdict):
        obj = super().__new__(cls, clsname, bases, clsdict)
        obj = debugmethods(obj)
        return obj

    # base class with metaclass 'debugMeta'


# now all the subclass of this
# will have debugging applied
class Base(metaclass=debugMeta): pass


# inheriting Base
class Calc(Base):
    def add(self, x, y):
        return x + y

    # inheriting Calc


class Calc_adv(Calc):
    def mul(self, x, y):
        return x * y

    # Now Calc_adv object showing


# debugging behaviour
mycal = Calc_adv()
print(mycal.mul(2, 3))