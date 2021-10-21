## Oppgave 4: UiO brukere
## 1), 2), 3), 4)

ordbok = {}

## Vi prøver først å lage et brukernavn som er basert på fornavn + første bokstav i etternavnet etter at vi har sjekket at fornavn og etternavn ble oppgitt. Deretter looper vi over etternavnet og lager nye brukernavn som vi sjekker om allerede eksisterer i ordboken. Hvis vi har brukt opp alle bokstavene i etternavnet til personen så går vi over til tall. Da har vi en lang for loop, det er umulig at vi har over en million brukere som alle har samme fornavn og etternavn.
def lagBrukernavn(navn):
    navn = navn.lower().split(" ")
    assert navn[0] and navn[1], "Forventet et fornavn og et etternavn, men mottok enten bare et fornavn eller et navn med mellomnavn."
    brukernavn = navn[0]
    for el in list(navn[1]):
        brukernavn = brukernavn + el
        if brukernavn not in ordbok: 
            return brukernavn
        else: 
            continue
    
    ## Hvis brukernavnet er tilstede i ordboken så vet vi at vi ikke har et unikt brukernavn. Da prøver vi å lage et nytt brukernavn ved å legge til tall på slutten. Vi fjerner alltid det siste tallet i brukernavnet hvis brukernavnet allerede finnes for å unngå at vi får brukernavn som er av typen lukamo1234567...
    if brukernavn in ordbok:
        for i in range(0, 1000000, 1):
            brukernavn = brukernavn + str(i)
            if brukernavn not in ordbok: 
                return brukernavn
            else:
                brukernavn = brukernavn[0:-1]
                continue
    else: return navn[0] + navn[1][0]

def lagEpost(brukernavn, suffix):
    assert brukernavn and suffix, "Forventet et brukernavn og en suffix"
    return str(f"{brukernavn}@{suffix}")

def printEposter(dic): 
    for el in dic: print (f"Brukeren {el} har epost-adressen: {dic[el]}")

def enWhileLøkke(): 
    svar = ""
    while(svar != "s"):
        svar = input("Hei, velkommen. Skriv:\n'i' hvis du vil lage brukernavn og eposter\n'p' for å skrive ut alle brukernavn og eposter du har laget\n's' for å avslutte programmet\nDitt valg: ")
    
        if svar == "s": break
        elif svar == "p": printEposter(ordbok)
        elif svar != "i": 
            print("Det der er ikke et valg, prøv på nytt")
            continue
        else:
            navn = input("Skriv inn ditt fulle navn, e.g. Luka Momcilovic: ")
            suffix = input("Skriv inn en suffix for epostadressen din: ")
            brukernavn = f"{lagBrukernavn(navn)}"
            ordbok[brukernavn] = lagEpost(brukernavn, suffix)

enWhileLøkke()