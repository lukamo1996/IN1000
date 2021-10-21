## Oppgave 6: Egen oppgave
## 1) I denne oppgaven så skal du lage et program som lar deg holde styr på brukere på en webside som liker å snakke om hobbyene sine. Du skal ta i bruk flere funksjoner som har forskjellige roller og du skal bruke både løkker, lister, ordbøker og nøstede ordbøker. Du skal også la brukeren ha muligheten til å redigere tilstedeværende brukere i ordboken, slette brukere, legge dem til, søke opp brukere og se alle brukere. Hobbyene skal lagres i lister og printes ut via for løkker.

brukere = {}

## 2) Brukerinfo er funksjonen som brukeren først ringer. Her blir brukeren spurt om hva de ønsker å gjøre.
def brukerInfo():
    valget = input("\n Hei, hva ønsker du å gjøre? Tast inn:\n 1: Hvis du vil legge til en ny bruker. \n 2: Hvis du vil redigere en eksisterende bruker. \n 3: Hvis du vil slette en bruker. \n 4: Hvis du vil se info om en bruker. \n 5: Hvis du vil se en liste over alle brukere. \n 6: Hvis du vil avslutte programmet. \n Valg: ")

    if valget == "1": leggTil()
    elif valget == "2": redigerBruker()
    elif valget == "3": slettBruker()
    elif valget == "4": seBruker()
    elif valget == "5": seAlleBrukere()
    elif valget == "6":
        print("Ha de bra :)")
        return None
    else:
        print("\n Det er ikke et valg.")
        brukerInfo()

## Denne funksjonen er ansvarlig for å legge til brukere i systemet. Den sjekker om brukeren er tilstede i ordboken. Hvis den er den så får brukeren en feilmelding og brukerInfo funksjonen blir kjørt på nytt, og return-callen utsatt helt til brukeren avslutter programmet. Vi har også en bekreftpassord seksjon nedenfor, der brukeren må skrive inn riktig passord på nytt for at brukeren skal kunne bli opprettet.
def leggTil():
    brukernavn = input("\nVelg et brukernavn: ")
    if brukernavn in brukere:
        print("\nDen brukeren finnes allerede")
        brukerInfo()

    epost = input("\nHva er e-posten din: ")
    hobbyer = input("\nSkriv inn hobbyene dine: e.g. tennis, piano, fjellturer, musikk etc.: ")
    passord = input("\nVelg et passord: ")
    bekreftpassord = input("\nSkriv passordet ditt på nytt: ")

    if passord == bekreftpassord:
        brukere[brukernavn] = {
            "brukernavn": brukernavn,
            "epost": epost,
            "passord": passord,
            "hobbyer": hobbyer.split(", "),
        }
        print("\nDu har herved lagt til brukeren", brukere[brukernavn]["brukernavn"])
    else:
        print("\nPassordene samsvarer ikke.")
        print("\nPrøv på nytt.")
    brukerInfo()

## Denne funksjonen er ansvarlig for å redigere brukere. Her sjekker vi om brukeren allerede er tilstede i brukere-ordboken. Vi sjekker så hvilket valg brukeren tok og gjør de adekvate responsene på valget de tar. Hvis brukere vil endre hobbyer så looper vi over hobbyene og viser brukeren alle de nye hobbyene de har lagt til.
def redigerBruker():
    bruker = input("\nSkriv inn brukernavnet til brukeren du vil redigere: ")
    if bruker in brukere:
        valg = input("\nHva vil du gjøre med denne brukeren? Skriv: \n1. Hvis du vil endre passord.\n2: Hvis du vil endre e-postadresse. \n3. Endre hobbyene dine. ")
        if valg == "1":
            passord = input("\nHva vil du at ditt nye passord skal være: ")
            bekreftpassord = input("\nBekreft passordet ditt: ")
            if passord == bekreftpassord:
                brukere[bruker]["passord"] = passord
                print("\nPassordet ditt har blitt endret. ")
            else:
                print("\nPassordet ditt må samsvare med bekreftet passord.")
        elif valg == "2":
            epost = input("Hva vil du at at din nye e-postadresse skal være: ")
            brukere[bruker]["epost"] = epost
            print("\nE-postadressen din har blitt endret. ")
        elif valg == "3":
            hobbyer = input("\nSkriv inn dine nye hobbyer e.g. piano, trening, dans osv. ").split(", ")
            brukere[bruker]["hobbyer"] = hobbyer
            print("\nDine nye hobbyer har blitt lagt til. Her ser du dem:")
            for el in brukere[bruker]["hobbyer"]:
                print(el)
        else:
            print("Det valget finnes ikke.")
    else:
        print("Den brukeren finnes ikke.")
    brukerInfo()

## Denne funksjonen er ansvarlig for å slette en gitt bruker fra bruker-ordboken. Vi har en dobbeltsjekk bit inni funksjonen for å være sikker på at brukeren faktisk vil slette den gitte brukeren.
def slettBruker():
    bruker = input("\nTast inn brukeren du vil slette: ")
    if bruker in brukere:
        valg = input(f"\nEr du sikker på at du vil slette {bruker}. Skriv JA/NEI: ")
        if valg == "JA":
            bekreft = input("\n100% sikker? Skriv JA/NEI: ")
            if bekreft == "JA":
                del brukere[bruker]
                print("\nBrukeren har blitt slettet")
            else:
                print("\nOkei, brukeren slettes ikke.")
        elif valg == "NEI":
            print("\nOkei, brukeren slettes ikke.")
        else:
            print("\nDet er ikke et valg")
    else:
        print("\nDen brukeren finnes ikke.")
    brukerInfo()

## Denne funksjonen er ansvarlig for å vise all info som er lagret om en gitt bruker. Vi looper over alle hobbyene til den gitte brukeren og printer de ut for personen.
def seBruker():
    bruker = input("\nHvilken bruker vil du se informasjon om: ")
    if bruker in brukere:
        print("\nInfo om følgende bruker: ", bruker)
        print("\nBrukernavnet er: ", bruker)
        print("\nEpostadressen er: ", brukere[bruker]["epost"])
        print("\nPassordet er: ", brukere[bruker]["passord"])
        print("\nHobbyene:\n")
        for el in brukere[bruker]["hobbyer"]:
            print(el)
    else:
        print("\nDen brukeren finnes ikke.")

    brukerInfo()

## Denne funksjonen printer ut alle brukere som er lagret i ordboken.
def seAlleBrukere():
    if brukere == {}:
        print("\n Det er ingen brukere lagt til. ")
    else:
        print("Alle brukere: \n")
        for el in brukere:
            print("\n", brukere[el])
    brukerInfo()

brukerInfo()
