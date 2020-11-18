# set can consist of different elements, the order of elements in a set is undefined. You can add and remove elements to
# a set, you can iterate over the elements of a set, you can perform operations on sets
# (union, intersection, difference). You can check if an element belongs to a set

# in sets the order of storage of elements is undefined
# This makes it possible to perform operations such as “check whether an element belongs to a set”
# faster than simply iterating over all the elements of a set.

# The elements of a set can be any immutable data type: numbers, strings, tuples. Mutable data types cannot be
# elements of a set.

# Each element can be included in the set only once

# Set operations
# A | B       A.union (B)                     Returns the set that is the union of the sets Aand B.
# A | = B     A.update (B)                    Adds Aall elements from the set to the set B.
# A & B       A.intersection (B)              Returns the set that is the intersection of the sets Aand B.
# A & = B     A.intersection_update (B)       Leaves in the set Aonly those elements that are in the set B.
# A - B       A.difference (B)                Returns the difference of the sets A and B
#                                             (elements included in A, but not included in B).
# A - = B     A.difference_update (B)         Removes Aall elements from the set B.
# A ^ B       A.symmetric_difference (B)      Returns the symmetric difference of the sets A and B
#                                             (elements included in A or in B, but not both of them at the same time).
# A ^ = B    A.symmetric_difference_update(B)     Writes to the Asymmetric difference of the sets Aand B.
# A <= B     A.issubset (B)                   Returns trueif Ais a subset B.
# A> = B     A.issuperset (B)                 Returns trueif Bis a subset A.
# A <B                                        Equivalent to A <= B and A != B
# A> B                                        Equivalent to A >= B and A != B

# Creating a Set
set1 = set()

#
# Adding element and tuple to the Set
set1.add(8)
set1.add(9)
set1.add((6, 7))

# Adding elements to the Set
# using Iterator
for i in range(1, 6):
    set1.add(i)

# Methods Sets
# Operation                       Equivalent                      Result
# s.update(t)                         s |= t              return set s with elements added from t
#                                                          (t = lists, strings, tuples, sets )
# s.intersection_update(t)            s &= t              return set s keeping only elements also found in t
# s.difference_update(t)              s -= t              return set s after removing elements found in t
# s.symmetric_difference_update(t)    s ^= t              return set s with elements from s or t but not both
# s.add(x)                                                add element x to set s
# s.remove(x)                                             remove x from set s; raises KeyError if not present
# s.discard(x)                                            removes x from set s if present
# s.pop()                                        remove and return an arbitrary element from s; raises KeyError if empty
# s.clear()                                               remove all elements from set s
# https://www.geeksforgeeks.org/python-sets/

