size = 20

def f():
    print("f")


def g():
    size = "a7b"
    print(size)
    f = 453678    # this is now lokal and f is no more a function
    print(f)
   # f()          # 'int' object is not callable


f()
g()
print(size)

# innere Funktion innerhalb umschließender Funktion
def print_with_indent(strings, n):
    def indented_sting(s, n):
        return " " * n + s

    print()
    for s in strings:
        print(indented_sting(s, n))
    for s in strings:
        print(indented_sting(s, 2 * n))


print_with_indent(["Groovy", "C#", "Typescript"], 6)