## Trix 4.3: Minst og størst
liste = [6, -4, 7, -2, 8, -3, 9, -11]
minst = liste[0]
størst = liste[0]

for el in liste:
    if el > størst: størst = el
    if el < minst: minst = el
print("Minst:", minst, "Størst:", størst)