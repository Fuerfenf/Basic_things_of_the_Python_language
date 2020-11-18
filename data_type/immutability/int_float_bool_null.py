#-> int
    #-> signed integer int([object], [radix])
        #-> radix:
            #-> bin(number)
                #-> bin(19) # '0b10011' or '10011'
            #-> hex(number)
                #-> hex(19) # '0x13'
            #-> oct(number)
                #-> oct(19) # '0o23'
        #-> methods:
            #-> int.bit_length() : count bits for view number in binary without sign and top nulls
                #-> n = -37 # '-0b100101'
                #-> n.bit_length() # 6
            #-> int.to_bytes(length, byteorder, *, signed=False) : return byte line from number
                #-> (1024).to_bytes(2, byteorder='big') # b'\x04\x00'
                #-> (1024).to_bytes(10, byteorder='big') # b'\x00\x00\x00\x00\x00\x00\x00\x00\x04\x00'
            #-> int.from_bytes(bytes, byteorder, *, signed=False) : return number from byte line
                #-> int.from_bytes(b'\x00\x10', byteorder='big') # 16
                #-> int.from_bytes(b'\x00\x10', byteorder='little') # 4096

#-> float
    #-> floating point real values
        #-> for greater accuracy used Decimal and Fraction
    #-> methods:
        #-> float.as_integer_ratio() return pair numerator denominator !!!! USE ONLY MODULE decimal
            #-> Decimal(0.25).as_integer_ratio() # (1, 4) ps 1/4 = 0.25
        #-> float.is_integer()
            #-> (1.0).is_integer() # True
            #-> (1.555).is_integer() # False
        #-> float.hex()
            #-> (10.5).hex() # '0x1.5000000000000p+3'
        #-> float.fromhex(s)
            #-> float.fromhex('0x1.5000000000000p+3') # 10.5

#-> complex
    #-> complex numbers
        #-> complex(1, 2) # (1+2j)

#-> bool
    #->  object.__bool__(self) -> bool
        #-> True
            #->  True, bool(10), bool('some')
        #-> False
            #-> False, bool(0), bool(''), bool()

# -> None
    #-> Null 0
        #-> check for None use keyword is:
            #-> box = None
            #-> if box is None: