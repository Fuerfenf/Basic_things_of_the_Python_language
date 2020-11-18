# A simple Python function to check whether x is even or odd
def evenOdd(x):
    if x % 2 == 0:
        print("even")
    else:
        print("odd")


evenOdd(2)
evenOdd(3)


# default arguments
def myFun(x, y=50):
    print("x: ", x)
    print("y: ", y)


myFun(10)


# Keyword arguments:
def student(firstname, lastname):
    print(firstname, lastname)


student(firstname='Geeks', lastname='Practice')
student(lastname='Practice', firstname='Geeks')


# Variable length arguments - *args
def myFun2(*argv):
    for arg in argv:
        print(arg)


myFun2('Hello', 'Welcome', 'to', 'GeeksforGeeks')


# Variable length arguments - *kwargs for variable number of keyword arguments
def myFun3(**kwargs):
    for key, value in kwargs.items():
        print("%s == %s" % (key, value))


myFun3(first='Geeks', mid='for', last='Geeks')

# Anonymous functions  Python code to illustrate cube of a number using labmda function
cube = lambda x: x * x * x
print(cube(7))
# filter() with lambda()
li = [5, 7, 22, 97, 54, 62, 77, 23, 73, 61]
final_list = list(filter(lambda x: (x % 2 != 0), li))
print(final_list)
# map() with lambda()
# to get double of a list.
li = [5, 7, 22, 97, 54, 62, 77, 23, 73, 61]
final_list = list(map(lambda x: x*2, li))
print(final_list)