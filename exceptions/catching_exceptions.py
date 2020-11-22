# Base block
# try:
#     ... run code ...
# except (Exception type, ... other exeption types ... or can use smae except block for catch other exception ):
#     ... execute this code when there is an exception ...
# else:
#     ... Run this code if no exception ...
# finally:
#     ... always run this code ...
try:
    a = 10/0
except ZeroDivisionError as exc:
    print("This exception: {}.".format(exc))
# other example:
try:
    with open("file", 'r', encoding="utf-8") as file:
        for line in file:
            print(line.strip())
except IOError as exc:
    print(exc)
except ValueError as exc:
    print(exc)
else:
    print("read all lines")
finally:
    print("finally block")


# context manager (other way to catch exception)
class InOutBlock:

    def __enter__(self):
        print("Inside in code block")

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("Out from code block {a} {b} {c}".format(a=exc_tb, b=exc_val, c=exc_tb))
        return True # return true for shutdown exception


with InOutBlock() as in_out:
    print("Processed ...")
    a = number / number2
    print("Calculate value ...")
print("after context manager")


# how raise exceptions
# for this used operator: raise
try:
    raise NameError("Exception")
except NameError as exc:
    print(exc)
    raise # in this we can raize other exception: raise TypeError from exc


# How create custom exception:
class CustomException1(Exception):
    pass


try:
    a = 10/0
except CustomException1 as exc:
    print("This exception: {}.".format(exc))
#
