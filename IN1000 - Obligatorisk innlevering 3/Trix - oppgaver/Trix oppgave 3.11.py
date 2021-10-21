## Trix oppgave 3.11 - Enkel telefonbok
telefonbok = {
    "Arne": 22334455,
    "Lisa": 95959595,
    "Jonas": 97959795,
    "Peder": 12345678,
}

def guleSider():
    søk = input("Søk etter en person: ")
    if søk in telefonbok: return telefonbok[søk]
    else: return "Vi har ikke indeksert denne personen"

print(guleSider())