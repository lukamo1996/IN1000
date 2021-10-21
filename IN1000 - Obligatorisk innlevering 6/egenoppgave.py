## Oppgave 6: Egen Oppgave
## 1) Jeg valgte oppgaven foreslått i oppgaveteksten.

class Person:
    def __init__(self, navn, alder):
        self._navn = navn
        self._alder = alder
        self._hobbyer = []

    def leggTilHobby(self, hobby):
        self._hobbyer.append(hobby)

    def skrivHobbyer(self):
        print(", ".join(self._hobbyer))

    def skrivUt(self):
        print(self._navn, self._alder)
        self.skrivHobbyer()

    def navn(self):
        return self._navn

    def alder(self):
        return self._alder

    def hobbyer(self):
        return self._hobbyer

def hovedProgram():
    navn = input("Skriv inn navnet på personen du vil legge inn: ")
    alder = int(input("Skriv inn alderen på denne personen: "))
    person = Person(navn, alder)

    valg = None
    while(valg != "stopp"):
        valg = input("Tast inn en hobby du vil legge til, eller tast inn 'stopp' for å avslutte/gå videre: \n")
        if valg != "stopp": person.leggTilHobby(valg)

    print(f"Brukeren du opprettet har følgene egenskaper:\nNavn: {person.navn()}\nAlder: {person.alder()}\nHobbyer: {', '.join(person.hobbyer())}")

hovedProgram()
