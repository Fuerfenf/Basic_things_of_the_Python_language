# List Comprehension
comp_list = [x * 2 for x in range(10)]  # [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]
comp_list2 = [x ** 2 for x in range(7) if x % 2 == 0]  # [4, 16, 36]

nums = [1, 2, 3, 4, 5]
letters = ['A', 'B', 'C', 'D', 'E']
nums_letters = [[n, l] for n in nums for l in letters]  # [[1, 'A'], [1, 'B'], [1, 'C'], [1, 'D'], [1, 'E'],...]

iter_string = "some text"
comp_list3 = [x for x in iter_string if x != " "]  # ['s', 'o', 'm', 'e', 't', 'e', 'x', 't']


# Dict Comprehension
dict_comp = {x: chr(65 + x) for x in range(1, 11)}  # {1: 'B', 2: 'C', 3: 'D', 4: 'E', 5: 'F', 6: 'G', 7: 'H',...}
set_comp = {x ** 3 for x in range(10) if x % 2 == 0}  # {0, 8, 64, 512, 216}

# Difference Between Iterable and Iterator
# Iterable is a “sequence” of data, you can iterate over using a loop. The easiest visible example of
# iterable can be a list of integers – [1, 2, 3, 4, 5, 6, 7]. However, it’s possible to iterate over other types of data
# like strings, dicts, tuples, sets, etc.

# Basically, any object that has iter() method can be used as an iterable.
# You can check it using hasattr()function in the interpreter.
hasattr(str, '__iter__')  # True
hasattr(bool, '__iter__')  # False

# Iterator protocol is implemented whenever you iterate over a sequence of data. For example,
# when you use a for loop the following is happening on a background:
#   first iter() - method is called on the object to converts it to an iterator object.
#   next() - method is called on the iterator object to get the next element of the sequence.
#   StopIteration - exception is raised when there are no elements left to call.
simple_list = [1, 2, 3]
my_iterator = iter(simple_list)
print(my_iterator)  # <list_iterator object at 0x7f66b6288630>
next(my_iterator)  # 1
next(my_iterator)  # 2
next(my_iterator)  # 3
next(my_iterator)  # Traceback (most recent call last):
#                    File "<stdin>", line 1, in <module>
#                    StopIteration


# Generator Expressions
def my_gen():
    for x in range(5):
        yield x


next(my_gen())  # 0,1,2,3,4 then error StopIteration


# Generator expression allows creating a generator on a fly without a yield keyword.
gen_exp = (x ** 2 for x in range(10) if x % 2 == 0)
for x in gen_exp:
    print(x)


# block of differences
list_comp2 = [x ** 2 for x in range(10) if x % 2 == 0]  # [0, 4, 16, 36, 64]
gen_exp2 = (x ** 2 for x in range(10) if x % 2 == 0)  # <generator object <genexpr> at 0x7f600131c410>

