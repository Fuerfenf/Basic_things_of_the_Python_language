# Properties of first class functions:

# A function is an instance of the Object type.
# store the function in a variable.
# pass the function as a parameter to another function.
# return the function from a function.
# store them in data structures such as hash tables, lists, ...


# Functions are objects
def shout(text):
    return text.upper()


print(shout('Hello'))
yell = shout
print(yell('Hello'))


# Functions passed as arguments to other functions
def shout(text):
    return text.upper()


def whisper(text):
    return text.lower()


def greet(func):
    greeting = func("Hi, I am created by a function passed as an argument.")
    print(greeting)


greet(shout)
greet(whisper)


# Functions return another function
def create_adder(x):
    def adder(y):
        return x + y

    return adder


add_15 = create_adder(15)
print(add_15(10))
