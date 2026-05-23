

import array
import random
import sys

for k in range(1, 100, 10):
    liste = random.sample(range(1, 100), k)
    int_array = array.array("i", liste)
    print("Große der liste:", sys.getsizeof(liste))
    print("Große des Array:", sys.getsizeof(int_array))
    print()
