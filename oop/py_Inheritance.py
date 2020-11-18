# A Python program to demonstrate inheritance
# Base or Super class. Note object in bracket.
# (Generally, object is made ancestor of all classes)
# In Python 3.x "class Person" is
# equivalent to "class Person(object)"
# https://www.geeksforgeeks.org/types-of-inheritance-python/?ref=lbp

# -> Single inheritance:
class Person:

    # Constructor
    def __init__(self, name):
        self.name = name

        # To get name

    def getName(self):
        return self.name

        # To check if this person is an employee

    def isEmployee(self):
        return False


# Inherited or Subclass (Note Person in bracket)
class Employee(Person):

    # Here we return true
    def isEmployee(self):
        return True


# Driver code
emp = Person("Geek1")  # An Object of Person
print(emp.getName(), emp.isEmployee())
emp = Employee("Geek2")  # An Object of Employee
print(emp.getName(), emp.isEmployee())


# Subclassing (Calling constructor of parent class)
# A child class needs to identify which class is its parent class. This can be done by mentioning
# the parent class name in the definition of the child class.
# Eg: class subclass_name (superclass_name):


class Person2:

    def __init__(self, name, idnumber):
        self.name = name
        self.idnumber = idnumber

    def display(self):
        print(self.name)
        print(self.idnumber)


class Employee2(Person2):

    def __init__(self, name, idnumber, salary=None, post=None):
        super().__init__(name, idnumber)
        self.salary = salary
        self.post = post


a = Employee2('Rahul', 886012)
a.display()


# -> Multiple inheritanc:
class Base1(object):
    def __init__(self):
        self.str1 = "Geek1"
        print("Base1")


class Base2(object):
    def __init__(self):
        self.str2 = "Geek2"
        print("Base2")


class Derived(Base1, Base2):
    def __init__(self):
        # Calling constructors of Base1
        # and Base2 classes
        Base1.__init__(self)
        Base2.__init__(self)
        print("Derived")

    def printStrs(self):
        print(self.str1, self.str2)


ob = Derived()
ob.printStrs()


# -> Multilevel inheritance: When we have a child and grandchild relationship:
# A Python program to demonstrate inheritance
# Base or Super class. Note object in bracket.
# (Generally, object is made ancestor of all classes)
# In Python 3.x "class Person" is
# equivalent to "class Person(object)"
class Base(object):

    # Constructor
    def __init__(self, name):
        self.name = name

        # To get name

    def getName(self):
        return self.name

    # Inherited or Sub class (Note Person in bracket)


class Child(Base):

    # Constructor
    def __init__(self, name, age):
        Base.__init__(self, name)
        self.age = age

        # To get name

    def getAge(self):
        return self.age

    # Inherited or Sub class (Note Person in bracket)


class GrandChild(Child):

    # Constructor
    def __init__(self, name, age, address):
        Child.__init__(self, name, age)
        self.address = address

        # To get address

    def getAddress(self):
        return self.address

    # Driver code


g = GrandChild("Geek1", 23, "Noida")
print(g.getName(), g.getAge(), g.getAddress())


# Hierarchical Inheritance: When more than one derived classes are created from a single base this type of inheritence
#   is called hierarchical inheritance. In this program, we have a parent (base) class and two child (derived) classes.
# Base class
class Parent:
    def func1(self):
        print("This function is in parent class.")

    # Derived class1


class Child1(Parent):
    def func2(self):
        print("This function is in child 1.")

    # Derivied class2


class Child2(Parent):
    def func3(self):
        print("This function is in child 2.")

    # Driver's code


object1 = Child1()
object2 = Child2()
object1.func1()
object1.func2()
object2.func1()
object2.func3()


# -> Hybrid Inheritance: Inheritence consisting of multiple types of inheritence is called hybrid inheritence.
class School:
    def func1(self):
        print("This function is in school.")


class Student1(School):
    def func2(self):
        print("This function is in student 1. ")


class Student2(School):
    def func3(self):
        print("This function is in student 2.")


class Student3(Student1, School):
    def func4(self):
        print("This function is in student 3.")


object = Student3()
object.func1()
object.func2()

