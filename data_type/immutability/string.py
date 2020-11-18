#-> string includ between ' '/" " (one line) or """ """ (multiline)
#-> examples:
var1 = 'Hello World!'
var2 = "Python Programming"
var3 = '''
    dasdsadsadad
    adasdasdasds
    dadsdsadadad
'''
#-> Escape Characters
# Backslash notation	Hexadecimal character	Description
# \a	                0x07	                Bell or alert
# \b	                0x08	                Backspace
# \cx	 	                                    Control-x
# \C-x	 	                                    Control-x
# \e	                0x1b	                Escape
# \f	                0x0c	                Formfeed
# \M-\C-x	 	                                Meta-Control-x
# \n	                0x0a	                Newline
# \nnn	 	                                    Octal notation, where n is in the range 0.7
# \r	                0x0d	                Carriage return
# \s	                0x20	                Space
# \t	                0x09	                Tab
# \v	                0x0b	                Vertical tab
# \x	 	                                    Character x
# \xnn	                                        Hexadecimal notation, where n is in the range 0.9, a.f, or A.F

#-> String Special Operators
# Operator	    Description	                                Example
#   +         	Concatenation - Adds values on              a + b will give HelloPython
#               either side of the operator
#   *	        Repetition - Creates new strings,           a*2 will give -HelloHello
#               concatenating multiple copies of
#               the same string
#   []	        Slice - Gives the character from 	        a[1] will give e
#               the given index
#   [ : ]	    Range Slice - Gives the characters  	    a[1:4] will give ell
#               from the given range
#   in	        Membership - Returns true if a      	    H in a will give 1
#               character exists in the given string
#   not in	    Membership - Returns true if a         	    M not in a will give 1
#               character does not exist in the
#               given string
#   r/R	        Raw String - Suppresses actual meaning 	    print r'\n' prints \n and print R'\n'prints \n
#               of Escape characters. The syntax for
#               raw strings is exactly the same as for
#               normal strings with the exception of
#               the raw string operator, the letter
#               "r," which precedes the quotation marks.
#                The "r" can be lowercase (r) or
#                uppercase (R) and must be placed immediately
#                preceding the first quote mark.
#   %	        Format - Performs String formatting	        See at next section

#-> String Formatting Operator
# coolest features is the string format operator %
print("My name is %s and weight is %d kg!" % ('Zara', 21)) # My name is Zara and weight is 21 kg!
# Format Symbol	    Conversion
#   %c	            character
#   %s	            string conversion via str() prior to formatting
#   %i	            signed decimal integer
#   %d	            signed decimal integer
#   %u	            unsigned decimal integer
#   %o	            octal integer
#   %x	            hexadecimal integer (lowercase letters)
#   %X	            hexadecimal integer (UPPERcase letters)
#   %e	            exponential notation (with lowercase 'e')
#   %E	            exponential notation (with UPPERcase 'E')
#   %f	            floating point real number
#   %g	            the shorter of %f and %e
#   %G	            the shorter of %f and %E
# Others
#   *	            argument specifies width or precision
#   -	            left justification
#   +	            display the sign
#   <sp>	        leave a blank space before a positive number
#   #	            add the octal leading zero ( '0' ) or hexadecimal leading '0x' or '0X',
#                   depending on whether 'x' or 'X' were used.
#   0	            pad from left with zeros (instead of spaces)
#   %	            '%%' leaves you with a single literal '%'
#   (var)	        mapping variable (dictionary arguments)
#   m.n.	        m is the minimum total width and n is the number of digits
#                   to display after the decimal point (if appl.)

#-> r'expression'
print(r'C:\\nowhere')

#-> Unicode String
# strings in Python are stored internally as 8-bit ASCII, while Unicode strings are stored as 16-bit Unicode
print(u'Hello, world!')

#-> String Methods      https://www.tutorialspoint.com/python/python_strings.htm

#   capitalize()
# Capitalizes first letter of string

#   center(width, fillchar)
# Returns a space-padded string with the original string centered to a total of width columns.

#   count(str, beg= 0,end=len(string))
# Counts how many times str occurs in string or in a substring of string if starting index beg and ending
# index end are given.

#   decode(encoding='UTF-8',errors='strict')
# Decodes the string using the codec registered for encoding. encoding defaults to the default string encoding.

#   encode(encoding='UTF-8',errors='strict')
# Returns encoded string version of string; on error, default is to raise a ValueError unless errors is given
# with 'ignore' or 'replace'.

#   endswith(suffix, beg=0, end=len(string))
# Determines if string or a substring of string (if starting index beg and
# ending index end are given) ends with suffix; returns true if so and false otherwise.

#   expandtabs(tabsize=8)
# Expands tabs in string to multiple spaces; defaults to 8 spaces per tab if tabsize not provided.

#   find(str, beg=0 end=len(string))
# Determine if str occurs in string or in a substring of string if starting index beg
# and ending index end are given returns index if found and -1 otherwise.

#   index(str, beg=0, end=len(string))
# Same as find(), but raises an exception if str not found.

#   isalnum()
# Returns true if string has at least 1 character and all characters are alphanumeric and false otherwise.

