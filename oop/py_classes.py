# Class Definition Syntax:
class ClassName:
    # Statement-1
    # Statement-N
    pass

# objects of class
# State : It is represented by attributes of an object. It also reflects the properties of an object.
# Behavior : It is represented by methods of an object. It also reflects the response of an object with other objects.
# Identity : It gives a unique name to an object and enables one object to interact with other objects.


# Declaring an object
class Dog:
    # attributes
    attr1 = "mamal"
    attr2 = "dog"

    # method
    def fun(self):
        print("I'm a", self.attr1)
        print("I'm a", self.attr2)


Rodger = Dog()
print(Rodger.attr1)
Rodger.fun()

# self
# When we call a method of this object as myobject.method(arg1, arg2), this is automatically converted by
# Python into MyClass.method(myobject, arg1, arg2) – this is all the special self is about.

# ------------------------------------------ Constructor -----------------------------------------------------------
# __init__ method - constructors

# class Person:
#     # init method - constructor
#     def __init__(self, name):
#         self.name = name
#     # Sample Method

# Types of constructors :

#  default constructor :The default constructor is simple constructor which doesn’t accept any arguments.It’s definition
#     has only one argument which is a reference to the instance being constructed.
#  parameterized constructor :constructor with parameters is known as parameterized constructor.The parameterized
#     constructor take its first argument as a reference to the instance being constructed known as self and the rest of
#     the arguments are provided by the programmer.

# default constructor :
# def __init__(self):
#     self.{name} = {value}

# parameterized constructor
# def __init__(self, par1, par2):
#     self.{name} = par1
#     self.{name 2} = par2

# ------------------------------------------ Constructor -----------------------------------------------------------
# __del__() method is a known as a destructor method in Python. It is called when all references to the object
# have been deleted i.e when an object is garbage collected.

# base syntax:
# def __del__(self):
#    body of destructor


class Employee:
    # Initializing
    def __init__(self):
        print('Employee created.')

    def __del__(self):
        print('Destructor called, Employee deleted.')


obj = Employee()  # Employee created.
del obj  # Destructor called, Employee deleted.

# The destructor was called after the program ended or when all the references to object are deleted i.e
# when the reference count becomes zero, not when object went out of scope


class Employee:

    def __init__(self):
        print('Employee created')

    def __del__(self):
        print("Destructor called")


def Create_obj():
    print('Making Object...')
    obj2 = Employee()
    print('function end...')
    return obj2


print('Calling Create_obj() function...')  # Calling Create_obj() function...
obj2 = Create_obj()  # Making Object...  ->  Employee created -> function end...
print('Program End...')  # Destructor called
