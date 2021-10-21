## Oppgave 5: Å telle bokstaver og ord
## Denne funksjonen returnerer antallet ord i den gitte setningen.
def antallOrd(ord): return len(ord.split(" "))

## Denne funksjonen lar hvert ord i den gitte setningen være en nøkkelverdi til en gitt verdi som indikerer antallet ganger ordet forekommer i den gitte setningen. Inni for-loopen bruker vi en ternary operator for å unngå multi-line if-sjekker.
def ordTeller(setning):
    ordbok = {}
    for el in setning.split(" "): ordbok[el] = ordbok[el] + 1 if el in ordbok else 1
    return ordbok

## Denne funksjonen printer først ut lengden på den tildelte setningen ved å ringe antallOrd-funksjonen. Deretter lager den en ordbok ved hjelp av ordTeller funksjonen, som returner verdien til ordbok-variabelen. Deretter looper vi over ordbok variabelene og printer ut hvor mange ganger hver ord forekommer og hvor langt ordet er.
def setningInfo():
    setning = input("Tast inn en setning du vil ha analysert: ")
    print("Lengden på setningen din er: ", antallOrd(setning))
    ordbok = ordTeller(setning)
    for el in ordbok: print("'", el, "'", "forekommer", ordbok[el], "ganger, og består av", len(el), "bokstaver.")

setningInfo()
