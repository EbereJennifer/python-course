"""
1)
A RandomIterator class returns random values in the range 0.0–1.0 (decimal numbers). The iteration stops as soon as a value exceeds 0.99.
"""

import random

class RandomIterator:
    def __init__(self, upper_bound):
        self.upper_bound = upper_bound
        self.is_finished = False

    def __iter__ (self):
        return self

    def __next__ (self):
        if self.is_finished:
            raise StopIteration
        zahl = random. random()
        if zahl > self.upper_bound:
            self.is_finished = True
        return zahl

numbers = RandomIterator(0.99)
for n in numbers:
    print(n)