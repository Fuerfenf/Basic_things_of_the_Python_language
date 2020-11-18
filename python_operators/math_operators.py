#max priority run first
#-> +
# priority : 1
print(2 + 4) # 6

#-> -
# priority : 1
print(4 - 2) # 2

#-> *
# priority : 2
print(4 * 2) # 8
print(4.0 * 2) # 8.0 !! return float if one of numbers is float

#-> /
# priority : 2
print(4 / 2) # 2.0  !! always return float

#-> //
# priority : 2
print(4 // 2) # 2
print(3 // 2) # 1

#-> %
# priority : 2
print(4 % 2) # 0
print(19 % 7) # 5
print(2 % 7) # 2 because in 2 zero

#-> **
# priority : 3
print(4 ** 2) # 16

#-> ()
# priority : 4
print(2*(5+2)) # 14