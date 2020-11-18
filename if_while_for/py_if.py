# -> if statement

# if condition:
#    statement1
# statement2
i = 10
if i > 15:
    print("10 is less than 15")
print("I am Not in if")

# -> if- else
# if (condition):
#     Executes this block if
#     condition is true
# else:
#     Executes this block if
#     condition is false
i = 20
if i < 15:
    print("i is smaller than 15")
else:
    print("i is greater than 15")
print("i'm not in if and not in else Block")

# -> nested-if
# if (condition1):
#     Executes when condition1 is true
#    if (condition2):
#        Executes when condition2 is true
#     if Block is end here
#  if Block is end here
i = 10
if i == 10:
    if i < 15:
        print("i is smaller than 15")
    if i < 12:
        print("i is smaller than 12 too")
    else:
        print("i is greater than 15")

# if-elif-else ladder
# if (condition):
#     statement
# elif (condition):
#     statement
# .
# .
# else:
#     statement
i = 20
if i == 10:
    print("i is 10")
elif i == 15:
    print("i is 15")
elif i == 20:
    print("i is 20")
else:
    print("i is not present")

# ====================================SHORT HAND===========================================
# Short Hand if statement
i = 10
if i < 15: print("i is less than 15")

# Short Hand if-else statement
i = 10
print(True) if i < 15 else print(False)