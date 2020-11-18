# Heap queue it is available using “heapq” module
# The property of this data structure in python is that each time the smallest of heap element is popped(min heap).
# Whenever elements are pushed or popped, heap structure in maintained.
# The heap[0] element also returns the smallest element each time.

# Operations on heap :
# 1. heapify(iterable) :- This function is used to convert the iterable into a heap data structure. i.e. in heap order.
# 2. heappush(heap, ele) :- This function is used to insert the element mentioned in its arguments into heap.
#     The order is adjusted, so as heap structure is maintained.
# 3. heappop(heap) :- This function is used to remove and return the smallest element from heap.
#    The order is adjusted, so as heap structure is maintained.
# https://www.geeksforgeeks.org/heap-queue-or-heapq-in-python/?ref=lbp
# https://python-scripts.com/queues

import heapq

# initializing list
li = [5, 7, 9, 1, 3]

# using heapify to convert list into heap
heapq.heapify(li)

# printing created heap
print("The created heap is : ", end="")
print(list(li))

# using heappush() to push elements into heap
# pushes 4
heapq.heappush(li, 4)

# printing modified heap
print("The modified heap after push is : ", end="")
print(list(li))

# using heappop() to pop smallest element
print("The popped and smallest element is : ", end="")
print(heapq.heappop(li))

li1 = [5, 7, 9, 4, 3]
li2 = [5, 7, 9, 4, 3]

# using heapify() to convert list into heap
heapq.heapify(li1)
heapq.heapify(li2)

# using heappushpop() to push and pop items simultaneously
# pops 2
print("The popped item using heappushpop() is : ", end="")
print(heapq.heappushpop(li1, 2))

# using heapreplace() to push and pop items simultaneously
# pops 3
print("The popped item using heapreplace() is : ", end="")
print(heapq.heapreplace(li2, 2))

li1 = [6, 7, 9, 4, 3, 5, 8, 10, 1]

# using heapify() to convert list into heap
heapq.heapify(li1)

# using nlargest to print 3 largest numbers
# prints 10, 9 and 8
print("The 3 largest numbers in list are : ", end="")
print(heapq.nlargest(3, li1))

# using nsmallest to print 3 smallest numbers
# prints 1, 3 and 4
print("The 3 smallest numbers in list are : ", end="")
print(heapq.nsmallest(3, li1))