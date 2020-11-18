# Class Method
# class C(object):
#     @classmethod
#     def fun(cls, arg1, arg2, ...):
#        ....
# fun: function that needs to be converted into a class method
# # returns: a class method for function.
# - A class method is a method which is bound to the class and not the object of the class.
# - They have the access to the state of the class as it takes a class parameter that points to the class and not
#   the object instance.
# - It can modify a class state that would apply across all the instances of the class. For example it can modify a
#   class variable that will be applicable to all the instances.


# Static Method
# class C(object):
#     @staticmethod
#     def fun(arg1, arg2, ...):
#         ...
# returns: a static method for function fun.
# - A static method is also a method which is bound to the class and not the object of the class.
# - A static method can’t access or modify class state.
# - It is present in a class because it makes sense for the method to be present in class.

# - A class method takes cls as first parameter while a static method needs no specific parameters.
# - A class method can access or modify class state while a static method can’t access or modify it.
# - In general, static methods know nothing about class state. They are utility type methods that take some parameters
#   and work upon those parameters. On the other hand class methods must have class as parameter.
# - We use @classmethod decorator in python to create a class method and we use @staticmethod decorator to
#   create a static method in python

# - We generally use class method to create factory methods. Factory methods return class object
#   ( similar to a constructor ) for different use cases.
# - We generally use static methods to create utility functions.

# Python program to demonstrate
# use of class method and static method.
from datetime import date


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

        # a class method to create a Person object by birth year.

    @classmethod
    def fromBirthYear(cls, name, year):
        return cls(name, date.today().year - year)

        # a static method to check if a Person is adult or not.

    @staticmethod
    def isAdult(age):
        return age > 18


person1 = Person('mayank', 21)
person2 = Person.fromBirthYear('mayank', 1996)

print(person1.age)
print(person2.age)

# print the result
print(Person.isAdult(22))


"""
Метод привязан к самому класу (между обычным методом и staticmethod)
сам класс как объект метод cls
Нужно для создание перегрузок конструктора и фабричных методов
"""


class Rectangle:

    def __init__(self, side_a, side_b):
        self.a = side_a
        self.b = side_b

    def __repr__(self): # method representation (create string for debugger or console) correct sting as object
        return "Rectangle(%.1f, %.1f)"% (self.a, self.b)


class Circle:

    def __init__(self, radius):
        self.r = radius

    def __repr__(self):
        return "Circle(%.1f)" % self.r

    @classmethod
    def from_rectangle(cls, rectangle):
        radius = (rectangle.a ** 2 + rectangle.b ** 2) ** 0.5/2
        return cls(radius)


if __name__ == "__main__":
    rectangle = Rectangle(4, 6)
    print(rectangle)

    first_circle = Circle(1)
    print(first_circle)

    second_circle = Circle.from_rectangle(rectangle)
    print(second_circle)


"""
static method works on created object atributes
"""


class MyClass:
    class_attribute = 8

    def __init__(self):
        self.data_attribute = 42

    def instance_method(self):
        print(self.data_attribute)

    @staticmethod
    def static_method():
        print(MyClass.class_attribute)


if __name__ == "__main__":
    MyClass.static_method()  #на классе
    obj = MyClass()
    obj.instance_method() #на экземпляре класса
    obj.static_method()
