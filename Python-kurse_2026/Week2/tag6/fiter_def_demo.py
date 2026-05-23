# You use a function (def) when you want to:

# reuse, organize, or simplify code
# so instead of writing or inputing values everytime, def helps return it, so you can always input easily
# def read_int():
#     return int(input("integer: "))
#
# n1 = read_int()
# n2 = read_int()
# n3 = read_int()
#
# 👉 Cleaner, reusable ✅
"""
Name	                        Meaning
words	                        The entire list
s	                            One element from the list
has_3_or_more_characters	    Function that tests each element
"""

words = ["C++", "Javascript", "C", "D", "Java"]
print(words)

#Test methode
def has_3_or_more_characters(s):
    truth_value = len(s) >= 3
    return truth_value

filter_result = filter(has_3_or_more_characters, words) # filter() = passes each item to your function (s)
print(filter_result)    # this will give < filter object at 0x000001E1C71B29E0>, so you need list, to bring out the result

filtered_words = list(filter_result)   # lists out the result
print(list(filtered_words))




"""
filtern
#benögtigt: eine Funktion, die auf die einzelnen Listenelemente angewendet wird und die bool zurückliefert
"""
#Required: a function that is applied to each list element and returns a boolean value

def ist_gerade(n):       # ist_gerade means even'
    return n % 2 == 0    # returns: True → even number and False → odd number

gefiltert = filter(ist_gerade, [2, 4, 5, 2, 8, 4])   # “Go through the list and keep only the elements where ist_gerade returns True.”
for elem in gefiltert:
    print(elem, end=" ")
