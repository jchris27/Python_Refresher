# String data type

# literal assignment
first = 'Jino'
last = 'Alba'

print(type(first))
print(type(first) == str)
print(isinstance(first, str))

# constructor functino
pizza = str('Pepperoni')
print(type(pizza))
print(type(pizza) == str)
print(isinstance(pizza, str))

# Concatenation
fullname = first + " " + last
print(fullname)

fullname += "!"
print(fullname)

# Casting a number to a string
decade = str(1980)
print(type(decade))
print(decade)

statement = "I like rock music from the " + decade + "s."
print(statement)

# Multiple lines
multiline = '''
Hey, how are you?                          
I was just checking in.          
                                All good?
'''
print(multiline)

# Escaping special characters
sentence = 'I\'m back at work!\tHey!\n\nWhere\'s this at\\located?'
print(sentence)

# String mprint(type(first))
print(type(first) == str)
print(isinstance(first, str))

# String Methods

print(first)
print(first.lower())
print(first.upper())
print(first)

print(multiline.title())
print(multiline.replace("good", "ok"))
print(multiline)

# Removing white spaces
print(len(multiline))
multiline += "                                       "
multiline = "               " + multiline
print(len(multiline))

print(len(multiline.strip())) # removes all spaces
print(len(multiline.lstrip())) # removes all leading spaces
print(len(multiline.rstrip())) # removes all trailing spaces
print(multiline)

# Build a menu
title = "menu".upper()
print(title.center(20, "="))
print("Coffee".ljust(16, ".") + "$1".rjust(4))
print("Muffin".ljust(16, ".") + "$2".rjust(4))
print("Cheesecake".ljust(16, ".") + "$4".rjust(4))

# string index values
print(first[1])
print(first[-1])
print(first[1:-1])
print(first[1:])

# Some methods return boolean data
print(first.startswith("J"))
print(first.startswith("j"))
print(first.endswith("Z"))

# Boolean data type
myvalue = True
x = bool(False)
print(type(x))
print(isinstance(myvalue, bool))

# Numeric data types

# integer types
price = 100
best_price = int(80)
print(type(price))
print(isinstance(best_price, int))

# float type
gpa = 3.28
y = float(1.14)
print(type(gpa))
print(isinstance(y, float))

# complex type
comp_type = 5 + 3j
print(type(comp_type))
print(comp_type.real)
print(comp_type.imag)

# Built-in functions for numbers

print(abs(gpa))
print(round(gpa))

print(round(gpa, 1))

# math module
import math

print(math.pi)
print(math.sqrt(64))
print(math.ceil(gpa))
print(math.floor(gpa))

# Casting a string to a number
zipcode = "10001"
zip_value = int(zipcode)
print(type(zip_value))

# Error if you attempt to cast incorrect data
# zip_value = int("New York")