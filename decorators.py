# Function Decorator
def decorate_message(fun):
    # Nested function
    def addWelcome(site_name):
        return "Welcome to " + fun(site_name)

        # Decorator returns a function
    return addWelcome


@decorate_message
def site(site_name):
    return site_name


print(site("GeeksforGeeks"))  # Welcome to GeeksforGeeks


def attach_data(func):
    func.data = 3
    return func


@attach_data
def add(x, y):
    return x + y


# ‘add()’ returns sum of x and y passed as arguments but it is wrapped by a decorator function,
# calling add(2, 3) would simply give sum of two numbers but when we call add.data then ‘add’ function is
# passed into then decorator function ‘attach_data’ as argument and this function returns ‘add’ function with
# an attribute ‘data’ that is set to 3 and hence prints it.
print(add(2, 3))  # 5
print(add.data)  # 3


# the execution time of a function
import time
import math


def calculate_time(func):
    # added arguments inside the inner1,
    # if function takes any arguments,
    # can be added like this.
    def inner1(*args, **kwargs):
        # storing time before function execution
        begin = time.time()
        func(*args, **kwargs)
        # storing time after function execution
        end = time.time()
        print("Total time taken in : ", func.__name__, end - begin)
    return inner1


# this can be added to any function present,
# in this case to calculate a factorial
@calculate_time
def factorial(num):
    # sleep 2 seconds because it takes very less time
    # so that you can see the actual difference
    time.sleep(2)
    print(math.factorial(num))


# calling the function.
factorial(10)


# Syntax for decorators with parameters
# @decorator(params)
# def func_name():
#     ''' Function implementation'''
# same as :
# def func_name():
#     ''' Function implementation'''
#
# func_name = (decorator(params))(func_name)
# """

def decorator_fun(func):
    print("Inside decorator")

    def inner(*args, **kwargs):
        print("Inside inner function")
        print("Decorated the function")
        # do operations with func

        func()

    return inner


# first way
@decorator_fun
def func_to():
    print("Inside actual function")


func_to()


# another way of using decorators
def func_to():
    print("Inside actual function")


decorator_fun(func_to)()


def decorator(*args, **kwargs):
    print("Inside decorator")

    def inner(func):
        # code functionality here
        print("Inside inner function")
        print("I like", kwargs['like'])

        func()

        # reurning inner function

    return inner


@decorator(like="geeksforgeeks")
def my_func():
    print("Inside actual function")


def decorator_func(x, y):
    def Inner(func):
        def wrapper(*args, **kwargs):
            print("I like Geeksforgeeks")
            print("Summation of values - {}".format(x + y))

            func(*args, **kwargs)

        return wrapper

    return Inner


# Not using decorator
def my_fun(*args):
    for ele in args:
        print(ele)

    # another way of using dacorators


decorator_func(12, 15)(my_fun)('Geeks', 'for', 'Geeks')


# Factorial program with memoization using
# decorators.

# A decorator function for function 'f' passed
# as parameter
def memoize_factorial(f):
    memory = {}

    # This inner function has access to memory
    # and 'f'
    def inner(num):
        if num not in memory:
            memory[num] = f(num)
        return memory[num]

    return inner


@memoize_factorial
def facto(num):
    if num == 1:
        return 1
    else:
        return num * facto(num - 1)


print(facto(5))
