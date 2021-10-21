## Trix 4.9: While-løkke med input
tall = int(input("Tast inn et tall: "))
teller = 0
while(tall >= teller):
    print(teller)
    t = input("Tast inn enda et tall: ")
    if t == "10": break
    teller += 1
