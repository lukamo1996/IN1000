## Oppgave 3: Billettpris
def billettpris():
    billettpris = 0
    alder = int(input("Hvor gammel er du? "))
    if alder <= 17: billettpris = 30
    elif alder >= 63: billettpris = 35
    elif alder > 17: billettpris = 50
    return f"Du må betale: {billettpris} kroner."

for i in range(0, 4, 1): print(billettpris())
## 6)
## Brukere kan skrive inn bokstaver og spesielle symboler (%, ¤, "", \s) som vil gi en feilmelding ved kjøring. Det er også mulig å skrive inn negative verdier, noe som ikke gir mening og vil heller ikke gi en feilmelding.
