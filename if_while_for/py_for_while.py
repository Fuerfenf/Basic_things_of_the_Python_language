# for iterator_var in sequence:
#     statements(s)

# Iterating over a list
print("List Iteration")
l = ["geeks", "for", "geeks"]
for i in l:
    print(i)

# Iterating over a tuple (immutable) 
print("\nTuple Iteration")
t = ("geeks", "for", "geeks")
for i in t:
    print(i)

# Iterating over a String 
print("\nString Iteration")
s = "Geeks"
for i in s:
    print(i)

# Iterating over dictionary 
print("\nDictionary Iteration")
d = dict()
d['xyz'] = 123
d['abc'] = 345
for i in d:
    print("%s  %d" % (i, d[i]))

# continue
for letter in 'geeksforgeeks':
    if letter == 'e' or letter == 's':
         continue
    print('Current Letter :', letter)

# break
for letter in 'geeksforgeeks':

    # break the loop as soon it sees 'e'
    # or 's'
    if letter == 'e' or letter == 's':
        break
print('Current Letter :', letter)

# pass
for letter in 'geeksforgeeks':
    pass
print('Last Letter :', letter)


# while expression:
#     statement(s)
count = 0
while count < 3:
    count = count+1
    print("Hello Geek")
