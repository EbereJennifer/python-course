
"""
1)
Klasse Produkt (produkt_id, name, preis, begleittext) soll einige übliche Methoden erhalten.

In einem separaten Skript: Liste von 10 Produkten erzeugen.
Funktion sort_produkte(produkt_liste, key) soll eine In-place Sortierung vornehmen, dann mit einigen unterschiedlichen keys testen.
The `Class Product` (`product_id`, `name`, `price`, `description`) should implement several common methods.

In a separate script: Generate a list of 10 products.
The function `sort_products(product_list, key)` should perform an in-place sort, then test it with several different keys.

"""

class Produkt:
    def __init__(self, produkt_id, name, preis, begleittext):
        self.produkt_id = produkt_id
        self.name = name
        self.preis = preis
        self.begleittext = begleittext

    def __str__(self):
        return f"""Produkt {self.produkt_id}
    Name: {self.name}
    Preis: {self.preis}
    Begleittext: {self.begleittext}
"""

    def __repr__(self):  # “This is how my object should look when it’s represented as text (especially for debugging).”
        s = f"Produkt('{self.produkt_id}', '{self.name}', " \
                    f"{self.preis}, '{self.begleittext}')"
        return s

    def __eq__(self, other):
        # hier ausführlich
        check1 = type(self) == type(other)
        if not check1:
            return False
        check2 = self.produkt_id == other.produkt_id
        check3 = self.name == other.name
        check4 = self.preis == other.preis
        check5 = self.begleittext == other.begleittext
        return check2 and check3 and check4 and check5


def main():
    p = Produkt('P-574563-A', 'Notebook', 1299.99, 'Bahnbrechend')
    print(p)
    print(repr((p)))

if __name__ == "__main__":
    main()

p = Produkt('P-574563-A', 'Notebook', 12456.89, 'Bahnbrechend')
print(p)
print(repr((p)))


