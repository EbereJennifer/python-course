class Auto:
    anzahl_autos = 0
    def __init__(self, marke, modell):
        self.marke = marke
        self.modell = modell
        Auto.anzahl_autos +=1
        # instanzmethode
    def fahren(self):
        print("Auto fahrt")

        # instanzmethode, Name vorgegeben provided
    def __str__(self):
        return f"Auto{self.marke} {self.modell}"

    @classmethod
    def print_anzahl(cls):
        print("Gesamtzahl Autos:", cls.anzahl_autos)

auto1 = Auto("VW", "Passat")
print(auto1) #ruft automatisch auto1.__str__()
print(auto1.__str__()) # gleichbedeutend
auto1.fahren()

auto2 = Auto("Tesla", "Modle3")
auto2.fahren()
print(auto2.__str__())
print("anzahl Autos:", Auto.anzahl_autos)

Auto.print_anzahl()

auto3 = auto1      # beide Variable referenzieren dasselbe Objekt
Auto.print_anzahl()

