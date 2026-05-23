
"""
The array module in Python is used to create arrays of numbers that are more memory-efficient than lists.

🔹 What it is

The array module provides a way to store elements of the same data type (like all integers or all floats) in a compact form.

👉 Unlike Python lists:

Lists can store mixed types ([1, "hello", 3.5])
Arrays store only one type ([1, 2, 3, 4])
🔹 Why use it?
✅ Uses less memory
✅ Faster for large numeric data
❌ Less flexible than lists
🔹 Basic example
import array

arr = array.array('i', [1, 2, 3, 4])  # 'i' means integer type
print(arr)
🔹 Type codes (important)

When creating an array, you must specify the type:

'i' → signed integer
'f' → float
'd' → double (higher precision float)
'b' → signed char (small integers)

Example:

import array

arr = array.array('f', [1.0, 2.5, 3.2])
print(arr)
🔹 Common operations
arr.append(5)        # add element
arr.insert(1, 10)    # insert at index
arr.remove(2)        # remove element
print(arr[0])        # access element
🔹 Key limitation
arr = array.array('i', [1, 2, 3])
arr.append(4.5)  # ❌ Error (wrong type)
🔹 When to use it

Use array when:

You have large numeric datasets
You need better memory efficiency than lists
You don’t need mixed data types
🔹 Modern alternative

In real-world Python, people often use:

NumPy arrays (much more powerful for math and data science)
🧠 Simple summary
list → flexible, general-purpose
array → compact, same-type numbers only
import array as array_module
"""

# Anton
import array as array_module
# Array für ganze zahlen erzeugen

zahlen = array_module.array('i', [2, -9, 0, 17, 3])
print(type(zahlen), zahlen)

for zahl in zahlen:
    print(zahl)


bytes = array_module.array('b', [56, 87, -34])
print(bytes)

print()

bytes.append(-22)
print(bytes)

print()

bytes.pop(0)
print(bytes)

print()

bytes[1] = 111
print(bytes)

print()
for elem in bytes:
    print(elem)

print()
from array import array as array_function # aliasname
float_array = array_function("f", [])
float_array.append(2.456)
float_array.append(-34234)               # it converted this to float
print(float_array)