## Oppgave 4: Matplan
beboere = {
    "luka momcilovic": ["musli", "risotto", "spaghetti bolognese"],
    "ola nordmann": ["kyllingsalat", "brødskiver", "ratatouille"],
    "kristine pokahontas": ["nestle sjokokuler", "lammesaute", "mousakka"]
}

def matplan():
    print("Disser er beboere: ")
    for el in beboere: print(el)
    b = input("Skriv inn fullt navn: ").lower().strip()
    if b in beboere: print(f"Din matplan er: {beboere[b][0]} til frokost, {beboere[b][1]} til lunsj og {beboere[b][2]} til middag. Velbekomme!")
    else: print("Du er ikke registrert hos oss.")

matplan()

## 4)

## 4a) En ordbok kunne vært hensiktsmessig til denne oppgaven siden ordbøker har en nøkkel:verdi relasjon. Dette betyr at hvis man ønsker å hente frem et brukernavn fra en ordbok med hundretusenvis av brukernavn så vil dette ta kortere tid enn hvis man brukte en liste. Ordbøker har dessuten også unike nøkkel-verdier, så en ordbok kan ikke ha 2 identiske brukernavn, dette kan en liste. En mengde kunne allikevel også være hensiktsmessig her da den fungerer som en liste med kun unike verdier der to identiske elementer ikke kan forekomme. Det er en slags blanding av en liste og en ordbok. Rekkefølgen av brukernavn er dessuten irrelevant i denne situasjonen og derfor kan en ordbok evt. mengde være det beste valget til denne jobben.

## 4b) Her vil en ordbok kunne være det beste valget da det muliggjør et raskt oppslag i ordboken ved hjelp av en nøkkelverdi samt et videre oppslag etter poengsummen. Her er heller ikke rekkefølgen så viktig og vi ønsker dessuten heller ikke at et brukernavn skal ha flere forskjellige poengsummer på en innlevering. Så en liste er her mindre egnet. En mengde passer ikke ettersom den ikke kan lagre egenskaper til nøkler.

## 4c) Her er nok en liste og mengde begge egnet. Hvis man ønsker å bare ha en liste over hvor mange som har vunnet lotto i år så er en mengde godt egnet. En liste kunne også fungert her hvis man ikke bryr seg om at antallet lottovinnere forekommer flere ganger i listen. En mengde vil her trolig være mest egnet til denne oppgaven siden den vil fungere som en unik liste med navnene på alle de som vant lotto det siste året. Selvfølgelig, en ordbok kunne også her vært aktuell, dette hadde allikevel være mer aktuelt hvis man ønsker å også vite hvor mange ganger hver lottovinner har vunnet. Alle funker.

## 4d) En ordbok er her mest passende ettersom vi kan ha en ordbok med alle gjesters navn som nøkkelverdier og allergier som egenskaper som viser til en liste/mengde med alle tingene de er allergiske mot. Rekkefølgen er heller ikke her viktig, så det har ikke så mye å si om man bruker liste eller mengde.
