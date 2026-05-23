from kunden_verwaltung import kundenVerwaltung
from kunde import kunde

def main():
    kunde = Kunde(101_865, "Sira", "sira@microsoft.com")
    verwaltung = KundenVerwaltung()
    verwaltung.anlegen(kunde)
    for k in verwaltung.get_kundenliste():
        print(k)
