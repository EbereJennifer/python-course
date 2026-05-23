#1. Type conversion functions: Used to convert data types:

int("5")      # 5
float("3.2")  # 3.2
str(10)       # "10"
bool(0)       # False

#2. Information & inspection

type(5)       # <class 'int'>
len("hello")  # 5
id(x)         # memory address

#3. Math-related functions
abs(-10)      # 10
round(3.6)    # 4
min(1, 2, 3)  # 1
max(1, 2, 3)  # 3
sum([1, 2, 3])# 6

#4. Iteration & collections
range(5)           # 0 to 4
list((1, 2, 3))    # [1, 2, 3]
tuple([1, 2, 3])   # (1, 2, 3)
set([1, 1, 2])     # {1, 2}

#Logic & conditions
all([True, True])     # True
any([False, True])    # True

#Input & output
print("Hello")     # outputs text
n = input("Enter: ")   # user input
print(n)

#Advanced / functional tools
map(str, [1, 2, 3])     # convert to strings
filter(lambda x: x > 0, [-1, 2, 3])
zip([1,2], ['a','b'])   # pairs elements

Object-related
dir(object)        # list attributes
help(len)          # documentation
isinstance(5, int) # True

A few special ones
open("file.txt")   # open a file
eval("2 + 2")      # evaluate expression (use carefully!)


import math
print(round(3.9))
print(abs(-3.9))

"""
math.ceil(x): Returns the smallest integer greater than or equal to x.

math.floor(x): Returns the largest integer less than or equal to x.

math.fabs(x): Returns the absolute value of x.

math.factorial(x): Returns the factorial of x.

math.gcd(x, y): Returns the greatest common divisor of x and y.

math.sqrt(x): Returns the square root of x.

math.pow(x, y): Returns x raised to the power of y.

math.log(x, base): Returns the logarithm of x to the specified base.
"""

print(math.ceil(2.3)) # Output: 3
print(math.floor(2.3)) # Output: 2
print(math.fabs(-10)) # Output: 10.0
print(math.factorial(5)) # Output: 120
print(math.gcd(15, 5)) # Output: 5
print(math.sqrt(16)) # Output: 4.0
print(math.pow(2, 3)) # Output: 8.0
print(math.log(8, 2)) # Output: 3.0