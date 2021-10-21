## Oppgave 5: Egen oppgave
## 1)
## Kod en funksjon som tar inn en liste med deltakere til facebook-arrangementet ditt og lager en ordbok med alle deltakerne og alle informasjonen som finnes i .txt-filen. 
## Brukerne i .txt-filen vil ha formatet: navn : alder : epost. Din jobb er altså å lage en ordbok som er lettere å ta i bruk enn .txt-filen direkte. Du liker også å holde styring på alder-distribusjonen på festene dine så regn også ut gjennomsnittet av alderne på festen din. Skriv ut gjennomsnittsalderen på festen.

## 2)
## Løsning
def gjennomsnittAlder(obj):
    sum = 0
    for el in obj: sum = sum + int(obj[el]["alder"])
    return sum / len(obj.keys())

## Vi bruker navnet som nøkkelen i ordboken
def objAvDeltakere(filnavn):
    artikler = open(f"{filnavn}.txt", "r", encoding='utf-8').read()
    liste = artikler.split("\n")
    tabell = {}
    for el in liste:
        temp = el.split(":")
        tabell[temp[0].strip()] = {
            "navn": temp[0].strip(),
            "alder": temp[1][0:-3].strip(),
            "epost": temp[2].strip(),
        }
    print(f"Gjennomsnittsalderen til deltakerne på festen din er: {round(gjennomsnittAlder(tabell), 2)} år.")

objAvDeltakere("deltakere")