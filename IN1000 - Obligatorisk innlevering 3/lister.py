## Oppgave 1: Lister
## 1)
liste1 = [1, 3, 8]
liste1.append(9)
print(liste1[0])
print(liste1[2])

## 2) og ## 3)
## Her bruker jeg split og map metodene og en lambda funksjon.
## Vi kaller på map-metoden. Map-metoden tar input-verdien som liste-verdi, noe den mottar ved å kalle på input-metoden, hvor brukeren skriver noe inn som så split-metoden kutter opp der det er komma og genererer en liste som mottas av map-metoden. Map-metoden tar også blant annet en lambda-funksjon som argument 1. Her sender map-metoden hvert element i listen generert fra inputen til lambda-funksjonen i form av variabel x. x-variabelen blir så endret til små bokstaver og mellomrom blir fjernet. Denne verdien blir så returnert til map-metoden, og slik holder den på til alle elementene i listen har blitt gått igjennom. Vi ender da opp med et liste-objet. Til slutt sjekker vi bare om "luka" er i denne listen eller ikke.
liste2 = []
liste2 = map(lambda x: x.lower().strip(), input("Oppgi 4 navn adskilt med komma ").split(","))
if "luka" in liste2: print("Du husket meg!")
else: print("Du glemte meg?")

## 4)
sum = 0
produkt = 1
## += betyr sum = sum + el og *= betyr produkt = produkt * el
## [:-2] er en slice-metode, den tar listen og kutter den fra fra index 0 til lengden på listen minus 2
for el in liste1:
    sum += el
    produkt *= el
liste2 = [sum, produkt]
liste3 = liste1 + liste2
print(liste3)
liste3 = liste3[0:-2]
print(liste3)
