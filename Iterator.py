# iterator object contains a countable number of values
# in python iterator object consist of methods __iter__() and __next__()

# some examples:
string_one = 'sadasdsa'
string_iter = iter(string_one)
print(next(string_iter))


# create iterator class, example:
class Mynumber:
    def __init__(self):
        pass

    def __iter__(self):
        # set step to zero position
        self.iteration = 0
        return self

    def __next__(self):
        step = self.iteration
        if self.iteration <= 20:
            self.iteration += 1
            return step
        else:
            raise StopIteration
