### set and frozenset
* manipulations with set/frozenset:
    * **len (s)** 
        > the number of elements in the set (the size of the set)
    * **x in s**
        > whether x belongs to the set s
    * **set.isdisjoint (other)**
        > True if set and other have no elements in common.
    * **set == other** 
        > all elements of set belong to other, all elements of other belong to set
    * **set.issubset (other)** or **set <= other** 
        > all elements of set belong to other
    * **set.issuperset (other)** or **set> = other**    
        > are the same
    * **set.union (other, ...)** or **set | other | ...**   
        > union of several sets
    * **set.intersection (other, ...)** or **set & other & ...**    
        > is an intersection
    * **set.difference (other, ...)** or **set - other - ...**
        > is a set of all set elements that do not belong to any of the other
    * **set.symmetric_difference (other)** or **set ^ other**  
        > is a set of elements that appear in the same set, but do not occur in both
    * **set.copy ()** 
        > is a copy of the set.
* changing set:
    * **set.update (other, ...)** or **set | = other | ... **
        > an association
    * **set.intersection_update (other, ...)** or **set & = other & ...** 
        > intersection
    * **set.difference_update (other, ...)** or **set - = other | ...**
        > subtraction
    * **set.symmetric_difference_update (other)** or **set ^ = other** 
        > a set of elements that appear in one set, but do not occur in both
    * **set.add (elem)**
        > adds an element to the set
    * **set.remove (elem)**
        > removes an element from the set. KeyError if no such element exists
    * **set.discard (elem)**
        > removes an element if it is in a set
    * **set.pop ()** 
        > removes the first element from the set. Since the sets are not ordered, it is impossible to say for sure which element will come first
    * **set.clear ()**
        > set clear