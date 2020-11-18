# list in Python is the sequence. Each element of a sequence is assigned a number - its position or index.
# The first index is zero, the second index is one, and so forth

# There are certain things you can do with all sequence types. These operations include indexing, slicing, adding,
# multiplying, and checking for membership. In addition, Python has built-in functions for finding the length of a
# sequence and for finding its largest and smallest elements.

# example:
l_types_in = ['physics', 1997, [], {}, (), set(), True, None]

# -> access values in lists
list1 = ['physics', 'chemistry', 1997, 2000]
list2 = [1, 2, 3, 4, 5, 6, 7]
print("list1[0]: ", list1[0])
print("list2[1:5]: ", list2[1:5])

# update single or multiple elements of lists by giving the slice on the left-hand side of the assignment operator,
# and you can add to elements in a list with the append() method
listX = ['physics', 'chemistry', 1997, 2000]
print("Value available at index 2 : ", listX[2])
listX[2] = 2001
print("New value available at index 2 : ", listX[2])

# -> remove a list element
del list2[2]
print("After deleting value at index 2 : ", list2)

# -> Basic List Operations
# Python                         Expression	                 Results	Description
# len([1, 2, 3])	             3                              Length
# [1, 2, 3] + [4, 5, 6]	        [1, 2, 3, 4, 5, 6]	            Concatenation
# ['Hi!'] * 4	                ['Hi!', 'Hi!', 'Hi!', 'Hi!']	Repetition
# 3 in [1, 2, 3]	            True	                        Membership
# for x in [1, 2, 3]: print x,	1 2 3	                        Iteration

# -> Indexing, Slicing, and Matrixes
L = ['spam', 'Spam', 'SPAM!']
# Python                        Expression	                      Results	Description
#   L[2]	                        SPAM!	                        Offsets start at zero
#   L[-2]	                        Spam	                        Negative: count from the right
#   L[1:]	                    ['Spam', 'SPAM!']	                Slicing fetches sections

# -> List Functions
# 	len(list) Gives the total length of the list.
len(listX)
#   max(list) Returns item from the list with max value.
max(list2)
#   min(list) Returns item from the list with min value.
min(list2)
#   list(seq) Converts a tuple into list.

# -> List Methods
#   list.append(obj) Appends object obj to list
listX.append(list2)
# 	list.count(obj) Returns count of how many times obj occurs in list
listX.count(2000)
# 	list.extend(seq) Appends the contents of seq to list
listX.extend([2009, 'manni'])
# 	list.index(obj) Returns the lowest index in list that obj appears
listX.index(2000)
#   list.insert(index, obj) Inserts object obj into list at offset index
listX.insert(4, 3400)
#   list.pop(obj=list[-1]) Removes and returns last object or obj from list by index
listX.pop(3)
#   list.remove(obj)  Removes object obj from list
listX.remove('chemistry')
#   list.reverse() Reverses objects of list in place
listX.reverse()
# 	list.sort([func]) Sorts objects of list, use compare func if given
listX.sort()

# List Comprehension
comp_list = [x * 2 for x in range(10)]  # [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]
comp_list2 = [x ** 2 for x in range(7) if x % 2 == 0]  # [4, 16, 36]

nums = [1, 2, 3, 4, 5]
letters = ['A', 'B', 'C', 'D', 'E']
nums_letters = [[n, l] for n in nums for l in letters]  # [[1, 'A'], [1, 'B'], [1, 'C'], [1, 'D'], [1, 'E'],...]

iter_string = "some text"
comp_list3 = [x for x in iter_string if x != " "]  # ['s', 'o', 'm', 'e', 't', 'e', 'x', 't']
