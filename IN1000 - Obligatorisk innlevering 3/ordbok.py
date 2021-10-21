## Oppgave 2: Ordbok
varer = {
    "melk": 14.90,
    "brød": 24.90,
    "pizza": 39.90,
    "yoghurt": 12.90,
}
print(varer)

## Denne funksjonen legger inn varer i varer ordboken
def vareInnlegger():
    vare = input("Tast inn vare: ")
    pris = float(input("Tast inn pris: "))
    varer[vare] = pris

vareInnlegger()
vareInnlegger()
print(varer)