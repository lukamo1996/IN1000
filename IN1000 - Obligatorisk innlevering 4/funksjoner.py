## Oppgave 1 - Paramtere og returverdier
## 1)
## Funksjonen tar to tall som argumenter, adderer dem og returnerer dem
def adder(tall1, tall2): print("Summer av: ", tall1, "og", tall2, "er", tall1 + tall2)

adder(1,1)
adder(1,2)

## 2)
## Funksjonen ber om en setning og en bokstav fra brukeren. Deretter ringer den teller-funksjonen, som mottar setning og bokstav som argumenter. Teller funksjonen returnerer så en tallverdi til tellForekomst funksjonen som så returnerer denne verdien til print-funksjonen.
def tellForekomst():
    setning = input("Gi meg en setning: ")
    bokstav = input("Hvilken bokstav vil du telle? ")
    return teller(setning, bokstav)

## 3)
## Denne funksjonen tar i bruk list funksjonen som kutter opp minTekst inn i  sine indivisuelle ASCII-karakterer. Dette tar så count funksjonen imot og teller hvor mange ganger gitt minBokstav forekommer.
def teller(minTekst, minBokstav): return (f"I teksten din så forekommer bokstaven {minBokstav}: {list(minTekst).count(minBokstav)} ganger.")

print(tellForekomst())
