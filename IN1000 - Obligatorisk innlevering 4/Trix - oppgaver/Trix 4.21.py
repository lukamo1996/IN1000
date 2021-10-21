## Trix 4.21: Skattejakt
## Vi lager et skattekart
skattekart = []
for i in range(0, 5, 1):
    rad = []
    for el in range(0, 5, 1): 
        rad.append("O")
        skattekart.append(rad)

## Denne funksjonen printer ut skattekartet
def printSkattekart():
    for el in skattekart: print(el, end = "\n")

## Denne funksjonen er ansvarlig for gjettingen
def gjett():
    while(True):
        g = [int(el) for el in input("Gjett en kordinat i dette formatet: 2, 1: ").split(",")]
        if 0 <= g[0] < len(skattekart) and 0 <= g[1] < len(skattekart[g[0]]):
            print(g)
            return g
        else: print("Det er ikke en gyldig koordinat, gjett på nytt:")

## Dette er selve spillet
def spill():  
    print("Dette er skattekartet ditt, velg en koordinat der du vil begrave den dyrebare skatten din")
    printSkattekart()
    koordinat = [int(el) for el in input("Spiller 1 begynner. Velg en koordinat i dette formatet: 1, 1: ").split(",")]

    if 0 <= koordinat[0] < len(skattekart) and 0 <= koordinat[1] < len(skattekart[koordinat[0]]): skattekart[koordinat[0]][koordinat[1]] = "X"
    else: 
        print("Den koordinaten eksisterer ikke, velg en koordinat på nytt: ")
        spill()
    printSkattekart()

    for i in range(0, 3, 1):
        gjetteForsøk = gjett()
        if skattekart[gjetteForsøk[0]][gjetteForsøk[1]] == "X":
            printSkattekart() 
            return "Du vinner!"
        else:
            if i == 2:
                printSkattekart()
                return "Du tapte"
            else:
                print("Bom, prøv på nytt: ")
                skattekart[gjetteForsøk[0]][gjetteForsøk[1]] = "B"
                printSkattekart()

## Kjør spill
print(spill())