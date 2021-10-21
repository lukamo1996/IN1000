## Oppgave 5: Egen oppgave
## 1) Lag en prosedyre som tar inn et fullt navn fra en bruker og forteller brukeren om den gitte personen har noen allergier eller ikke. Deltakernes fulle navn skal være nøklene i ordboken, som så viser til en ny ordbok som har "allergier" som en nøkkel til en liste med allergier. Hvis personen ikke er deltaker så skriv ut en melding som gir beskjed om dette. Hvis personen er en deltaker så blir en liste med allergier for den gitte deltakeren skrevet ut til brukeren.

## 2)
## Her har vi en funksjon som tar inn et ønsket navn fra brukeren, gjør teksten til små bokstaver og fjerner eventuelle \s  karakterer fra inputen. "deltaker"-verdien blir så sjekket opp i "deltakere"-ordboken og sjekker om den finnes i deltakere og gir en adekvat respons basert på dette. Hvis den er tilstede så blir allergiene printet ut til brukeren. 
def allergisjekk():
    deltaker = input("Tast inn ønsket deltaker ").lower().strip()
    deltakere = {
        "luka momcilovic": {
            "allergier": ["egg", "sulfitt", "peanøtter"],
        },
        "michael johnsen": {
            "allergier": ["plommer", "melk", "fluor"]
        },
        "christian mathews": {
            "allergier": ["laktose", "gluten"]
        },
        "kristine trintzen johnsen": {
            "allergier": ["gluten"]
        },
        "petter northug": {
            "allergier": []
        },
    }
    if deltaker not in deltakere: print("Du er dessverre ikke påmeldt til dette arrangementet.")
    else: print(f"{deltaker} er allergisk mot: {', '.join(deltakere[deltaker]['allergier'])}")

allergisjekk()