#   isalpha()
# Returns true if string has at least 1 character and all characters are alphabetic and false otherwise.

#   isdigit()
# Returns true if string contains only digits and false otherwise.

#   islower()
# Returns true if string has at least 1 cased character and all cased characters are in lowercase and false otherwise.

#   isnumeric()
# Returns true if a unicode string contains only numeric characters and false otherwise.

#   isspace()
# Returns true if string contains only whitespace characters and false otherwise

#   istitle()
# Returns true if string is properly "titlecased" and false otherwise

#   isupper()
# Returns true if string has at least one cased character and all cased characters are in uppercase and false otherwise.

#   join(seq)
# Merges (concatenates) the string representations of elements in sequence seq into a string, with separator string.

#   len(string)
# Returns the length of the string

#   ljust(width[, fillchar])
# Returns a space-padded string with the original string left-justified to a total of width columns.

#   lower()
# Converts all uppercase letters in string to lowercase.

#   lstrip()
# Removes all leading whitespace in string.

#   maketrans()
# Returns a translation table to be used in translate function.

#   max(str)
# Returns the max alphabetical character from the string str.

#   min(str)
# Returns the min alphabetical character from the string str.

#   replace(old, new [, max])
# Replaces all occurrences of old in string with new or at most max occurrences if max given.

#   rfind(str, beg=0,end=len(string))
# Same as find(), but search backwards in string.

#   rindex( str, beg=0, end=len(string))
# Same as index(), but search backwards in string.

#   rjust(width,[, fillchar])
# Returns a space-padded string with the original string right-justified to a total of width columns.

#   rstrip()
# Removes all trailing whitespace of string.

#   split(str="", num=string.count(str))
# Splits string according to delimiter str (space if not provided) and returns list of substrings;
# split into at most num substrings if given.

#   splitlines( num=string.count('\n'))
# Splits string at all (or num) NEWLINEs and returns a list of each line with NEWLINEs removed.

#   startswith(str, beg=0,end=len(string))
# Determines if string or a substring of string (if starting index beg and ending index end are given)
# starts with substring str; returns true if so and false otherwise.

#   strip([chars])
# Performs both lstrip() and rstrip() on string.

#   swapcase()
# Inverts case for all letters in string.

#   title()
# Returns "titlecased" version of string, that is, all words begin with uppercase and the rest are lowercase.

#   translate(table, deletechars="")
# Translates string according to translation table str(256 chars), removing those in the del string.

#   upper()
# Converts lowercase letters in string to uppercase.

#   zfill (width)
# Returns original string leftpadded with zeros to a total of width characters; intended for numbers,
# zfill() retains any sign given (less one zero).

#   isdecimal()
# Returns true if a unicode string contains only decimal characters and false otherwise.


#-> Теперь спецификация формата:
# спецификация ::=  [[fill]align][sign][#][0][width][,][.precision][type]
# заполнитель  ::=  символ кроме '{' или '}'
# выравнивание ::=  "<" | ">" | "=" | "^"
# знак         ::=  "+" | "-" | " "
# ширина       ::=  integer
# точность     ::=  integer
# тип          ::=  "b" | "c" | "d" | "e" | "E" | "f" | "F" | "g" | "G" |
#                   "n" | "o" | "s" | "x" | "X" | "%"
#
# Выравнивание производится при помощи символа-заполнителя. Доступны следующие варианты выравнивания:
# Флаг	Значение
# '<'	Символы-заполнители будут справа (выравнивание объекта по левому краю) (по умолчанию).
# '>'	выравнивание объекта по правому краю.
# '='	Заполнитель будет после знака, но перед цифрами. Работает только с числовыми типами.
# '^'	Выравнивание по центру.
#
# Опция "знак" используется только для чисел и может принимать следующие значения:
# Флаг	Значение
# '+'	Знак должен быть использован для всех чисел.
# '-'	'-' для отрицательных, ничего для положительных.
# 'Пробел'	'-' для отрицательных, пробел для положительных.
#
# Поле "тип" может принимать следующие значения:
# Тип	Значение
# 'd', 'i', 'u'	Десятичное число.
# 'o'	Число в восьмеричной системе счисления.
# 'x'	Число в шестнадцатеричной системе счисления (буквы в нижнем регистре).
# 'X'	Число в шестнадцатеричной системе счисления (буквы в верхнем регистре).
# 'e'	Число с плавающей точкой с экспонентой (экспонента в нижнем регистре).
# 'E'	Число с плавающей точкой с экспонентой (экспонента в верхнем регистре).
# 'f', 'F'	Число с плавающей точкой (обычный формат).
# 'g'	Число с плавающей точкой. с экспонентой (экспонента в нижнем регистре),
#       если она меньше, чем -4 или точности, иначе обычный формат.
# 'G'	Число с плавающей точкой. с экспонентой (экспонента в верхнем регистре),
#       если она меньше, чем -4 или точности, иначе обычный формат.
# 'c'	Символ (строка из одного символа или число - код символа).
# 's'	Строка.
# '%'	Число умножается на 100, отображается число с плавающей точкой, а за ним знак %.

# https://www.geeksforgeeks.org/python-strings/