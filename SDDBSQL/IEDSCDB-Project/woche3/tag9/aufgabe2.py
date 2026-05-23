"""
2)
Try out some of the generator functions, such as
read_lines_from_file(file_path), square_numbers(start, end)
"""

def read_lines_from_file(file_path):
    with open(file_path) as file:
        for line in file:
            line = line.strip()
            if line:
                yield line


gen1 = read_lines_from_file("aufgabe1.py")
print(type(gen1))

for ziele in gen1:
    print(ziele)


def square_numbers(start, end):
    for i in range(start, end + 1):
        yield i ** 2


for quadrat in square_numbers(5, 10):
    print(quadrat)