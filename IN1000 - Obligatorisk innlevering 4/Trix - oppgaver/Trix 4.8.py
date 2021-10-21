## Trix 4.8: Nøstet liste
oliste = []
stjerneliste = []
rutenett = []
for i in range(0, 5, 1): 
    oliste.append("o")
    stjerneliste.append("*")

rutenett.append(oliste)
rutenett.append(stjerneliste)
rutenett.append(oliste)

print(rutenett[0])
print(rutenett[1])
print(rutenett[2])

for el in rutenett:
    print(el)