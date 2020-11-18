# Example for usage of *arg:
def myFun1(*argv):
    for arg in argv:
        print(arg)


myFun1('Hello', 'Welcome', 'to', 'GeeksforGeeks')


def myFun2(arg1, *argv):
    print("First argument :", arg1)
    for arg in argv:
        print("Next argument through *argv :", arg)


myFun2('Hello', 'Welcome', 'to', 'GeeksforGeeks')


# Example for usage of **kwargs:
def myFun4(**kwargs):
    for key, value in kwargs.items():
        print("%s == %s" % (key, value))


myFun4(first='Geeks', mid='for', last='Geeks')


def myFun5(arg1, **kwargs):
    for key, value in kwargs.items():
        print("%s == %s" % (key, value))


myFun5("Hi", first='Geeks', mid='for', last='Geeks')


# *args and **kwargs to call a function
def myFun6(arg1, arg2, arg3):
    print("arg1:", arg1)
    print("arg2:", arg2)
    print("arg3:", arg3)


# Now we can use *args or **kwargs to
# pass arguments to this function :
args = ("Geeks", "for", "Geeks")
myFun6(*args)

kwargs = {"arg1": "Geeks", "arg2": "for", "arg3": "Geeks"}
myFun6(**kwargs)


# Using *args and **kwargs in same line to call a function
def myFun7(*arguments, **kwarguments):
    print("args: ", arguments)
    print("kwargs: ", kwarguments)


myFun7('geeks', 'for', 'geeks', first="Geeks", mid="for", last="Geeks")
