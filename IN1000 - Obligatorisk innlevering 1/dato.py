## Oppgave 3: Problemløsning med beslutninger
## Her henter vi inn de nødvendige verdiene fra brukeren
dag1 = int(input("Oppgi dag for første måneden:"))
måned1 = int(input("Oppgi hvilken måned:"))
dag2 = int(input("Oppgi dagen for andre måned:"))
måned2 = int(input("Oppgi hvilken andre måned:"))

## Først sjekker vi om brukeren har valgt 0 som dato, deretter ledsager den generelle logikken
if(not måned1 or not måned2 or not dag1 or not dag2): print("Det er ikke riktig valg av dato")
elif(måned1 < måned2): print("Riktig rekkefølge!")
elif(måned1 > måned2): print("Feil rekkefølge!")
elif(måned1 == måned2 and dag1 < dag2): print("Riktig rekkefølge!")
elif(måned1 == måned2 and dag1 > dag2): print("Feil rekkefølge!")
elif(måned1 == måned2 and dag1 == dag2): print("Samme dato!")

## Frivillig oppgave
def datoInnlegger():
    dato = input("Skriv inn ønsket dato i gitt format: dag/måned/år e.g. 1/12/2017").split("/")
    ## Vi returnerer et objekt med de gitte verdiene
    return {
        "år": dato[2],
        "måned": dato[1],
        "dag": dato[0]
    }

def riktigRekkefølge():
    ## Datoer blir tildelt verdier
    dato1 = datoInnlegger()
    dato2 = datoInnlegger()

    ## Logikk
    if(dato1["år"] < dato2["år"]): print("Riktig rekkefølge!")
    elif(dato1["år"] > dato2["år"]): print("Feil rekkefølge!")
    elif(dato1["år"] == dato2["år"]and dato1["måned"] < dato2["måned"]): print("Riktig rekkefølge!")
    elif(dato1["år"] == dato2["år"] and dato1["måned"] > dato2["måned"]): print("Feil rekkefølge!")
    elif(dato1["år"] == dato2["år"] and dato1["måned"] == dato2["måned"] and dato1["dag"] < dato2["dag"]): print("Riktig rekkefølge!")
    elif(dato1["år"] == dato2["år"] and dato1["måned"] == dato2["måned"] and dato1["dag"] > dato2["dag"]): print("Feil rekkefølge!")
    elif(dato1["år"] == dato2["år"] and dato1["måned"] == dato2["måned"] and dato1["dag"] == dato2["dag"]): print("Samme dato!")