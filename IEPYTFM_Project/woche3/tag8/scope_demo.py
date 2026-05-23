global_variable = "global"

def außere_funktion():
    enclosing_variable = "enclosing"
    print(enclosing_variable)
    print(global_variable)

    def innere_funktion():
        lokale_variable = "lokal"
        print("In inneren funktion", lokale_variable, enclosing_variable, lokale_variable)

        innere_funktion()


außere_funktion()