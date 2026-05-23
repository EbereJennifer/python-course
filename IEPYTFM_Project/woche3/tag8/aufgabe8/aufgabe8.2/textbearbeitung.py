# 2)
# Zwei Module textbearbeitung.py und hauptprogramm.py.
# Funktionen in textbearbeitung z.B. umdrehen(text), woerter_zaehlen(text). Two modules: textprocessing.py and mainprogram.py.
# Functions in textprocessing.py, e.g., reverse(text), count_words(text).




def umdrehen(text):
    return text[::-1]

def woerter_zahlen(text):
    return len(text.split())

print(umdrehen("Anaconda"))

print(woerter_zahlen("Java, Python, C++ und Ruby"))


def ersetzen(text, teil, ersetzung):
    return text.replace(teil, ersetzung)


def ist_anfang_oder_ende(text, teil, ersetzung):
    return text. replace(teil, ersetzung)

def ist_anfang_oder(text, teil):
    return text.startswith(teil) or text.endswith(teil)



print(umdrehen("Anaconda"))

print(woerter_zahlen("Java, Python, C++ und Ruby"))

print(ersetzen("Ich mag Java.", "Java", "Python"))

print()


