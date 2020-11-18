# Private Variables
#  Any identifier of the form __geek (at least two leading underscores or at most one trailing underscore) is
#  replaced with _classname__geek, where classname is the current class name with leading underscore(s) stripped.
#  As long as it occurs within the definition of the class, this mangling is done. This is helpful for letting
#  subclasses override methods without breaking intraclass method calls.


# Python code to illustrate how mangling works
class Map:
    def __init__(self, iterate):
        self.list = []
        self.__geek(iterate)

    def geek(self, iterate):
        for item in iterate:
            self.list.append(item)

            # private copy of original geek() method
    __geek = geek


# class MapSubclass(Map):
#
#     # provides new signature for geek() but
#     # does not break __init__()
#     def geek(self, key, value):
#         for i in zip(keys, values):
#             self.list.append(i)


# _Single Leading Underscores
# Python code to illustrate
# how single underscore works
def _get_errors(self):
    if self._errors is None:
        self.full_clean()
    return self._errors


errors = property(_get_errors)


# __Double Leading Underscores
# Python code to illustrate how double
# underscore at the beginning works
class Geek:
    def _single_method(self):
        pass

    def __double_method(self): # for mangling
        pass


class Pyth(Geek):
    def __double_method(self): # for mangling
        pass


# __Double leading and Double trailing underscores__
#  follow this while using special variables or methods (called “magic method”) such as__len__, __init__.
#  These methods provide special syntactic features to the names. For example, __file__ indicates the location of Python
#  file, __eq__ is executed when a == b expression is executed.
# Python code to illustrate double leading and
# double trailing underscore works
class Geek:
    # '__init__' for initializing, this is a
    # special method
    def __init__(self, ab):
        self.ab = ab

        # custom special method. try not to use it
    def __custom__(self):
        pass