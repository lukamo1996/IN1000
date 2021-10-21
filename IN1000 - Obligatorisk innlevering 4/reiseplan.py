## Oppgave 4: Reiseplan
steder = []
## Vi looper 5 ganger og for hver gang så appender vi ett reisemål til steder frem til vi når 4, ettersom 5 er sluttverdien, men ikke inklusiv.
for el in range(0, 5, 1): steder.append(input("Legg inn et reisemål: "))

klesplagg = []
avreisedatoer = []
## Her lar vi brukeren legge inn et klesplagg og en avreisedato. Vi bruker en if-statement inni for-loopen fordi vi ønsker ikke at brukeren skal veksle mellom å legge inn avreisedato og klesplagg. Vi ønsker at brukere skal legge inn 5 klesplagg og deretter 5 avreisedatoer, uten å hoppe mellom dem.
for el in range(0, 10, 1):
    if el < 5: klesplagg.append(input("Legg inn et klesplagg: "))
    else: avreisedatoer.append(input("Legg inn en avreisedato: "))

reiseplan = [steder, klesplagg, avreisedatoer]

print(reiseplan)
for el in reiseplan: print(el)

indeks1 = int(input("Tast inn indeks 1: "))
indeks2 = int(input("Tast inn indeks 2: "))

if indeks1 >= 0 and indeks1 < len(reiseplan) and indeks2 >= 0 and indeks2 < len(reiseplan[indeks1]):
    print(reiseplan[indeks1][indeks2])
else: print("Ugyldig input!")

## En alternativ måte å gjøre det på.
# try: print(reiseplan[indeks1][indeks2])
# except: print("Ugyldig input!")
