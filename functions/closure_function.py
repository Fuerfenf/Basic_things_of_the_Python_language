import logging
# When and why to use Closures:
# - As closures are used as callback functions, they provide some sort of data hiding.
#   This helps us to reduce the use of global variables.
# - When we have few functions in our code, closures prove to be efficient way.
#   But if we need to have many functions, then go for class (OOP).
# https://www.geeksforgeeks.org/python-closures/

# Nested functions in Python
def outerFunction(text):
    text = text

    def innerFunction():
        print(text)

    innerFunction()


outerFunction('Hey!')


# Python Closures
def outerFunction(text):
    text = text

    def innerFunction():
        print(text)

    return innerFunction  # Note we are returning function WITHOUT parenthesis


myFunction = outerFunction('Hey!')
myFunction()


logging.basicConfig(filename='example.log', level=logging.INFO)


def logger(func):
    def log_func(*args):
        logging.info(
            'Running "{}" with arguments {}'.format(func.__name__, args))
        print(func(*args))
        # Necessary for closure to work (returning WITHOUT parenthesis)

    return log_func


def add(x, y):
    return x + y


def sub(x, y):
    return x - y


add_logger = logger(add)
sub_logger = logger(sub)
add_logger(3, 3)
add_logger(4, 5)
sub_logger(10, 5)
sub_logger(20, 10)


