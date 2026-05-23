
from kunde import Kunde
from daten_ops import DatenHelper

class KundenVerwaltung:
    def __init__(self):
        self.helper = DatenHelper("kunden.db")

    def anlegen(self, kunde):
        self.helper.datensatz_erzeugen(kunde.nummer, kunde.name, kunde.email)

    def get_kundenliste(self):
        # gibt Liste von Objekten des Typs Kunde zurück
        ergebnis = self.helper.alle_daten()
        return [Kunde(zeile[0], zeile[1], zeile[2]) for zeile in ergebnis]