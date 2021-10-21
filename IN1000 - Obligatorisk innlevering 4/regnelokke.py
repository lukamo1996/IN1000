## Oppgave 2: Regning med løkker
## 1) og 2)
## While løkken looper så lenge variabelen num ikke er lik 0. Straks brukeren taster inn 0 så stopper den opp.
arr = []
num = None
while(num != 0):
    num = int(input("Tast inn et tall: "))
    arr.append(num)

## 3)
for el in arr: print(el)

## 4)
minSum = 0
for el in arr: minSum += int(el)
print(minSum)

## 5)
## Hvis det gitte midlertidige elementet er større enn max, sett max til elementet, ellers nei.
max = arr[0]
min = arr[0]
for el in arr:
    if el > max:
        max = el

## Hvis det gitte midlertidige elementet er mindre enn min, sett min til elementet, ellers nei.
for el in arr:
    if el < min:
        min = el

## Her skriver vi ut det største og minste tallet
print("Dette er det største tallet: ", max)
print("Dette er det minste tallet: ", min)
