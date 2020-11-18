#-> &
# Operator copies a bit to the result if it exists in both operands
print(2 & 4) # return 0 (2=0b10, 4=0b100 -> 010 & 100 = 000 (0))

#-> |
# It copies a bit if it exists in either operand.
print(2 | 4) # return 6 (2=0b10, 4=0b100 -> 010 | 100 = 110 (6))

#-> ~
# It copies the bit if it is set in one operand but not both.
print(~3) # return -4 (3=0b11 -> -0b11+1 = -0b100 = -4)
print(~4) # return -5 (4=0b100 -> -0b100+1 = -0b101 = -5)

#-> ^
# It is unary and has the effect of 'flipping' bits.
print(4 ^ 2) # return 6 (2=0b10, 4=0b100 -> 010 ^ 100 = 110 (6))
print(5 ^ 4) # return 1 (2=0b101, 4=0b100 -> 101 ^ 100 = 001 (1))

#-> <<
# The left operands value is moved left by the number of bits specified by the right operand.
print(7 << 2) # return 28 (7=ob0000 0111, move left 2 points = ob0001 1100 (28))

#-> >>
# The left operands value is moved right by the number of bits specified by the right operand.
print(7 >> 2) # return 1 (7=ob0000 0111, move right 2 points = ob0000 0001 (1))
