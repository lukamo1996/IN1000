from spillebrett import Spillebrett

#Hovedprogram
def main():
    input("Velkommen skal du være til The Game of Life av John Horton Conway. Trykk enter for å begynne modige eventyrer.")
    rad = int(input("Velg antall rader du begjærer ditt spillbrett skal ha: "))
    kolonner = int(input("Velg nå antall kolonner du begjærer ditt spillbrett skal ha: "))
    print("Spillet loader...")
    input("Ferdig lastet ned. Trykk enter for å starte spillet.")
    spill = Spillebrett(rad, kolonner)
    valg = None
    while(valg != "q"):
        spill.tegnBrett()
        spill.oppdatering()
        valg = input("Trykk enter for å fortsette. (Skriv inn 'q' og trykk enter for å avslutte eventyret: ")

# starte hovedprogrammet
main()