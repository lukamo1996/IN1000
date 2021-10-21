## Oppgave 4: Kodeforstaaelse og feilsoking
## 1) Nei. Dette er ikke lovlig kode siden man ikke kan addere et heltall (int) med tekst (string). Dette problemet kan løses ved å printe ut "b + 'Hei!'" i en F-string, f.eks. print(f"{navn} + {tall}"). Da unngår man at python prøver å addere et tall med tekst. Eventuelt så kan man også presisere at man ønsker å konvertere heltallet til tekst først ved å legge tallverdien inn i str() metoden.
## 2) Vi vil få en feilmelding som påpeker at å addere tall og tekst ikke går an; "TypeError: must be str, not int"

## Koden i oppgaven, løst så den fungerer
a = input("Tast inn et heltall! ")
b = int(a)
if b < 10:
    print (str(b) + "Hei!")