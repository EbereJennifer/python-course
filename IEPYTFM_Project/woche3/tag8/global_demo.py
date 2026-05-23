globale_variable = "Inhalt der globalen Variable"

def demo():
    global globale_variable
    print(globale_variable)# nur so Änderung erlaubt

    globale_variable = "Neu"
    print(globale_variable)


demo()